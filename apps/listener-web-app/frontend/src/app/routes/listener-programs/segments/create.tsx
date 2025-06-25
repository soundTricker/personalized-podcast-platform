/**
 * Copyright 2025 Keisuke Tominaga a.k.a soundTricker
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import {Accordion, Button, Card, Checkbox, Label, Select, Textarea, TextInput} from "flowbite-react";
import {Dispatch, ReactNode, RefObject, SetStateAction, useCallback, useEffect, useRef, useState} from "react";
import {useForm} from "@tanstack/react-form";
import {z} from "zod";
import {Route} from './+types/create';
import {dehydrate, QueryClient} from "@tanstack/react-query";
import {useLocation, useNavigate, useParams} from "react-router";
import {
    closestCenter,
    DndContext,
    DragEndEvent,
    KeyboardSensor,
    PointerSensor,
    useSensor,
    useSensors
} from '@dnd-kit/core';
import {
    arrayMove,
    SortableContext,
    sortableKeyboardCoordinates,
    useSortable,
    verticalListSortingStrategy
} from '@dnd-kit/sortable';
import {CSS} from '@dnd-kit/utilities';
import {ListenerProgramSegmentsService, ListenerProgramsService, GoogleOauth2Service} from "@api/requests/services.gen";
import {
    useListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegments,
    useListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramId,
    useListenersServiceGetApiV1ListenersMe,
    useRadioCastsServiceGetApiV1RadioCasts
} from "@api/queries";
import {prefetchUseRadioCastsServiceGetApiV1RadioCasts} from "@api/queries/prefetch";
import {
    ListenerProgramCalendarSegmentUpdate,
    ListenerProgramGmailSegmentUpdate,
    ListenerProgramRSSSegmentUpdate,
    ListenerProgramSchema,
    ListenerProgramWebSegmentUpdate,
    SegmentType
} from "@api/requests/types.gen";

// Google OAuth2 scopes
const GMAIL_SCOPE = "https://www.googleapis.com/auth/gmail.readonly";
const CALENDAR_SCOPE = "https://www.googleapis.com/auth/calendar.events.readonly";

// Function to get required scope for a segment type
const getRequiredScopeForSegmentType = (segmentType: SegmentType): string | null => {
    switch (segmentType) {
        case SegmentType.GMAIL:
            return GMAIL_SCOPE;
        case SegmentType.CALENDAR:
            return CALENDAR_SCOPE;
        default:
            return null;
    }
};

// Common segment fields schema
const commonSegmentSchema = z.object({
    id: z.string().optional(),
    title: z.string().min(1, "タイトルは必須です"),
    description: z.string().optional(),
    constraints: z.string().optional(),
    order: z.number().int(),
    overrideRadioCasts: z.array(z.string()).optional(),
    segmentType: z.nativeEnum(SegmentType)
});

// RSS segment schema
const rssSegmentSchema = commonSegmentSchema.extend({
    segmentType: z.literal(SegmentType.RSS),
    feedUrl: z.string().url("有効なURLを入力してください")
});

// Calendar segment schema
const calendarSegmentSchema = commonSegmentSchema.extend({
    segmentType: z.literal(SegmentType.CALENDAR),
    startOffsetDays: z.number().int(),
    endOffsetDays: z.number().int(),
    calendarId: z.string().min(1, "カレンダーIDは必須です")
});

// Web segment schema
const webSegmentSchema = commonSegmentSchema.extend({
    segmentType: z.literal(SegmentType.WEB),
    urls: z.array(z.string().url("有効なURLを入力してください")).min(1, "少なくとも1つのURLを入力してください")
});

// Gmail segment schema
const gmailSegmentSchema = commonSegmentSchema.extend({
    segmentType: z.literal(SegmentType.GMAIL),
    filter: z.string().min(1, "フィルターは必須です"),
    startOffsetDays: z.number().int(),
    endOffsetDays: z.number().int()
});

// Union type for all segment types
const segmentSchema = z.discriminatedUnion("segmentType", [
    rssSegmentSchema,
    calendarSegmentSchema,
    webSegmentSchema,
    gmailSegmentSchema
]);

// Form schema for the entire form
const formSchema = z.object({
    segments: z.array(segmentSchema)
});

type FormValues = z.infer<typeof formSchema>;

// Default values for new segments by type
const defaultSegmentValues = {
    [SegmentType.RSS]: {
        title: "",
        description: "",
        constraints: "",
        order: 0,
        overrideRadioCasts: [],
        segmentType: SegmentType.RSS,
        feedUrl: ""
    },
    [SegmentType.CALENDAR]: {
        title: "",
        description: "",
        constraints: "",
        order: 0,
        overrideRadioCasts: [],
        segmentType: SegmentType.CALENDAR,
        startOffsetDays: 0,
        endOffsetDays: 7,
        calendarId: ""
    },
    [SegmentType.WEB]: {
        title: "",
        description: "",
        constraints: "",
        order: 0,
        overrideRadioCasts: [],
        segmentType: SegmentType.WEB,
        urls: [""]
    },
    [SegmentType.GMAIL]: {
        title: "",
        description: "",
        constraints: "",
        order: 0,
        overrideRadioCasts: [],
        segmentType: SegmentType.GMAIL,
        filter: "",
        startOffsetDays: 0,
        endOffsetDays: 7
    }
};

export async function loader({params}: Route.LoaderArgs) {
    const queryClient = new QueryClient();
    const {programId} = params;

    // Prefetch program data
    await queryClient.prefetchQuery({
        queryKey: ['listener-programs', programId],
        queryFn: () => ListenerProgramsService.getApiV1ListenerProgramsByListenerProgramId({listenerProgramId: programId})
    });

    // Prefetch segments data
    await queryClient.prefetchQuery({
        queryKey: ['listener-programs', programId, 'segments'],
        queryFn: () => ListenerProgramSegmentsService.getApiV1ListenerProgramsByProgramIdSegments({programId})
    });

    // Prefetch radio casts data
    await prefetchUseRadioCastsServiceGetApiV1RadioCasts(queryClient);

    return {dehydratedState: dehydrate(queryClient)};
}

// Segment form component based on segment type
function SegmentForm(
    {
        segmentType,
        index,
        form,
        radioCasts,
        handleRadioCastChange,
        isRadioCastDropdownOpen,
        setIsRadioCastDropdownOpen,
        radioCastDropdownRef
    }: {
        segmentType: SegmentType;
        index: number;
        form: any;
        radioCasts: any[] | undefined;
        handleRadioCastChange: (segmentIndex: number, radioCastId: string, checked: boolean) => void;
        isRadioCastDropdownOpen: { [key: number]: boolean };
        setIsRadioCastDropdownOpen: Dispatch<SetStateAction<{ [key: number]: boolean }>>;
        radioCastDropdownRef: RefObject<{ [key: number]: HTMLDivElement | null }>;
    }) {
    switch (segmentType) {
        case SegmentType.RSS:
            return (
                <div className="space-y-4">
                    {form.Field({
                        name: `segments[${index}].feedUrl`,
                        children: (field) => (
                            <div>
                                <div className="mb-2 block">
                                    <Label htmlFor={field.name}>RSSフィードURL</Label>
                                </div>
                                <TextInput
                                    id={field.name}
                                    name={field.name}
                                    placeholder="https://example.com/feed.xml"
                                    value={field.state.value}
                                    onChange={(e) => field.handleChange(e.target.value)}
                                    required
                                />
                                {field.state.meta.errors && (
                                    <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                )}
                            </div>
                        )
                    })}

                    {/* ラジオキャスト選択ドロップダウン */}
                    {form.Field({
                        name: `segments[${index}].overrideRadioCasts`,
                        children: (field) => {
                            const selectedRadioCastIds = field.state.value || [];
                            const selectedRadioCasts = radioCasts?.filter(c => selectedRadioCastIds.includes(c.id!)) || [];

                            return (
                                <div ref={el => radioCastDropdownRef.current[index] = el}>
                                    <div className="mb-2 block">
                                        <Label
                                            htmlFor={`radioCasts-${index}`}>コーナーキャスト（最大2つまで選択可能）</Label>
                                    </div>
                                    <div className="relative">
                                        <Button
                                            id={`radioCasts-${index}`}
                                            color="light"
                                            onClick={() => setIsRadioCastDropdownOpen(prev => ({
                                                ...prev,
                                                [index]: !prev[index]
                                            }))}
                                            className="w-full text-left flex justify-between items-center"
                                        >
                                            <span>
                                                {selectedRadioCastIds.length === 0
                                                    ? "選択してください"
                                                    : `${selectedRadioCastIds.length}つ選択中`}
                                            </span>
                                            <svg className="w-4 h-4 ml-2" fill="currentColor" viewBox="0 0 20 20"
                                                 xmlns="http://www.w3.org/2000/svg">
                                                <path fillRule="evenodd"
                                                      d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                                                      clipRule="evenodd"></path>
                                            </svg>
                                        </Button>
                                        {isRadioCastDropdownOpen[index] && (
                                            <div
                                                className="absolute z-10 w-full bg-white rounded-lg shadow-lg mt-1 py-1 max-h-60 overflow-y-auto">
                                                {/* ラジオキャストのリスト */}
                                                {radioCasts?.map(cast => (
                                                    <div key={cast.id} className="px-4 py-2 hover:bg-gray-100">
                                                        <div className="flex items-start">
                                                            <div className="flex items-center h-5">
                                                                <Checkbox
                                                                    id={`cast-${index}-${cast.id}`}
                                                                    checked={selectedRadioCastIds.includes(cast.id!)}
                                                                    onChange={(e) => handleRadioCastChange(index, cast.id!, e.target.checked)}
                                                                />
                                                            </div>
                                                            <div className="ml-3 text-sm">
                                                                <Label htmlFor={`cast-${index}-${cast.id}`}
                                                                       className="font-medium text-gray-900">
                                                                    <div>{cast.name}</div>
                                                                    <div className="text-xs text-gray-500 mt-1">
                                                                        <div><span
                                                                            className="font-semibold">役割:</span> {cast.role === 'RADIO_PERSONALITY' ? 'ラジオパーソナリティ' : cast.role === 'ASSISTANT' ? 'アシスタント' : 'ゲスト'}
                                                                        </div>
                                                                        {cast.personality && <div><span
                                                                            className="font-semibold">性格:</span> {cast.personality}
                                                                        </div>}
                                                                        {cast.voiceName && <div><span
                                                                            className="font-semibold">ボイス名:</span> {cast.voiceName}
                                                                        </div>}
                                                                    </div>
                                                                </Label>
                                                            </div>
                                                        </div>
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                        {selectedRadioCasts.length > 0 && (
                                            <div className="flex flex-col gap-1 mt-2">
                                                {selectedRadioCasts.map(cast => (
                                                    <div key={cast.id}
                                                         className="px-4 py-2 border border-gray-200 rounded">
                                                        <div className="flex items-start">
                                                            <div className="ml-3 text-sm">
                                                                <Label htmlFor={`cast-${index}-${cast.id}`}
                                                                       className="font-medium text-gray-900">
                                                                    {cast.name}
                                                                </Label>
                                                                <div className="text-xs text-gray-500 mt-1">
                                                                    <div><span
                                                                        className="font-semibold">役割:</span> {cast.role === 'RADIO_PERSONALITY' ? 'ラジオパーソナリティ' : cast.role === 'ASSISTANT' ? 'アシスタント' : 'ゲスト'}
                                                                    </div>
                                                                    {cast.personality && <div><span
                                                                        className="font-semibold">性格:</span> {cast.personality}
                                                                    </div>}
                                                                    {cast.voiceName && <div><span
                                                                        className="font-semibold">ボイス名:</span> {cast.voiceName}
                                                                    </div>}
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                    </div>
                                </div>
                            );
                        }
                    })}
                </div>
            );
        case SegmentType.CALENDAR:
            return (
                <div className="space-y-4">
                    {form.Field({
                        name: `segments[${index}].calendarId`,
                        children: (field) => (
                            <div>
                                <div className="mb-2 block">
                                    <Label htmlFor={field.name}>カレンダーID</Label>
                                </div>
                                <TextInput
                                    id={field.name}
                                    name={field.name}
                                    placeholder="カレンダーID"
                                    value={field.state.value}
                                    onChange={(e) => field.handleChange(e.target.value)}
                                    required
                                />
                                {field.state.meta.errors && (
                                    <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                )}
                            </div>
                        )
                    })}
                    <div className="grid grid-cols-2 gap-4">
                        {form.Field({
                            name: `segments[${index}].startOffsetDays`,
                            children: (field) => (
                                <div>
                                    <div className="mb-2 block">
                                        <Label htmlFor={field.name}>開始日オフセット（日）</Label>
                                    </div>
                                    <TextInput
                                        id={field.name}
                                        name={field.name}
                                        type="number"
                                        value={field.state.value}
                                        onChange={(e) => field.handleChange(parseInt(e.target.value))}
                                        required
                                    />
                                    {field.state.meta.errors && (
                                        <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                    )}
                                </div>
                            )
                        })}
                        {form.Field({
                            name: `segments[${index}].endOffsetDays`,
                            children: (field) => (
                                <div>
                                    <div className="mb-2 block">
                                        <Label htmlFor={field.name}>終了日オフセット（日）</Label>
                                    </div>
                                    <TextInput
                                        id={field.name}
                                        name={field.name}
                                        type="number"
                                        value={field.state.value}
                                        onChange={(e) => field.handleChange(parseInt(e.target.value))}
                                        required
                                    />
                                    {field.state.meta.errors && (
                                        <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                    )}
                                </div>
                            )
                        })}
                    </div>

                    {/* ラジオキャスト選択ドロップダウン */}
                    {form.Field({
                        name: `segments[${index}].overrideRadioCasts`,
                        children: (field) => {
                            const selectedRadioCastIds = field.state.value || [];
                            const selectedRadioCasts = radioCasts?.filter(c => selectedRadioCastIds.includes(c.id!)) || [];

                            return (
                                <div ref={el => radioCastDropdownRef.current[index] = el}>
                                    <div className="mb-2 block">
                                        <Label
                                            htmlFor={`radioCasts-${index}`}>ラジオキャスト（最大2つまで選択可能）</Label>
                                    </div>
                                    <div className="relative">
                                        <Button
                                            id={`radioCasts-${index}`}
                                            color="light"
                                            onClick={() => setIsRadioCastDropdownOpen(prev => ({
                                                ...prev,
                                                [index]: !prev[index]
                                            }))}
                                            className="w-full text-left flex justify-between items-center"
                                        >
                                            <span>
                                                {selectedRadioCastIds.length === 0
                                                    ? "選択してください"
                                                    : `${selectedRadioCastIds.length}つ選択中`}
                                            </span>
                                            <svg className="w-4 h-4 ml-2" fill="currentColor" viewBox="0 0 20 20"
                                                 xmlns="http://www.w3.org/2000/svg">
                                                <path fillRule="evenodd"
                                                      d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                                                      clipRule="evenodd"></path>
                                            </svg>
                                        </Button>
                                        {isRadioCastDropdownOpen[index] && (
                                            <div
                                                className="absolute z-10 w-full bg-white rounded-lg shadow-lg mt-1 py-1 max-h-60 overflow-y-auto">
                                                {/* ラジオキャストのリスト */}
                                                {radioCasts?.map(cast => (
                                                    <div key={cast.id} className="px-4 py-2 hover:bg-gray-100">
                                                        <div className="flex items-start">
                                                            <div className="flex items-center h-5">
                                                                <Checkbox
                                                                    id={`cast-${index}-${cast.id}`}
                                                                    checked={selectedRadioCastIds.includes(cast.id!)}
                                                                    onChange={(e) => handleRadioCastChange(index, cast.id!, e.target.checked)}
                                                                />
                                                            </div>
                                                            <div className="ml-3 text-sm">
                                                                <Label htmlFor={`cast-${index}-${cast.id}`}
                                                                       className="font-medium text-gray-900">
                                                                    <div>{cast.name}</div>
                                                                    <div className="text-xs text-gray-500 mt-1">
                                                                        <div><span
                                                                            className="font-semibold">役割:</span> {cast.role === 'RADIO_PERSONALITY' ? 'ラジオパーソナリティ' : cast.role === 'ASSISTANT' ? 'アシスタント' : 'ゲスト'}
                                                                        </div>
                                                                        {cast.personality && <div><span
                                                                            className="font-semibold">性格:</span> {cast.personality}
                                                                        </div>}
                                                                        {cast.voiceName && <div><span
                                                                            className="font-semibold">ボイス名:</span> {cast.voiceName}
                                                                        </div>}
                                                                    </div>
                                                                </Label>
                                                            </div>
                                                        </div>
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                        {selectedRadioCasts.length > 0 && (
                                            <div className="flex flex-col gap-1 mt-2">
                                                {selectedRadioCasts.map(cast => (
                                                    <div key={cast.id}
                                                         className="px-4 py-2 border border-gray-200 rounded">
                                                        <div className="flex items-start">
                                                            <div className="ml-3 text-sm">
                                                                <Label htmlFor={`cast-${index}-${cast.id}`}
                                                                       className="font-medium text-gray-900">
                                                                    {cast.name}
                                                                </Label>
                                                                <div className="text-xs text-gray-500 mt-1">
                                                                    <div><span
                                                                        className="font-semibold">役割:</span> {cast.role === 'RADIO_PERSONALITY' ? 'ラジオパーソナリティ' : cast.role === 'ASSISTANT' ? 'アシスタント' : 'ゲスト'}
                                                                    </div>
                                                                    {cast.personality && <div><span
                                                                        className="font-semibold">性格:</span> {cast.personality}
                                                                    </div>}
                                                                    {cast.voiceName && <div><span
                                                                        className="font-semibold">ボイス名:</span> {cast.voiceName}
                                                                    </div>}
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                    </div>
                                </div>
                            );
                        }
                    })}
                </div>
            );
        case SegmentType.WEB:
            return (
                <div className="space-y-4">
                    <form.Field name={`segments[${index}].urls`} mode="array">
                        {(field) => (
                            <div>
                                <div className="mb-2 block">
                                    <Label htmlFor={`${field.name}[0]`}>URL</Label>
                                </div>
                                {field.state.value.map((url: string, urlIndex: number) => (
                                    <form.Field name={`segments[${index}].urls[${urlIndex}]`}
                                                key={`url-${urlIndex}`}>
                                        {(f) => (
                                            <div key={urlIndex} className="flex items-center mb-2">
                                                <TextInput
                                                    id={`${f.name}`}
                                                    name={`${f.name}`}
                                                    placeholder="https://example.com"
                                                    value={url}
                                                    onChange={(e) => {
                                                        const newUrls = [...field.state.value];
                                                        newUrls[urlIndex] = e.target.value;
                                                        field.handleChange(newUrls);
                                                    }}
                                                    className="flex-grow"
                                                    required
                                                />
                                                <Button
                                                    color="light"
                                                    size="sm"
                                                    className="ml-2"
                                                    onClick={() => {
                                                        console.log("hoge");
                                                        const newUrls = [...field.state.value];
                                                        newUrls.splice(urlIndex, 1);
                                                        field.handleChange(newUrls);
                                                    }}
                                                    disabled={field.state.value.length <= 1}
                                                >
                                                    削除
                                                </Button>
                                            </div>
                                        )
                                        }
                                    </form.Field>
                                ))}
                                <Button
                                    color="light"
                                    size="sm"
                                    className="cursor-pointer"
                                    onClick={() => {
                                        console.log("hoge");
                                        field.handleChange([...field.state.value, ""]);
                                    }}
                                >
                                    URLを追加
                                </Button>
                                {field.state.meta.errors && (
                                    <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                )}
                            </div>
                        )}
                    </form.Field>

                    {/* ラジオキャスト選択ドロップダウン */}
                    {form.Field({
                        name: `segments[${index}].overrideRadioCasts`,
                        children: (field) => {
                            const selectedRadioCastIds = field.state.value || [];
                            const selectedRadioCasts = radioCasts?.filter(c => selectedRadioCastIds.includes(c.id!)) || [];

                            return (
                                <div ref={el => radioCastDropdownRef.current[index] = el}>
                                    <div className="mb-2 block">
                                        <Label
                                            htmlFor={`radioCasts-${index}`}>ラジオキャスト（最大2つまで選択可能）</Label>
                                    </div>
                                    <div className="relative">
                                        <Button
                                            id={`radioCasts-${index}`}
                                            color="light"
                                            onClick={() => setIsRadioCastDropdownOpen(prev => ({
                                                ...prev,
                                                [index]: !prev[index]
                                            }))}
                                            className="w-full text-left flex justify-between items-center"
                                        >
                                            <span>
                                                {selectedRadioCastIds.length === 0
                                                    ? "選択してください"
                                                    : `${selectedRadioCastIds.length}つ選択中`}
                                            </span>
                                            <svg className="w-4 h-4 ml-2" fill="currentColor" viewBox="0 0 20 20"
                                                 xmlns="http://www.w3.org/2000/svg">
                                                <path fillRule="evenodd"
                                                      d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                                                      clipRule="evenodd"></path>
                                            </svg>
                                        </Button>
                                        {isRadioCastDropdownOpen[index] && (
                                            <div
                                                className="absolute z-10 w-full bg-white rounded-lg shadow-lg mt-1 py-1 max-h-60 overflow-y-auto">
                                                {/* ラジオキャストのリスト */}
                                                {radioCasts?.map(cast => (
                                                    <div key={cast.id} className="px-4 py-2 hover:bg-gray-100">
                                                        <div className="flex items-start">
                                                            <div className="flex items-center h-5">
                                                                <Checkbox
                                                                    id={`cast-${index}-${cast.id}`}
                                                                    checked={selectedRadioCastIds.includes(cast.id!)}
                                                                    onChange={(e) => handleRadioCastChange(index, cast.id!, e.target.checked)}
                                                                />
                                                            </div>
                                                            <div className="ml-3 text-sm">
                                                                <Label htmlFor={`cast-${index}-${cast.id}`}
                                                                       className="font-medium text-gray-900">
                                                                    <div>{cast.name}</div>
                                                                    <div className="text-xs text-gray-500 mt-1">
                                                                        <div><span
                                                                            className="font-semibold">役割:</span> {cast.role === 'RADIO_PERSONALITY' ? 'ラジオパーソナリティ' : cast.role === 'ASSISTANT' ? 'アシスタント' : 'ゲスト'}
                                                                        </div>
                                                                        {cast.personality && <div><span
                                                                            className="font-semibold">性格:</span> {cast.personality}
                                                                        </div>}
                                                                        {cast.voiceName && <div><span
                                                                            className="font-semibold">ボイス名:</span> {cast.voiceName}
                                                                        </div>}
                                                                    </div>
                                                                </Label>
                                                            </div>
                                                        </div>
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                        {selectedRadioCasts.length > 0 && (
                                            <div className="flex flex-col gap-1 mt-2">
                                                {selectedRadioCasts.map(cast => (
                                                    <div key={cast.id}
                                                         className="px-4 py-2 border border-gray-200 rounded">
                                                        <div className="flex items-start">
                                                            <div className="ml-3 text-sm">
                                                                <Label htmlFor={`cast-${index}-${cast.id}`}
                                                                       className="font-medium text-gray-900">
                                                                    {cast.name}
                                                                </Label>
                                                                <div className="text-xs text-gray-500 mt-1">
                                                                    <div><span
                                                                        className="font-semibold">役割:</span> {cast.role === 'RADIO_PERSONALITY' ? 'ラジオパーソナリティ' : cast.role === 'ASSISTANT' ? 'アシスタント' : 'ゲスト'}
                                                                    </div>
                                                                    {cast.personality && <div><span
                                                                        className="font-semibold">性格:</span> {cast.personality}
                                                                    </div>}
                                                                    {cast.voiceName && <div><span
                                                                        className="font-semibold">ボイス名:</span> {cast.voiceName}
                                                                    </div>}
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                    </div>
                                </div>
                            );
                        }
                    })}
                </div>
            );
        case SegmentType.GMAIL:
            return (
                <div className="space-y-4">
                    {form.Field({
                        name: `segments[${index}].filter`,
                        children: (field) => (
                            <div>
                                <div className="mb-2 block">
                                    <Label htmlFor={field.name}>Gmailフィルター</Label>
                                </div>
                                <TextInput
                                    id={field.name}
                                    name={field.name}
                                    placeholder="label:inbox is:unread"
                                    value={field.state.value}
                                    onChange={(e) => field.handleChange(e.target.value)}
                                    required
                                />
                                {field.state.meta.errors && (
                                    <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                )}
                            </div>
                        )
                    })}
                    <div className="grid grid-cols-2 gap-4">
                        {form.Field({
                            name: `segments[${index}].startOffsetDays`,
                            children: (field) => (
                                <div>
                                    <div className="mb-2 block">
                                        <Label htmlFor={field.name}>開始日オフセット（日）</Label>
                                    </div>
                                    <TextInput
                                        id={field.name}
                                        name={field.name}
                                        type="number"
                                        value={field.state.value}
                                        onChange={(e) => field.handleChange(parseInt(e.target.value))}
                                        required
                                    />
                                    {field.state.meta.errors && (
                                        <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                    )}
                                </div>
                            )
                        })}
                        {form.Field({
                            name: `segments[${index}].endOffsetDays`,
                            children: (field) => (
                                <div>
                                    <div className="mb-2 block">
                                        <Label htmlFor={field.name}>終了日オフセット（日）</Label>
                                    </div>
                                    <TextInput
                                        id={field.name}
                                        name={field.name}
                                        type="number"
                                        value={field.state.value}
                                        onChange={(e) => field.handleChange(parseInt(e.target.value))}
                                        required
                                    />
                                    {field.state.meta.errors && (
                                        <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                    )}
                                </div>
                            )
                        })}
                    </div>

                    {/* ラジオキャスト選択ドロップダウン */}
                    {form.Field({
                        name: `segments[${index}].overrideRadioCasts`,
                        children: (field) => {
                            const selectedRadioCastIds = field.state.value || [];
                            const selectedRadioCasts = radioCasts?.filter(c => selectedRadioCastIds.includes(c.id!)) || [];

                            return (
                                <div ref={el => radioCastDropdownRef.current[index] = el}>
                                    <div className="mb-2 block">
                                        <Label
                                            htmlFor={`radioCasts-${index}`}>ラジオキャスト（最大2つまで選択可能）</Label>
                                    </div>
                                    <div className="relative">
                                        <Button
                                            id={`radioCasts-${index}`}
                                            color="light"
                                            onClick={() => setIsRadioCastDropdownOpen(prev => ({
                                                ...prev,
                                                [index]: !prev[index]
                                            }))}
                                            className="w-full text-left flex justify-between items-center"
                                        >
                                            <span>
                                                {selectedRadioCastIds.length === 0
                                                    ? "選択してください"
                                                    : `${selectedRadioCastIds.length}つ選択中`}
                                            </span>
                                            <svg className="w-4 h-4 ml-2" fill="currentColor" viewBox="0 0 20 20"
                                                 xmlns="http://www.w3.org/2000/svg">
                                                <path fillRule="evenodd"
                                                      d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                                                      clipRule="evenodd"></path>
                                            </svg>
                                        </Button>
                                        {isRadioCastDropdownOpen[index] && (
                                            <div
                                                className="absolute z-10 w-full bg-white rounded-lg shadow-lg mt-1 py-1 max-h-60 overflow-y-auto">
                                                {/* ラジオキャストのリスト */}
                                                {radioCasts?.map(cast => (
                                                    <div key={cast.id} className="px-4 py-2 hover:bg-gray-100">
                                                        <div className="flex items-start">
                                                            <div className="flex items-center h-5">
                                                                <Checkbox
                                                                    id={`cast-${index}-${cast.id}`}
                                                                    checked={selectedRadioCastIds.includes(cast.id!)}
                                                                    onChange={(e) => handleRadioCastChange(index, cast.id!, e.target.checked)}
                                                                />
                                                            </div>
                                                            <div className="ml-3 text-sm">
                                                                <Label htmlFor={`cast-${index}-${cast.id}`}
                                                                       className="font-medium text-gray-900">
                                                                    <div>{cast.name}</div>
                                                                    <div className="text-xs text-gray-500 mt-1">
                                                                        <div><span
                                                                            className="font-semibold">役割:</span> {cast.role === 'RADIO_PERSONALITY' ? 'ラジオパーソナリティ' : cast.role === 'ASSISTANT' ? 'アシスタント' : 'ゲスト'}
                                                                        </div>
                                                                        {cast.personality && <div><span
                                                                            className="font-semibold">性格:</span> {cast.personality}
                                                                        </div>}
                                                                        {cast.voiceName && <div><span
                                                                            className="font-semibold">ボイス名:</span> {cast.voiceName}
                                                                        </div>}
                                                                    </div>
                                                                </Label>
                                                            </div>
                                                        </div>
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                        {selectedRadioCasts.length > 0 && (
                                            <div className="flex flex-col gap-1 mt-2">
                                                {selectedRadioCasts.map(cast => (
                                                    <div key={cast.id}
                                                         className="px-4 py-2 border border-gray-200 rounded">
                                                        <div className="flex items-start">
                                                            <div className="ml-3 text-sm">
                                                                <Label htmlFor={`cast-${index}-${cast.id}`}
                                                                       className="font-medium text-gray-900">
                                                                    {cast.name}
                                                                </Label>
                                                                <div className="text-xs text-gray-500 mt-1">
                                                                    <div><span
                                                                        className="font-semibold">役割:</span> {cast.role === 'RADIO_PERSONALITY' ? 'ラジオパーソナリティ' : cast.role === 'ASSISTANT' ? 'アシスタント' : 'ゲスト'}
                                                                    </div>
                                                                    {cast.personality && <div><span
                                                                        className="font-semibold">性格:</span> {cast.personality}
                                                                    </div>}
                                                                    {cast.voiceName && <div><span
                                                                        className="font-semibold">ボイス名:</span> {cast.voiceName}
                                                                    </div>}
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                    </div>
                                </div>
                            );
                        }
                    })}
                </div>
            );
        default:
            return null;
    }
}

// Sortable segment item component
function SortableSegmentItem({id, children, segment, index, removeSegment}: {
    id: string;
    children: ReactNode,
    segment: any,
    index: number,
    removeSegment: (index: number) => void
}) {
    const {
        attributes,
        listeners,
        setNodeRef,
        transform,
        transition
    } = useSortable({id});

    const style = {
        transform: CSS.Transform.toString(transform),
        transition
    };

    // Get segment type title
    const segmentTypeTitle = 
        segment.segmentType === SegmentType.RSS ? "RSSフィード" :
        segment.segmentType === SegmentType.CALENDAR ? "カレンダー" :
        segment.segmentType === SegmentType.WEB ? "Web" :
        segment.segmentType === SegmentType.GMAIL ? "Gmail" : "";

    return (
        <Card ref={setNodeRef} className="relative" style={style}>
            <div className="absolute top-4 right-4 flex gap-2">
                <Button
                    color="light"
                    size="sm"
                    onClick={() => removeSegment(index)}
                >
                    削除
                </Button>
            </div>
            <div className="flex items-center mb-4 cursor-move">
                <div className="mr-2" {...attributes} {...listeners}>
                    <svg width="24" height="24" viewBox="0 0 24 24"
                         fill="none"
                         xmlns="http://www.w3.org/2000/svg">
                        <path d="M8 9H16M8 12H16M8 15H16"
                              stroke="currentColor"
                              strokeWidth="2" strokeLinecap="round"/>
                    </svg>
                </div>
                <h3 className="text-lg font-semibold">
                    {segmentTypeTitle} コーナー
                </h3>
            </div>
            {children}
        </Card>
    );
}


export default function CreatePage() {

    const {programId} = useParams<{ programId: string }>();
    const location = useLocation();
    const navigate = useNavigate();

    // Get program data from location state or fetch it
    const [program, setProgram] = useState<ListenerProgramSchema | null>(
        location.state?.program || null
    );

    // Fetch program data if not available in location state
    const {data: fetchedProgram} = useListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramId(
        {listenerProgramId: programId!},
        undefined,
        {enabled: !program && !!programId}
    );

    // Fetch existing segments
    const {data: existingSegments} = useListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegments(
        {programId: programId!},
        undefined,
        {enabled: !!programId}
    );

    // Fetch radio casts
    const {data: radioCasts} = useRadioCastsServiceGetApiV1RadioCasts();

    // Fetch current listener
    const {data: listener, refetch: refetchListener} = useListenersServiceGetApiV1ListenersMe();

    // Check if any segment requires Google OAuth2 authorization
    const [requiredScopes, setRequiredScopes] = useState<string[]>([]);

    // Function to check if the listener has the required scopes
    const hasRequiredScopes = useCallback(() => {
        if (!listener || !listener.scopes || !requiredScopes.length) {
            return true;
        }
        return requiredScopes.every(scope => listener.scopes?.includes(scope));
    }, [listener, requiredScopes]);

    // Function to open Google OAuth2 authorization window
    const openGoogleOAuth2 = useCallback(async () => {

        const url = await GoogleOauth2Service.getApiV1GoogleOauth2({scopes: requiredScopes});
        window.open(url, 'oauthPopup', 'width=600,height=700');
    }, [requiredScopes]);

    // ドロップダウンの表示/非表示を制御する状態
    const [isRadioCastDropdownOpen, setIsRadioCastDropdownOpen] = useState<{ [key: number]: boolean }>({});
    const radioCastDropdownRef = useRef<{ [key: number]: HTMLDivElement | null }>({});

    // Form submission state
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);

    // Update program state when fetched
    useEffect(() => {
        if (!program && fetchedProgram) {
            setProgram(fetchedProgram);
        }
    }, [program, fetchedProgram]);

    // Add message event listener for OAuth2 success
    useEffect(() => {
        const handleMessage = (event: MessageEvent) => {
            if (event.data === 'oauth2-success') {
                // Refetch listener data to get updated scopes
                refetchListener();
            }
        };

        window.addEventListener('message', handleMessage);
        return () => {
            window.removeEventListener('message', handleMessage);
        };
    }, [refetchListener]);

    // ドロップダウン外のクリックを検知して閉じる
    useEffect(() => {
        function handleClickOutside(event: MouseEvent) {
            Object.entries(radioCastDropdownRef.current).forEach(([index, ref]) => {
                if (ref && !ref.contains(event.target as Node)) {
                    setIsRadioCastDropdownOpen(prev => ({
                        ...prev,
                        [index]: false
                    }));
                }
            });
        }

        document.addEventListener("mousedown", handleClickOutside);
        return () => {
            document.removeEventListener("mousedown", handleClickOutside);
        };
    }, []);

    // Initialize form with existing segments or empty array
    const [formValues, setFormValues] = useState<FormValues>({
        segments: []
    });

    // Update form values when existing segments are fetched
    useEffect(() => {
        if (existingSegments && existingSegments.length > 0) {
            // Map existing segments to form values
            const segments = existingSegments.map(segment => {
                const baseSegment = {
                    id: segment.id,
                    title: segment.title,
                    description: segment.description || "",
                    constraints: segment.constraints || "",
                    order: segment.order,
                    overrideRadioCasts: segment.overrideRadioCasts || [],
                    segmentType: segment.segmentType!
                };

                // Add type-specific fields
                switch (segment.segmentType) {
                    case SegmentType.RSS:
                        return {
                            ...baseSegment,
                            feedUrl: (segment as any).feedUrl
                        };
                    case SegmentType.CALENDAR:
                        return {
                            ...baseSegment,
                            startOffsetDays: (segment as any).startOffsetDays,
                            endOffsetDays: (segment as any).endOffsetDays,
                            calendarId: (segment as any).calendarId
                        };
                    case SegmentType.WEB:
                        return {
                            ...baseSegment,
                            urls: (segment as any).urls || [""]
                        };
                    case SegmentType.GMAIL:
                        return {
                            ...baseSegment,
                            filter: (segment as any).filter,
                            startOffsetDays: (segment as any).startOffsetDays,
                            endOffsetDays: (segment as any).endOffsetDays
                        };
                    default:
                        return baseSegment;
                }
            });

            setFormValues({segments} as FormValues);
        }
    }, [existingSegments]);

    // Update required scopes when form values change
    useEffect(() => {
        const scopes = new Set<string>();

        // Check each segment for required scopes
        formValues.segments.forEach(segment => {
            const requiredScope = getRequiredScopeForSegmentType(segment.segmentType);
            if (requiredScope) {
                scopes.add(requiredScope);
            }
        });

        setRequiredScopes(Array.from(scopes));
    }, [formValues.segments]);

    // Initialize TanStack Form
    const form = useForm({
        defaultValues: formValues,
        onSubmit: async ({value}) => {
            try {
                setIsSubmitting(true);
                setErrorMessage(null);

                // Map form values to API request format
                const segments = value.segments.map((segment, index) => {
                    const baseSegment = {
                        id: segment.id,
                        title: segment.title,
                        description: segment.description,
                        constraints: segment.constraints,
                        order: index, // Use index as order to ensure correct ordering
                        overrideRadioCasts: segment.overrideRadioCasts,
                        segmentType: segment.segmentType
                    };

                    // Add type-specific fields
                    switch (segment.segmentType) {
                        case SegmentType.RSS:
                            return {
                                ...baseSegment,
                                feedUrl: (segment as any).feedUrl
                            } as ListenerProgramRSSSegmentUpdate;
                        case SegmentType.CALENDAR:
                            return {
                                ...baseSegment,
                                startOffsetDays: (segment as any).startOffsetDays,
                                endOffsetDays: (segment as any).endOffsetDays,
                                calendarId: (segment as any).calendarId
                            } as ListenerProgramCalendarSegmentUpdate;
                        case SegmentType.WEB:
                            return {
                                ...baseSegment,
                                urls: (segment as any).urls
                            } as ListenerProgramWebSegmentUpdate;
                        case SegmentType.GMAIL:
                            return {
                                ...baseSegment,
                                filter: (segment as any).filter,
                                startOffsetDays: (segment as any).startOffsetDays,
                                endOffsetDays: (segment as any).endOffsetDays
                            } as ListenerProgramGmailSegmentUpdate;
                        default:
                            return baseSegment;
                    }
                });

                // Submit segments to API
                await ListenerProgramSegmentsService.putApiV1ListenerProgramsByProgramIdSegments({
                    programId: programId!,
                    requestBody: segments
                });

                // Navigate back to program list
                navigate("/listener-programs");
            } catch (error) {
                console.error("Error saving segments:", error);
                setErrorMessage("コーナーの保存に失敗しました。もう一度お試しください。");
            } finally {
                setIsSubmitting(false);
            }
        }
    });


    // Update form when formValues change
    useEffect(() => {
        // 初期ロード時または既存のセグメントデータをロードしたときのみ完全にリセット
        const isInitialLoad = formValues.segments.some(segment => 
            segment.id && !form.getFieldValue(`segments[0].id`)
        );

        // フォームのセグメント数とformValuesのセグメント数を比較
        const formSegmentsCount = form.getFieldValue('segments')?.length || 0;
        const hasSegmentCountChanged = formSegmentsCount !== formValues.segments.length;

        if (isInitialLoad) {
            // 初期ロード時は完全にリセット
            form.reset(formValues);
        } else if (hasSegmentCountChanged) {
            if (formSegmentsCount < formValues.segments.length) {
                // セグメントが追加された場合は、新しいセグメントのみを追加（既存の入力値は保持）
                const newSegmentIndex = formValues.segments.length - 1;
                const newSegment = formValues.segments[newSegmentIndex];

                // 新しいセグメントのフィールドを設定
                form.setFieldValue(`segments[${newSegmentIndex}]`, newSegment);
            } else {
                // セグメントが削除された場合は、フォームの状態を更新
                form.setFieldValue('segments', formValues.segments);
            }
        }
    }, [formValues]);

    // Add a new segment
    const addSegment = (type: SegmentType) => {
        // Check if maximum number of segments (5) is reached
        if (formValues.segments.length >= 5) {
            return;
        }

        const newSegment = {
            ...defaultSegmentValues[type],
            order: formValues.segments.length
        };

        console.log("newSegment", newSegment)

        setFormValues({
            segments: [...formValues.segments, newSegment]
        });
    };

    // Remove a segment
    const removeSegment = (index: number) => {
        const newSegments = [...formValues.segments];
        newSegments.splice(index, 1);

        // Update order of remaining segments
        newSegments.forEach((segment, i) => {
            segment.order = i;
        });

        setFormValues({segments: newSegments});
    };

    // ラジオキャスト選択の変更ハンドラー
    const handleRadioCastChange = (segmentIndex: number, radioCastId: string, checked: boolean) => {
        const newSegments = [...formValues.segments];
        const segment = newSegments[segmentIndex];

        if (!segment.overrideRadioCasts) {
            segment.overrideRadioCasts = [];
        }

        if (checked) {
            // 選択する場合、最大2つまでの制限を適用
            if (segment.overrideRadioCasts.length < 2) {
                segment.overrideRadioCasts.push(radioCastId);
            } else {
                // すでに2つ選択されている場合は、最初の選択を削除して新しい選択を追加
                segment.overrideRadioCasts = [...segment.overrideRadioCasts.slice(1), radioCastId];
            }
        } else {
            // 選択解除する場合
            segment.overrideRadioCasts = segment.overrideRadioCasts.filter(id => id !== radioCastId);
        }

        setFormValues({segments: newSegments});
    };

    // DnD sensors
    const sensors = useSensors(
        useSensor(PointerSensor),
        useSensor(KeyboardSensor, {
            coordinateGetter: sortableKeyboardCoordinates,
        })
    );

    // Handle drag end
    const handleDragEnd = (event: DragEndEvent) => {
        const {active, over} = event;

        if (over && active.id !== over.id) {
            const oldIndex = formValues.segments.findIndex(s => `segment-${s.order}` === active.id);
            const newIndex = formValues.segments.findIndex(s => `segment-${s.order}` === over.id);

            if (oldIndex !== -1 && newIndex !== -1) {
                const newSegments = arrayMove(formValues.segments, oldIndex, newIndex);

                // Update order of segments
                newSegments.forEach((segment, i) => {
                    segment.order = i;
                });

                setFormValues({segments: newSegments});
            }
        }
    };

    return (
        <div className="mx-auto px-4 py-8">
            <header className="mb-8">
                <h1 className="text-3xl font-bold mb-2">リスナープログラムコーナー設定</h1>
                {program && (
                    <p className="text-gray-600">
                        プログラム: {program.title}
                    </p>
                )}
            </header>

            <div className="mb-6">
                <div className="flex items-center justify-between mb-4">
                    <h2 className="text-xl font-semibold">コーナー</h2>
                    <div className="flex gap-2">
                        <Select
                            disabled={formValues.segments.length >= 5}
                            onChange={(e) => {
                                if (e.target.value) {
                                    addSegment(e.target.value as SegmentType);
                                    e.target.value = "";
                                }
                            }}
                        >
                            <option value="">
                                {formValues.segments.length >= 5 
                                    ? "コーナー数が上限に達しました（最大5つ）" 
                                    : "コーナーを追加..."}
                            </option>
                            <option value={SegmentType.RSS}>RSSフィード</option>
                            <option value={SegmentType.CALENDAR}>カレンダー</option>
                            <option value={SegmentType.WEB}>Web</option>
                            <option value={SegmentType.GMAIL}>Gmail</option>
                        </Select>
                    </div>
                </div>

                <form
                    onSubmit={(e) => {
                        e.preventDefault();
                        e.stopPropagation();
                        form.handleSubmit();
                    }}
                >
                    <form.Field name="segments" mode="array">
                        {(f) => (
                            <DndContext
                                sensors={sensors}
                                collisionDetection={closestCenter}
                                onDragEnd={handleDragEnd}
                            >
                                <SortableContext
                                    items={f.state.value.map(s => `segment-${s.order}`)}
                                    strategy={verticalListSortingStrategy}
                                >
                                    <div className="space-y-4">
                                        {f.state.value.map((segment, index) => (
                                            <SortableSegmentItem key={`segment-${index}`}
                                                                 id={`segment-${index}`}
                                                                 segment={segment}
                                                                 index={index}
                                                                 removeSegment={removeSegment}
                                            >
                                                <div className="space-y-4">
                                                    {form.Field({
                                                        name: `segments[${index}].title`,
                                                        children: (field) => (
                                                            <div>
                                                                <div className="mb-2 block">
                                                                    <Label htmlFor={field.name}>タイトル</Label>
                                                                </div>
                                                                <TextInput
                                                                    id={field.name}
                                                                    name={field.name}
                                                                    placeholder="コーナーのタイトル"
                                                                    value={field.state.value}
                                                                    onBlur={field.handleBlur}
                                                                    onChange={(e) => field.handleChange(e.target.value)}
                                                                    required
                                                                />
                                                                {field.state.meta.errors && (
                                                                    <div
                                                                        className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                                                )}
                                                            </div>
                                                        )
                                                    })}

                                                    {form.Field({
                                                        name: `segments[${index}].description`,
                                                        children: (field) => (
                                                            <div>
                                                                <div className="mb-2 block">
                                                                    <Label htmlFor={field.name}>説明</Label>
                                                                </div>
                                                                <Textarea
                                                                    id={field.name}
                                                                    name={field.name}
                                                                    placeholder="コーナーの説明"
                                                                    value={field.state.value || ""}
                                                                    onChange={(e) => field.handleChange(e.target.value)}
                                                                    rows={2}
                                                                />
                                                                {field.state.meta.errors && (
                                                                    <div
                                                                        className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                                                )}
                                                            </div>
                                                        )
                                                    })}

                                                    {form.Field({
                                                        name: `segments[${index}].constraints`,
                                                        children: (field) => (
                                                            <div>
                                                                <div className="mb-2 block">
                                                                    <Label htmlFor={field.name}>制約条件</Label>
                                                                </div>
                                                                <Textarea
                                                                    id={field.name}
                                                                    name={field.name}
                                                                    placeholder="コーナーの制約条件"
                                                                    value={field.state.value || ""}
                                                                    onChange={(e) => field.handleChange(e.target.value)}
                                                                    rows={2}
                                                                />
                                                                {field.state.meta.errors && (
                                                                    <div
                                                                        className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                                                )}
                                                            </div>
                                                        )
                                                    })}

                                                    {/* Segment type specific fields */}
                                                    <SegmentForm
                                                        segmentType={segment.segmentType}
                                                        index={index}
                                                        form={form}
                                                        radioCasts={radioCasts}
                                                        handleRadioCastChange={handleRadioCastChange}
                                                        isRadioCastDropdownOpen={isRadioCastDropdownOpen}
                                                        setIsRadioCastDropdownOpen={setIsRadioCastDropdownOpen}
                                                        radioCastDropdownRef={radioCastDropdownRef}
                                                    />
                                                </div>
                                            </SortableSegmentItem>
                                        ))}
                                    </div>
                                </SortableContext>
                            </DndContext>)
                        }
                    </form.Field>
                    {formValues.segments.length === 0 && (
                        <Card>
                            <div className="text-center py-8">
                                <p className="text-gray-500 mb-4">コーナーがありません。コーナーを追加してください。</p>
                                <Select
                                    className="max-w-xs mx-auto"
                                    disabled={formValues.segments.length >= 5}
                                    onChange={(e) => {
                                        if (e.target.value) {
                                            addSegment(e.target.value as SegmentType);
                                            e.target.value = "";
                                        }
                                    }}
                                >
                                    <option value="">
                                        {formValues.segments.length >= 5 
                                            ? "コーナー数が上限に達しました（最大5つ）" 
                                            : "コーナーを追加..."}
                                    </option>
                                    <option value={SegmentType.RSS}>RSSフィード</option>
                                    <option value={SegmentType.CALENDAR}>カレンダー</option>
                                    <option value={SegmentType.WEB}>Web</option>
                                    <option value={SegmentType.GMAIL}>Gmail</option>
                                </Select>
                            </div>
                        </Card>
                    )}

                    {errorMessage && (
                        <div className="text-red-500 mt-4">{errorMessage}</div>
                    )}

                    <div className="flex justify-end mt-6">
                        <Button
                            color="light"
                            className="mr-2"
                            onClick={() => navigate("/listener-programs")}
                        >
                            キャンセル
                        </Button>
                        {requiredScopes.length > 0 && !hasRequiredScopes() ? (
                            <>
                                <Button
                                    color="blue"
                                    className="mr-2"
                                    onClick={openGoogleOAuth2}
                                >
                                    Google API認可
                                </Button>
                                <Button
                                    type="submit"
                                    disabled={true}
                                >
                                    保存
                                </Button>
                            </>
                        ) : (
                            <Button
                                type="submit"
                                disabled={isSubmitting || formValues.segments.length === 0}
                            >
                                {isSubmitting ? "保存中..." : "保存"}
                            </Button>
                        )}
                    </div>
                </form>
            </div>
        </div>
    );
}

export function meta() {
    return [
        {title: "リスナープログラムコーナー設定 - Personalized Podcast Platform"},
        {name: "description", content: "リスナープログラムのコーナーを設定します"},
    ];
}
