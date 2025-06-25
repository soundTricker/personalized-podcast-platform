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

import {Button, Card, Checkbox, Label, Select, Textarea, TextInput, HelperText, FileInput} from "flowbite-react";
import {
    useListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramId,
    useRadioCastsServiceGetApiV1RadioCasts,
    useRadioCastsServicePostApiV1RadioCasts
} from "@api/queries";
import {
    prefetchUseListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramId,
    prefetchUseRadioCastsServiceGetApiV1RadioCasts
} from "@api/queries/prefetch";
import {useEffect, useRef, useState} from "react";
import {BroadcastSchedule, ProgramStatus, PublishSetting, RadioCastCreateSchema, RadioCastRole} from "@api/requests/types.gen";
import {ListenerProgramsService} from "@api/requests/services.gen";
import {RadioCastCreateModal} from "@/components/RadioCastCreateModal";
import {useForm} from "@tanstack/react-form";
import {z} from "zod";
import {Route} from './+types/edit';
import {dehydrate, QueryClient} from "@tanstack/react-query";
import {useNavigate, useParams} from "react-router";
import { getStorage, ref, uploadBytes } from 'firebase/storage';
import { initializeApp } from 'firebase/app';
import { firebaseConfig } from '@/firebase/config';
import { useAuth } from '@/firebase/auth';
import FBImage from '@/components/FBImage';
import HelpIcon from "@/components/HelpIcon.tsx";

// フォームのスキーマ定義
const formSchema = z.object({
    title: z.string().min(1, "タイトルは必須です"),
    description: z.string().min(1, "説明は必須です"),
    programMinutes: z.number().int().min(5).max(15),
    insertMusic: z.boolean(),
    baseRadioCastIds: z.array(z.string()).min(1, "メインキャストを選択してください"),
    broadcastSchedule: z.enum([BroadcastSchedule.DAILY, BroadcastSchedule.WEEKLY]),
    broadcastDayofweek: z.array(z.string()),
    publishSetting: z.enum([PublishSetting.PRIVATE, PublishSetting.LIMITED, PublishSetting.PUBLISH]),
    privateKey: z.string().optional(),
    coverArtUri: z.string().optional()
});

type FormValues = z.infer<typeof formSchema>;

// Initialize Firebase app for storage
const app = initializeApp(firebaseConfig);
const storage = getStorage(app);

export async function loader({params}: Route.LoaderArgs) {
    const queryClient = new QueryClient();

    await prefetchUseRadioCastsServiceGetApiV1RadioCasts(queryClient);
    await prefetchUseListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramId(queryClient, {listenerProgramId: params.programId});

    return {dehydratedState: dehydrate(queryClient)};
}

export default function EditPage() {
    const {programId} = useParams<{ programId: string }>();

    // フォーム送信中の状態管理
    const [isSubmitting, setIsSubmitting] = useState(false);
    // エラーメッセージの状態管理
    const [errorMessage, setErrorMessage] = useState<string | null>(null);

    // 画像アップロード関連の状態管理
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [isUploading, setIsUploading] = useState(false);
    const [uploadError, setUploadError] = useState<string | null>(null);

    // ラジオキャストの取得
    const {data: radioCasts, refetch: refetchRadioCasts} = useRadioCastsServiceGetApiV1RadioCasts();

    // 認証情報の取得
    const { currentUser } = useAuth();

    // リスナープログラムの取得
    const {data: listenerProgram, isLoading} = useListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramId({
        listenerProgramId: programId!
    });

    // モーダルの表示/非表示を制御する状態
    const [showModal, setShowModal] = useState(false);

    // dayOfWeekの表示/非表示
    const [showDayOfWeek, setShowDayOfWeek] = useState(false);

    // privateKeyの表示/非表示
    const [showPrivateKey, setShowPrivateKey] = useState(false);

    // 曜日の選択肢
    const daysOfWeek = [
        {id: "monday", name: "月曜日"},
        {id: "tuesday", name: "火曜日"},
        {id: "wednesday", name: "水曜日"},
        {id: "thursday", name: "木曜日"},
        {id: "friday", name: "金曜日"},
        {id: "saturday", name: "土曜日"},
        {id: "sunday", name: "日曜日"}
    ];

    const navigate = useNavigate();

    // ランダム文字列生成機能
    const generateRandomString = (length: number = 32): string => {
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        let result = '';
        for (let i = 0; i < length; i++) {
            result += chars.charAt(Math.floor(Math.random() * chars.length));
        }
        return result;
    };

    // 画像アップロード機能
    const handleImageUpload = async () => {
        if (!selectedFile || !currentUser) {
            return;
        }

        try {
            setIsUploading(true);
            setUploadError(null);

            // Generate random filename with extension
            const fileExtension = selectedFile.name.split('.').pop();
            const randomString = generateRandomString(16);
            const fileName = `${randomString}.${fileExtension}`;
            const filePath = `listener/${currentUser.uid}/${fileName}`;

            // Create storage reference
            const storageRef = ref(storage, filePath);

            // Upload file
            await uploadBytes(storageRef, selectedFile);

            // Create GCS URI
            const gcsUri = `gs://${firebaseConfig.storageBucket}/${filePath}`;

            // Update form with the GCS URI
            form.setFieldValue('coverArtUri', gcsUri);

            // Clear selected file
            setSelectedFile(null);
        } catch (error) {
            console.error('Error uploading image:', error);
            setUploadError('画像のアップロードに失敗しました。もう一度お試しください。');
        } finally {
            setIsUploading(false);
        }
    };

    // TanStack Formの初期化
    const form = useForm({
        defaultValues: {
            title: listenerProgram?.title || "",
            description: listenerProgram?.description || "",
            programMinutes: listenerProgram?.programMinutes || 10,
            insertMusic: listenerProgram?.insertMusic || true,
            baseRadioCastIds: listenerProgram?.baseRadioCastIds || [],
            broadcastSchedule: listenerProgram?.broadcastSchedule || BroadcastSchedule.DAILY,
            broadcastDayofweek: listenerProgram?.broadcastDayofweek || [],
            publishSetting: listenerProgram?.publishSetting || PublishSetting.PRIVATE,
            privateKey: listenerProgram?.privateKey || "",
            coverArtUri: listenerProgram?.coverArtUri || ""
        } as FormValues,
        onSubmit: async ({value}) => {
            try {
                setIsSubmitting(true);
                setErrorMessage(null);

                // APIクライアントを使用してリスナープログラムを更新
                const program = await ListenerProgramsService.putApiV1ListenerProgramsByListenerProgramId({
                    listenerProgramId: programId!,
                    requestBody: {
                        ...value,
                        status: listenerProgram?.status || ProgramStatus.DRAFT,
                        cover_art_uri: value.coverArtUri || null
                    }
                });

                // 成功したら詳細ページへ遷移
                navigate(`/listener-programs/${program.id!}`, {state: {program}});
            } catch (error) {
                console.error("Error updating listener program:", error);
                setErrorMessage("プログラムの更新に失敗しました。もう一度お試しください。");
            } finally {
                setIsSubmitting(false);
            }
        }
    });

    // リスナープログラムデータが取得できたらフォームに設定
    useEffect(() => {
        if (listenerProgram) {
            form.reset({
                title: listenerProgram.title || "",
                description: listenerProgram.description || "",
                programMinutes: listenerProgram.programMinutes || 10,
                insertMusic: listenerProgram.insertMusic || true,
                baseRadioCastIds: listenerProgram.baseRadioCastIds || [],
                broadcastSchedule: listenerProgram.broadcastSchedule || BroadcastSchedule.DAILY,
                broadcastDayofweek: listenerProgram.broadcastDayofweek || [],
                publishSetting: listenerProgram.publishSetting || PublishSetting.PRIVATE,
                privateKey: listenerProgram.privateKey || "",
                coverArtUri: listenerProgram.coverArtUri || ""
            }, {keepDefaultValues: false});

            // 週次配信の場合は曜日選択を表示
            setShowDayOfWeek(listenerProgram.broadcastSchedule === BroadcastSchedule.WEEKLY);

            // 限定公開の場合はプライベートキーを表示
            setShowPrivateKey(listenerProgram.publishSetting === PublishSetting.LIMITED);

            // 選択されているラジオキャストを設定
            if (listenerProgram.baseRadioCastIds) {
                setSelectedRadioCastIds(listenerProgram.baseRadioCastIds);
            }
        }
    }, [listenerProgram]);

    // ラジオキャスト作成のミューテーション
    const radioCastMutation = useRadioCastsServicePostApiV1RadioCasts({
        onSuccess: () => {
            // 成功時にモーダルを閉じてラジオキャストリストを再取得
            setShowModal(false);
            refetchRadioCasts();
        }
    });

    // 選択されたラジオキャストの状態管理
    const [selectedRadioCastIds, setSelectedRadioCastIds] = useState<string[]>([]);

    const selectedRadioCasts = radioCasts?.filter(c => selectedRadioCastIds.includes(c.id!)) || [];

    // フォームの値が変更されたときにselectedRadioCastIdsを更新
    useEffect(() => {
        if (form.state.values.baseRadioCastIds) {
            setSelectedRadioCastIds(form.state.values.baseRadioCastIds);
        }
    }, [form.state.values.baseRadioCastIds]);

    // ラジオキャスト選択の変更ハンドラー
    const handleRadioCastChange = (id: string, checked: boolean) => {
        // 「新規作成」が選択された場合
        if (id === 'create_new') {
            setShowModal(true);
            return;
        }

        let newSelected: string[];

        if (checked) {
            // 選択する場合、最大2つまでの制限を適用
            if (selectedRadioCastIds.length < 2) {
                newSelected = [...selectedRadioCastIds, id];
            } else {
                // すでに2つ選択されている場合は、最初の選択を削除して新しい選択を追加
                newSelected = [...selectedRadioCastIds.slice(1), id];
            }
        } else {
            // 選択解除する場合
            newSelected = selectedRadioCastIds.filter(castId => castId !== id);
        }

        setSelectedRadioCastIds(newSelected);
        form.setFieldValue("baseRadioCastIds", newSelected);
    };

    // ドロップダウンの表示/非表示を制御する状態
    const [isDropdownOpen, setIsDropdownOpen] = useState(false);
    const dropdownRef = useRef<HTMLDivElement>(null);

    // ドロップダウン外のクリックを検知して閉じる
    useEffect(() => {
        function handleClickOutside(event: MouseEvent) {
            if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
                setIsDropdownOpen(false);
            }
        }

        document.addEventListener("mousedown", handleClickOutside);
        return () => {
            document.removeEventListener("mousedown", handleClickOutside);
        };
    }, []);

    // ラジオキャスト作成の送信ハンドラー
    const handleCreateRadioCast = (radioCast: RadioCastCreateSchema) => {
        radioCastMutation.mutate({
            requestBody: radioCast
        });
    };

    if (isLoading) {
        return (
            <div className="mx-auto px-4 py-8 text-center">
                <p>読み込み中...</p>
            </div>
        );
    }

    return (
        <div className="mx-auto px-4 py-8">
            <header className="mb-8 text-center">
                <h1 className="text-3xl font-bold mb-2">リスナープログラム編集</h1>
                <p className="text-gray-600">ポッドキャストプログラムを編集しましょう</p>
            </header>

            <Card className="max-w-2xl mx-auto">
                <form
                    className="space-y-4"
                    onSubmit={(e) => {
                        e.preventDefault();
                        e.stopPropagation();
                        form.handleSubmit();
                    }}
                >
                    {form.Field({
                        name: "title",
                        children: (field) => (
                            <div>
                                <div className="mb-2 block">
                                    <Label htmlFor={field.name}>タイトル</Label>
                                </div>
                                <TextInput
                                    id={field.name}
                                    name={field.name}
                                    placeholder="プログラムのタイトルを入力"
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

                    {form.Field({
                        name: "description",
                        children: (field) => (
                            <div>
                                <div className="mb-2 block">
                                    <Label htmlFor={field.name}>説明</Label>
                                </div>
                                <Textarea
                                    id={field.name}
                                    name={field.name}
                                    placeholder="プログラムの説明を入力"
                                    value={field.state.value}
                                    onChange={(e) => field.handleChange(e.target.value)}
                                    required
                                    rows={4}
                                />
                                {field.state.meta.errors && (
                                    <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                )}
                            </div>
                        )
                    })}

                    {form.Field({
                        name: "programMinutes",
                        children: (field) => (
                            <div>
                                <div className="mb-2 block">
                                    <Label htmlFor={field.name}>プログラム時間(目安)（分）</Label>
                                </div>
                                <Select
                                    id={field.name}
                                    name={field.name}
                                    value={field.state.value.toString()}
                                    onChange={(e) => field.handleChange(parseInt(e.target.value))}
                                    required
                                >
                                    <option value="5">5分</option>
                                    <option value="10">10分</option>
                                    <option value="15">15分</option>
                                </Select>
                                {field.state.meta.errors && (
                                    <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                )}
                            </div>
                        )
                    })}
                    {form.Field({
                        name: "baseRadioCastIds",
                        children: (field) => (
                            <div ref={dropdownRef}>
                                <div className="mb-2 block">
                                    <Label htmlFor="baseRadioCastIds">メインキャスト（最大2つまで選択可能）</Label>
                                </div>
                                <div className="relative">
                                    <Button
                                        id="baseRadioCastIds"
                                        color="light"
                                        onClick={() => setIsDropdownOpen(!isDropdownOpen)}
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
                                    {isDropdownOpen && (
                                        <div
                                            className="absolute z-10 w-full bg-white rounded-lg shadow-lg mt-1 py-1 max-h-60 overflow-y-auto">
                                            {/* 新規作成オプション */}
                                            <div
                                                className="px-4 py-2 hover:bg-gray-100 cursor-pointer border-b border-gray-200 text-blue-600 font-medium"
                                                onClick={() => {
                                                    setIsDropdownOpen(false);
                                                    setShowModal(true);
                                                }}
                                            >
                                                + 新規作成
                                            </div>

                                            {/* ラジオキャストのリスト */}
                                            {radioCasts?.map(cast => (
                                                <div key={cast.id} className="px-4 py-2 hover:bg-gray-100">
                                                    <div className="flex items-start">
                                                        <div className="flex items-center h-5">
                                                            <Checkbox
                                                                id={`cast-${cast.id}`}
                                                                checked={selectedRadioCastIds.includes(cast.id!)}
                                                                onChange={(e) => handleRadioCastChange(cast.id!, e.target.checked)}
                                                            />
                                                        </div>
                                                        <div className="ml-3 text-sm">
                                                            <Label htmlFor={`cast-${cast.id}`}
                                                                   className="font-medium text-gray-900">
                                                                <div>{cast.name}</div>
                                                                <div className="text-xs text-gray-500 mt-1">
                                                                    <div><span
                                                                        className="font-semibold">役割:</span> {cast.role === RadioCastRole.RADIO_PERSONALITY ? 'ラジオパーソナリティ' : cast.role === RadioCastRole.ASSISTANT ? 'アシスタント' : 'ゲスト'}
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
                                    {selectedRadioCasts.length > 0
                                        &&
                                        <div className="flex flex-col gap-1">
                                            {selectedRadioCasts.map(cast =>
                                                <div key={cast.id} className="px-4 py-2 ">
                                                    <div className="flex items-start">
                                                        <div className="ml-3 text-sm">
                                                            <Label htmlFor={`cast-${cast.id}`}
                                                                   className="font-medium text-gray-900">
                                                                {cast.name}
                                                            </Label>
                                                            <div className="text-xs text-gray-500 mt-1">
                                                                <div><span
                                                                    className="font-semibold">役割:</span> {cast.role === RadioCastRole.RADIO_PERSONALITY ? 'ラジオパーソナリティ' : cast.role === RadioCastRole.ASSISTANT ? 'アシスタント' : 'ゲスト'}
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
                                                </div>)}
                                        </div>
                                    }

                                </div>
                                {field.state.meta.errors && (
                                    <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                )}
                            </div>
                        )
                    })}

                    {form.Field({
                        name: "insertMusic",
                        children: (field) => (
                            <div className="flex items-center gap-2">
                                <Checkbox
                                    id={field.name}
                                    name={field.name}
                                    checked={field.state.value}
                                    onChange={(e) => field.handleChange(e.target.checked)}
                                />
                                <Label htmlFor={field.name}>音楽を挿入する</Label>
                            </div>
                        )
                    })}

                    {form.Field({
                        name: "broadcastSchedule",
                        children: (field) => (
                            <div>
                                <div className="mb-2 block">
                                    <Label htmlFor={field.name}>配信スケジュール</Label>
                                </div>
                                <Select
                                    id={field.name}
                                    name={field.name}
                                    value={field.state.value}
                                    onChange={(e) => {
                                        field.handleChange(e.target.value as BroadcastSchedule);
                                        setShowDayOfWeek(e.target.value === BroadcastSchedule.WEEKLY);
                                    }}
                                    required
                                >
                                    <option value={BroadcastSchedule.DAILY}>毎日</option>
                                    <option value={BroadcastSchedule.WEEKLY}>毎週</option>
                                </Select>
                                {field.state.meta.errors && (
                                    <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                )}
                            </div>
                        )
                    })}
                    {form.Field({
                        name: "broadcastDayofweek",
                        children: (field) => (
                            <div className={showDayOfWeek ? "" : "hidden"}>
                                <div className="mb-2 block">
                                    <Label htmlFor={field.name}>配信曜日</Label>
                                </div>
                                <div className="grid grid-cols-2 gap-2">
                                    {daysOfWeek.map(day => (
                                        <div key={day.id} className="flex items-center gap-2">
                                            <Checkbox
                                                id={`day-${day.id}`}
                                                checked={field.state.value.includes(day.id)}
                                                onChange={(e) => {
                                                    const newValue = [...field.state.value];
                                                    if (e.target.checked) {
                                                        if (!newValue.includes(day.id)) {
                                                            newValue.push(day.id);
                                                        }
                                                    } else {
                                                        const index = newValue.indexOf(day.id);
                                                        if (index !== -1) {
                                                            newValue.splice(index, 1);
                                                        }
                                                    }
                                                    field.handleChange(newValue);
                                                }}
                                            />
                                            <Label htmlFor={`day-${day.id}`}>{day.name}</Label>
                                        </div>
                                    ))}
                                </div>
                                {field.state.meta.errors && (
                                    <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                )}
                            </div>
                        )
                    })}

                    {form.Field({
                        name: "publishSetting",
                        children: (field) => (
                            <div>
                                <div className="mb-2 block">
                                    <Label htmlFor={field.name}>公開設定</Label>
                                </div>
                                <Select
                                    id={field.name}
                                    name={field.name}
                                    value={field.state.value}
                                    onChange={(e) => field.handleChange(e.target.value as PublishSetting)}
                                    required
                                >
                                    <option value={PublishSetting.PRIVATE}>非公開</option>
                                    <option value={PublishSetting.LIMITED}>限定公開</option>
                                    <option value={PublishSetting.PUBLISH}>公開</option>
                                </Select>
                                {field.state.meta.errors && (
                                    <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                                )}
                            </div>
                        )
                    })}

                    {/* カバー画像アップロード */}
                    <div>
                        <div className="mb-2 block">
                            <Label htmlFor="coverImage">
                                <div className="flex flex-row items-center gap-1">
                                    <span>カバー画像</span>
                                    <HelpIcon>
                                        ポッドキャストのカバー画像をアップロードできます。<br/>
                                        JPEGまたはPNG形式の画像ファイルを選択してください。
                                    </HelpIcon>
                                </div>
                            </Label>
                        </div>

                        {/* 現在のカバー画像表示 */}
                        {form.state.values.coverArtUri && (
                            <div className="mb-4">
                                <p className="text-sm text-gray-600 mb-2">現在のカバー画像:</p>
                                <FBImage 
                                    path={form.state.values.coverArtUri.replace('gs://' + firebaseConfig.storageBucket + '/', '')}
                                    alt="カバー画像"
                                    className="w-32 h-32 object-cover rounded-lg border"
                                />
                            </div>
                        )}

                        <div className="flex gap-2 items-end">
                            <div className="flex-1">
                                <FileInput
                                    id="coverImage"
                                    accept="image/jpeg,image/png,image/jpg"
                                    onChange={(e) => {
                                        const file = e.target.files?.[0];
                                        setSelectedFile(file || null);
                                        setUploadError(null);
                                    }}
                                />
                            </div>
                            <Button
                                type="button"
                                color="light"
                                onClick={handleImageUpload}
                                disabled={!selectedFile || isUploading || !currentUser}
                            >
                                {isUploading ? "アップロード中..." : "アップロード"}
                            </Button>
                        </div>

                        {uploadError && (
                            <div className="text-red-500 text-sm mt-1">{uploadError}</div>
                        )}

                        <HelperText className="mt-1">
                            画像ファイルを選択してアップロードボタンをクリックしてください。
                        </HelperText>
                    </div>

                    {errorMessage && (
                        <div className="text-red-500">{errorMessage}</div>
                    )}

                    <div></div>
                    <div className="flex items-end justify-end gap-2">
                        <Button color="light" onClick={() => navigate(`/listener-programs/${programId!}`)}>
                            キャンセル
                        </Button>
                        <Button type="submit" disabled={isSubmitting || selectedRadioCastIds.length === 0}>
                            {isSubmitting ? "更新中..." : "プログラムを更新"}
                        </Button>
                    </div>
                </form>
            </Card>

            {/* ラジオキャスト作成用モーダル */}
            <RadioCastCreateModal
                show={showModal}
                onClose={() => setShowModal(false)}
                onCreateRadioCast={handleCreateRadioCast}
                isCreating={radioCastMutation.isPending}
            />
        </div>
    );
}

export function meta() {
    return [
        {title: "リスナープログラム編集 - Personalized Podcast Platform"},
        {name: "description", content: "あなたのポッドキャストプログラムを編集"},
    ];
}
