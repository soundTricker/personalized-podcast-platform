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

import {Link, useNavigate, useParams} from "react-router";
import {
    Alert,
    Badge,
    Button,
    Card,
    Modal,
    ModalBody,
    ModalHeader, Popover,
    Spinner,
    TabItem,
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeadCell,
    TableRow,
    Tabs,
    TabsRef,
    Toast,
    ToastToggle,
    ClipboardWithIconText
} from "flowbite-react";
import {
    HiCheckCircle,
    HiEnvelopeOpen,
    HiMagnifyingGlass,
    HiMicrophone,
    HiMiniListBullet,
    HiMiniMegaphone,
    HiMiniPencilSquare,
    HiMiniPlay,
    HiMiniWrenchScrewdriver,
    HiOutlineAdjustmentsVertical,
    HiOutlineArrowPath,
    HiOutlineChatBubbleLeftEllipsis,
    HiOutlineChatBubbleLeftRight,
    HiOutlineClipboard,
    HiOutlineExclamationCircle,
    HiOutlineMusicalNote,
    HiOutlineRadio,
    HiOutlineRocketLaunch,
    HiOutlineSignal,
    HiOutlineSparkles
} from 'react-icons/hi2';
import {
    useListenerProgramsServiceGetApiV1ListenerPrograms,
    useListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegments,
    useListenerProgramsServiceDeleteApiV1ListenerProgramsByListenerProgramId,
    useListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramId,
    useListenerProgramsServicePutApiV1ListenerProgramsByListenerProgramId,
    useProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistory,
    useRadioCastsServiceGetApiV1RadioCasts,
    UseRadioCastsServiceGetApiV1RadioCastsKeyFn
} from "@api/queries";
import {
    BroadcastSchedule,
    OpenAPI,
    ProgramBroadcastHistorySchema,
    ProgramBroadcastHistoryService,
    ProgramBroadcastHistoryStatus,
    ProgramStatus,
    PublishSetting,
    RadioCastSchema
} from "@api/requests";
import {useReducer, useRef, useState} from "react";
import {useAuth} from '@/firebase/auth';
import {IconType} from "react-icons";
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import ProgramStatusBadge from "@/components/ProgramStatusBadge.tsx";
import FBImage from '@/components/FBImage';
import {firebaseConfig} from '@/firebase/config';

type StepState = 'yet' | 'running' | 'done';

type GeneratePodcastStepName =
    "prepare"
    | "research"
    | "planning"
    | "writing"
    | "recoding"
    | "generateMusic"
    | "mastering"
    | "done"

type GeneratePodcastState = {
    show: boolean
    generating: boolean
    steps: Record<GeneratePodcastStepName, StepState>
    error: string | null
    done: boolean
    dryRun: boolean
};

type GeneratePodcastStep = {
    title: string;
    description: string;
    children?: GeneratePodcastStep[],
    icon: IconType
    stepName?: GeneratePodcastStepName
    showDryRun: boolean
}

type GeneratePodcastStateAction =
    | { type: 'start', payload: { dryRun: boolean } }
    | { type: 'research' }
    | { type: 'planning' }
    | { type: 'writing' }
    | { type: 'recoding' }
    | { type: 'generateMusic' }
    | { type: 'mastering' }
    | { type: 'done' }
    | { type: 'error', payload: string }
    | { type: 'hideToast' }


const initialGeneratePodcastState: GeneratePodcastState = {
    show: false,
    generating: false,
    steps: {
        prepare: 'running',
        research: 'yet',
        planning: 'yet',
        writing: 'yet',
        recoding: 'yet',
        mastering: 'yet',
        generateMusic: 'yet',
        done: 'yet'
    },
    error: null,
    done: false,
    dryRun: false
};


function generatePodcastStateReducer(state: GeneratePodcastState, action: GeneratePodcastStateAction): GeneratePodcastState {
    switch (action.type) {
        case 'start': {
            return {
                ...state,
                ...initialGeneratePodcastState,
                show: true,
                generating: true,
                dryRun: action.payload.dryRun
            }
        }
        case 'research': {
            return {
                ...state,
                steps: {
                    ...state.steps,
                    prepare: 'done',
                    research: 'running'
                }
            }
        }
        case "planning": {
            return {
                ...state,
                steps: {
                    ...state.steps,
                    prepare: 'done',
                    research: 'done',
                    planning: 'running'
                }
            }
        }
        case "generateMusic": {
            return {
                ...state,
                steps: {
                    ...state.steps,
                    prepare: 'done',
                    research: 'done',
                    planning: 'done',
                    generateMusic: 'running'
                }
            }
        }
        case "writing": {
            return {
                ...state,
                steps: {
                    ...state.steps,
                    prepare: 'done',
                    research: 'done',
                    planning: 'done',
                    writing: 'running'
                }
            }
        }
        case "recoding": {
            return {
                ...state,
                steps: {
                    ...state.steps,
                    research: 'done',
                    planning: 'done',
                    writing: 'done',
                    recoding: "running"
                }
            }
        }
        case "mastering": {
            return {
                ...state,
                steps: {
                    ...state.steps,
                    research: 'done',
                    planning: 'done',
                    generateMusic: 'done',
                    writing: 'done',
                    recoding: "done",
                    mastering: "running"
                }
            }
        }
        case "done": {
            return {
                ...state,
                generating: false,
                show: true,
                done: true,
                steps: {
                    ...state.steps,
                    prepare: 'done',
                    research: 'done',
                    planning: 'done',
                    generateMusic: 'done',
                    writing: 'done',
                    recoding: "done",
                    mastering: "done",
                    done: 'done',
                }
            }
        }
        case "error": {
            return {
                ...state,
                generating: false,
                show: true,
                done: true,
                error: action.payload
            }
        }
        case "hideToast": {
            return {
                ...state,
                show: false,
            }
        }
    }
}


const generatePodcastSteps: GeneratePodcastStep[] = [
    {
        title: "準備",
        description: "データの準備を行ってます。",
        icon: HiOutlineSparkles,
        stepName: "prepare",
        showDryRun: true
    },
    {
        title: "リサーチ",
        description: "コーナーを作成するための調査を行います。",
        icon: HiMagnifyingGlass,
        stepName: "research",
        showDryRun: true
    },
    {
        title: "プランニング",
        description: "調査結果からコーナーの計画を行います。",
        icon: HiOutlineChatBubbleLeftEllipsis,
        stepName: "planning",
        showDryRun: true
    },
    {
        title: "コンテンツの作成",
        description: "ポッドキャストのコンテンツを作成します。",
        icon: HiOutlineRadio,
        showDryRun: true,
        children: [
            {
                title: "ライティング",
                description: "台本を作成します。",
                icon: HiMiniPencilSquare,
                stepName: "writing",
                showDryRun: true
            },
            {
                title: "レコーディング",
                description: "台本からレコーディングを行います。",
                icon: HiMicrophone,
                stepName: "recoding",
                showDryRun: false
            },
            {
                title: "音楽制作",
                description: "音楽の作成を行います。",
                icon: HiOutlineMusicalNote,
                stepName: "generateMusic",
                showDryRun: false
            }
        ]
    },
    {
        title: "マスタリング",
        description: "音声と音楽の合成、マスタリング処理を行います。",
        icon: HiOutlineAdjustmentsVertical,
        stepName: "mastering",
        showDryRun: false
    },
    {
        title: "完了",
        description: "完了です。配信一覧からポッドキャストを聞いてみてください。",
        icon: HiOutlineRocketLaunch,
        stepName: "done",
        showDryRun: true
    }
]

function GenerateStepIcon({step, state}: { step: GeneratePodcastStep, state: GeneratePodcastState }) {
    if (!step.stepName) {
        if (step.children) {
            if (step.children.some(s => s.stepName && state.steps[s.stepName] === 'running')) {
                if (state.error) {
                    return (
                        <span
                            className="absolute text-lg flex items-center justify-center w-8 h-8 bg-red-700 rounded-full -start-4 ring-4 ring-white text-gray-700">
                            <HiOutlineExclamationCircle></HiOutlineExclamationCircle>
                        </span>)

                    return
                } else {
                    return (
                        <span
                            className="absolute text-lg flex items-center justify-center w-8 h-8 bg-blue-200 rounded-full -start-4 ring-4 ring-white text-gray-700">
                            <Spinner></Spinner>
                        </span>)
                }
            } else if (step.children.every(s => s.stepName && state.steps[s.stepName] === 'done')) {
                return (
                    <span
                        className="absolute text-lg flex items-center justify-center w-8 h-8 bg-green-300 rounded-full -start-4 ring-4 ring-white text-gray-700">
                    <HiCheckCircle></HiCheckCircle>
                    </span>
                );
            }
        }
        return <span
            className="absolute text-lg flex items-center justify-center w-8 h-8 bg-blue-300 rounded-full -start-4 ring-4 ring-white text-gray-700">
        <HiMiniWrenchScrewdriver></HiMiniWrenchScrewdriver>
        </span>
    }

    const steps = state.steps[step.stepName];
    switch (steps) {
        case "yet":
            return <span
                className="absolute text-lg flex items-center justify-center w-8 h-8 bg-blue-300 rounded-full -start-4 ring-4 ring-white text-gray-700">
                <step.icon></step.icon>
            </span>;
        case "running":
            if (state.error) {
                return <span
                    className="absolute text-lg flex items-center justify-center w-8 h-8 bg-red-700 rounded-full -start-4 ring-4 ring-white text-gray-700">
                <HiOutlineExclamationCircle></HiOutlineExclamationCircle>
            </span>
            } else {
                return <span
                    className="absolute text-lg flex items-center justify-center w-8 h-8 bg-blue-300 rounded-full -start-4 ring-4 ring-white text-gray-700">
                <Spinner/>
            </span>
            }
        case "done":
            return <span
                className="absolute text-lg flex items-center justify-center w-8 h-8 bg-green-300 rounded-full -start-4 ring-4 ring-white text-gray-700">
                <HiCheckCircle></HiCheckCircle>
            </span>;
    }
}

function GenerateStepItem({step, state}: { step: GeneratePodcastStep, state: GeneratePodcastState }) {
    return <li className="mb-6 ms-6">
        <GenerateStepIcon step={step} state={state}></GenerateStepIcon>
        <h3 className="font-medium leading-tight text-gray-700">{step.title}</h3>
        <p className="text-sm mb-2 text-gray-300">{step.description}</p>
        {step.children && (
            <ol className="relative text-gray-500 border-s border-gray-200 ">
                {step.children && step.children.filter(s => !state.dryRun || s.showDryRun).map((s, index) => (
                        <GenerateStepItem key={`step-item-${step.stepName}-${index}`} step={s}
                                          state={state}></GenerateStepItem>
                    )
                )}
            </ol>
        )}
    </li>
}


function ListenerProgramDetailPage() {
    const {programId} = useParams<{ programId: string }>();
    const navigate = useNavigate();
    const [error, setError] = useState<string | null>(null);
    const [generatePodcastState, dispatch] = useReducer(generatePodcastStateReducer, initialGeneratePodcastState);
    const tabsRef = useRef<TabsRef>(null);
    const [_, setActiveTab] = useState(0);
    const {data: programs, isLoading: loadPrograms} = useListenerProgramsServiceGetApiV1ListenerPrograms();

    const activePrograms = (loadPrograms || !programs) ? [] : programs.filter(p => p.id !== programId && p.status === ProgramStatus.ACTIVE);

    // State for audio player modal
    const [showAudioModal, setShowAudioModal] = useState(false);
    const [showingHistory, setShowingHistory] = useState<ProgramBroadcastHistorySchema | null>(null);
    const [currentAudioUrl, setCurrentAudioUrl] = useState<string | null>(null);

    const {currentUser} = useAuth();

    // Fetch listener program
    const {
        data: program,
        isLoading: programLoading,
        error: programError,
        refetch: refetchProgram
    } = useListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramId(
        {listenerProgramId: programId || ""}
    );

    // Fetch segments
    const {
        data: segments,
        isLoading: segmentsLoading,
        error: segmentsError
    } = useListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegments(
        {programId: programId || ""}
    );

    // Fetch broadcast history
    const {
        data: broadcastHistories,
        isLoading: broadcastHistoriesLoading,
        error: broadcastHistoriesError,
        refetch: refetchBroadcastHistories,
    } = useProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistory(
        {programId: programId || ""}
    );

    // Create a unique list of radio cast IDs
    const radioCastIds = new Set<string>();

    // Add base radio cast IDs from the program
    if (program?.baseRadioCastIds) {
        program.baseRadioCastIds.forEach(id => radioCastIds.add(id));
    }

    // Add override radio cast IDs from segments
    if (segments) {
        segments.forEach(segment => {
            if (segment.overrideRadioCasts) {
                segment.overrideRadioCasts.forEach(id => radioCastIds.add(id));
            }
        });
    }

    // Fetch radio casts
    const {
        data: radioCasts,
        isLoading: radioCastsLoading,
        error: radioCastsError
    } = useRadioCastsServiceGetApiV1RadioCasts(
        {radioCastIds: Array.from(radioCastIds)},
        UseRadioCastsServiceGetApiV1RadioCastsKeyFn({radioCastIds: Array.from(radioCastIds)}),
        {enabled: radioCastIds.size > 0}
    );


    // Filter radio casts by IDs
    const programRadioCasts = radioCasts?.filter(
        cast => radioCastIds.has(cast.id || "")
    ) || [];

    const handleGenerateRadioSSE = (response: Response) => {
        refetchBroadcastHistories();
        const reader = response.body?.getReader();
        const decoder = new TextDecoder('utf-8');
        let prevLine: string = '';
        const read = () => {
            reader?.read()
                .then(({done, value}) => {
                    if (done) {
                        refetchBroadcastHistories();
                        return;
                    }
                    const chunk = decoder.decode(value, {stream: true});
                    const lines = chunk.split(/^data:\s*/gm)
                        .filter(line => line && line !== "")
                        .map(line => `data: ${line}`);
                    lines.forEach((line) => {
                        let data = line.replace(/^data:\s*/, '');
                        if (!data || data === "") {
                            return;
                        }
                        try {
                            if (!data.startsWith("{") && prevLine && prevLine.startsWith("{")) {
                                data = prevLine + data;
                            }
                            console.log(data);
                            const event = JSON.parse(data);
                            prevLine = '';
                            if (event.error || event.errorMessage || event.errorCode) {
                                dispatch({type: "error", payload: event.error || event.errorMessage || event.errorCode});
                                return;
                            }

                            switch (event.author) {
                                case "ResearchFlowAgent": {
                                    if (generatePodcastState.steps.research === 'yet') {
                                        dispatch({type: "research"});
                                    }
                                    break;
                                }
                                case "ProgramPlannerAgent": {
                                    if (generatePodcastState.steps.planning === 'yet') {
                                        dispatch({type: "planning"});
                                    }
                                    break;
                                }
                                case "ProgramSegmentWriterFlowAgent": {
                                    if (generatePodcastState.steps.writing === 'yet') {
                                        dispatch({type: "writing"});
                                    }
                                    break;
                                }
                                case "RecordingFlowAgent": {
                                    if (generatePodcastState.steps.recoding === 'yet') {
                                        dispatch({type: "recoding"});
                                    }
                                    break;
                                }
                                case "ComposerFlowAgent": {
                                    if (generatePodcastState.steps.generateMusic === 'yet') {
                                        dispatch({type: "generateMusic"});
                                    }
                                    break;
                                }
                                case "MasteringAgent": {
                                    if (generatePodcastState.steps.mastering === 'yet') {
                                        dispatch({type: "mastering"});
                                    }
                                    break;
                                }
                                case "done": {
                                    dispatch({type: "done"});
                                }
                            }
                        } catch (e) {
                            prevLine = data;
                            if (!(e instanceof SyntaxError)) {
                                console.error(e, data);
                            }
                            return;
                        }
                    });

                    read();  // Read the next chunk
                })
                .catch((err) => {
                    console.error(err);
                });
        };

        read();
    };

    // Delete mutation
    const deleteMutation = useListenerProgramsServiceDeleteApiV1ListenerProgramsByListenerProgramId({
        onSuccess: () => {
            navigate("/listener-programs");
        },
        onError: (error) => {
            setError(`削除に失敗しました: ${error.message}`);
        }
    });

    // Function to handle delete
    const handleDelete = () => {
        if (confirm("このプログラムを削除してもよろしいですか？")) {
            deleteMutation.mutate({listenerProgramId: programId || ""});
        }
    };

    const activateMutation = useListenerProgramsServicePutApiV1ListenerProgramsByListenerProgramId({
        onSuccess: () => refetchProgram(),
        onError: (error) => {
            setError(`変更に失敗しました: ${error.message}`);
        }
    })
    const handleActivate = () => {

        if (program!.status === ProgramStatus.PAUSE && activePrograms.length > 0) {
            return;
        }

        const msg = program!.status === ProgramStatus.ACTIVE ? "このプログラムの定期実行を停止してもよろしいですか？" : "このプログラムの定期実行を開始してもよろしいですか？"

        if (confirm(msg)) {
            activateMutation.mutate({
                listenerProgramId: programId || "",
                requestBody: {status: program!.status === ProgramStatus.ACTIVE ? ProgramStatus.PAUSE : ProgramStatus.ACTIVE}
            });
        }
    };


    // Function to render broadcast status badge with appropriate color
    const renderBroadcastStatus = (status: ProgramBroadcastHistoryStatus) => {
        let color: string;

        switch (status) {
            case "generating":
                color = "warning";
                break;
            case "success":
                color = "success";
                break;
            case "failure":
                color = "failure";
                break;
            default:
                color = "info";
        }

        return <Badge className="inline-block" color={color}>{getBroadcastStatusText(status)}</Badge>;
    };

    // Function to convert broadcast status to Japanese
    const getBroadcastStatusText = (status: ProgramBroadcastHistoryStatus) => {
        switch (status) {
            case "prepare":
                return "準備中";
            case "generating":
                return "生成中";
            case "success":
                return "完了";
            case "failure":
                return "失敗";
            default:
                return status;
        }
    };

    // Loading state
    if (programLoading || segmentsLoading || radioCastsLoading || broadcastHistoriesLoading) {
        return (
            <div className="flex justify-center items-center h-64">
                <Spinner size="xl"/>
            </div>
        );
    }

    // Error state
    if (programError || segmentsError || radioCastsError || broadcastHistoriesError) {
        return (
            <Alert color="failure">
                <span className="font-medium">エラー:</span> データの取得に失敗しました
            </Alert>
        );
    }

    // If program not found
    if (!program) {
        return (
            <Alert color="failure">
                <span className="font-medium">エラー:</span> プログラムが見つかりません
            </Alert>
        );
    }

    const handleGenerateFirstPodCast = async () => {
        if (program.numberOfBroadcast === undefined || program.numberOfBroadcast > 0) {
            return;
        }
        tabsRef.current?.setActiveTab(2);
        const dryRun = true
        dispatch({type: "start", payload: {dryRun}});
        fetch(
            `${OpenAPI.BASE}/api/v1/listener-programs/${programId}/generate-podcast?dry_run=${dryRun}`,
            {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'text/event-stream',
                    'Authorization': `bearer ${await currentUser?.getIdToken()}`
                },
                body: JSON.stringify({})
            }
        ).then(handleGenerateRadioSSE).catch(error => console.log(error));
        //
        // ListenerProgramsService.postApiV1ListenerProgramsByListenerProgramIdGeneratePodcast({listenerProgramId: programId!}).then(value => {
        //     console.log(value);
        // });
    };

    const handleRegeneratePodcast = async (broadcastHistoryId: string, dryRun: boolean) => {
        dispatch({type: "start", payload: {dryRun}});
        fetch(
            `${OpenAPI.BASE}/api/v1/listener-programs/${programId}/broadcast_history/${broadcastHistoryId}/generate-podcast?dry_run=${dryRun}`,
            {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'text/event-stream',
                    'Authorization': `bearer ${await currentUser?.getIdToken()}`
                },
                body: JSON.stringify({})
            }
        ).then(handleGenerateRadioSSE).catch(error => console.log(error));
    };

    // Function to handle playing audio
    const handlePlayAudio = async (history: ProgramBroadcastHistorySchema) => {
        try {
            setShowingHistory(history);
            setCurrentAudioUrl(null);
            setShowAudioModal(true);

            if (history.dryRun) {
                return;
            }

            // Fetch the audio data
            const response = (await ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudio({
                programId: programId!, broadcastHistoryId: history.id!
            }));

            if (!(response instanceof Blob)) {
                throw new Error(`failed to fetch audio data: ${response}`)
            }

            // Get the audio data as an ArrayBuffer
            const audioData = await response.arrayBuffer();

            // Convert the audio data to a base64 data URI
            const base64 = btoa(
                new Uint8Array(audioData)
                    .reduce((data, byte) => data + String.fromCharCode(byte), '')
            );

            // Set the audio URL and show the modal
            setCurrentAudioUrl(`data:audio/mp3;base64,${base64}`);
        } catch (error) {
            console.error('Error playing audio:', error);
            alert('音声の再生中にエラーが発生しました。');
        }
    };

    return (
        <div className="mx-auto px-4 py-8">
            {error && (
                <Alert color="failure" className="mb-4">
                    {error}
                </Alert>
            )}

            <header className="mb-8">
                {/* カバー画像とタイトル */}
                <div className="flex gap-6 mb-6">
                    {/* カバー画像 */}
                    <div className="flex-shrink-0">
                        <FBImage
                            path={program.coverArtUri ? program.coverArtUri.replace('gs://' + firebaseConfig.storageBucket + '/', '') : null}
                            alt={`${program.title} カバー画像`}
                            className="w-48 h-48 object-cover rounded-lg border shadow-lg"
                        />
                    </div>

                    {/* プログラム情報 */}
                    <div className="flex-1">
                        <div className="flex justify-between items-start mb-4">
                            <h1 className="text-3xl font-bold">{program.title}</h1>
                            <div className="flex gap-2">
                                {program.status === ProgramStatus.PAUSE && <Popover content={(
                                    <div className="w-64 text-sm text-gray-500 dark:text-gray-400">
                                        <div className="px-3 py-2">
                                            {program.status === ProgramStatus.PAUSE && activePrograms.length > 0 ?
                                                <p>既に定期実行中のラジオ番組があります。<br/>現在
                                                    定期実行が可能な番組はユーザあたり最大1つです。</p> :
                                                <p>毎朝5時にスケジュールに配信スケジュールにマッチすれば自動作成されます。</p>}
                                        </div>
                                    </div>
                                )} trigger="hover"><Button color="light" onClick={handleActivate}
                                                           className={program.status === ProgramStatus.PAUSE && activePrograms.length > 0 ? 'disabled' : ''}>
                                    定期実行を開始
                                </Button></Popover>}
                                {program.status === ProgramStatus.ACTIVE && <Popover content={(
                                    <div className="w-64 text-sm text-gray-500 dark:text-gray-400">
                                        <div className="px-3 py-2">
                                            <p>定期配信が停止されます。</p>
                                        </div>
                                    </div>
                                )} trigger="hover"><Button color="light" onClick={handleActivate}>
                                    定期実行を停止
                                </Button></Popover>}
                                <Button as={Link} to="./edit" color="light">
                                    編集
                                </Button>
                                <Button as={Link} to="./segments/create" color="light">
                                    コーナー編集
                                </Button>
                                <Button color="red" onClick={handleDelete}>
                                    削除
                                </Button>

                                {segments && segments.length > 0 && broadcastHistories && broadcastHistories.length === 0 &&
                                    <Button color="blue" onClick={handleGenerateFirstPodCast}
                                            disabled={generatePodcastState.generating}>
                                        第0回を作成(お試し作成)
                                    </Button>
                                }
                            </div>
                        </div>
                        <div className="flex items-center gap-4 mb-2">
                            <span className="text-sm">プログラム時間: {program.programMinutes}分</span>
                            <span className="text-sm">定期作成: <ProgramStatusBadge
                                status={program.status}></ProgramStatusBadge></span>
                            <span
                                className="text-sm">配信スケジュール: {program.broadcastSchedule === BroadcastSchedule.DAILY ? '毎日' : '毎週'}</span>
                            <span className="text-sm">公開設定: <Badge className="inline-block"
                                                                       color={program.publishSetting === PublishSetting.PRIVATE ? 'gray' : 'info'}>{program.publishSetting === PublishSetting.PRIVATE ? '非公開' : program.publishSetting === PublishSetting.LIMITED ? '限定公開' : '公開'}</Badge></span>
                            {program.broadcastSchedule === BroadcastSchedule.WEEKLY && program.broadcastDayofweek && program.broadcastDayofweek.length > 0 && (
                                <span>配信曜日: {program.broadcastDayofweek.map(day => {
                                    switch (day) {
                                        case 'monday':
                                            return '月';
                                        case 'tuesday':
                                            return '火';
                                        case 'wednesday':
                                            return '水';
                                        case 'thursday':
                                            return '木';
                                        case 'friday':
                                            return '金';
                                        case 'saturday':
                                            return '土';
                                        case 'sunday':
                                            return '日';
                                        default:
                                            return day;
                                    }
                                }).join(', ')}</span>
                            )}
                            {program.publishedAt && (
                                <span>公開日: {new Date(program.publishedAt).toLocaleDateString()}</span>
                            )}
                        </div>
                        {program.status !== ProgramStatus.DRAFT && program.publishSetting !== PublishSetting.PRIVATE && broadcastHistories && broadcastHistories.length > 0 && (
                            <div className="flex items-center gap-2 mb-2">
                                <span>配信URL:</span>
                                <div className="grid w-full max-w-200">
                                    <div className="relative">
                                        <label htmlFor="publish-url" className="sr-only">
                                            配信URL
                                        </label>
                                        <input
                                            id="publish-url"
                                            type="text"
                                            className="col-span-6 block w-full rounded-lg border border-gray-300 bg-gray-50 px-2.5 py-3 text-sm text-gray-500 focus:border-blue-500 focus:ring-blue-500"
                                            value={`https://ppp-jjoi5qw7aa-an.a.run.app/api/v1/podcast/rss/${program.id}${program.publishSetting === PublishSetting.LIMITED ? `?privateKey=${program.privateKey}` : ''}`}
                                            disabled
                                            readOnly
                                        />
                                        <ClipboardWithIconText
                                            valueToCopy={`https://ppp-jjoi5qw7aa-an.a.run.app/api/v1/podcast/rss/${program.id}${program.publishSetting === PublishSetting.LIMITED ? `?privateKey=${program.privateKey}` : ''}`}/>
                                    </div>
                                </div>
                            </div>
                        )}

                        <p className="p-5 bg-white rounded-lg border border-gray-200 text-gray-600">{program.description}</p>
                    </div>

                </div>

            </header>

            <Tabs variant="underline" ref={tabsRef} onActiveTabChange={(tab) => setActiveTab(tab)}>
                <TabItem title="コーナー" icon={HiMiniListBullet} active>
                    {segments && segments.length > 0 ? (
                        <Card>
                            <Table>
                                <TableHead>
                                    <TableRow>
                                        <TableHeadCell>タイトル</TableHeadCell>
                                        <TableHeadCell>説明</TableHeadCell>
                                        <TableHeadCell>タイプ</TableHeadCell>
                                        <TableHeadCell>順序</TableHeadCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody className="divide-y">
                                    {segments.sort((a, b) => a.order - b.order).map((segment) => (
                                        <TableRow key={segment.id} className="bg-white">
                                            <TableCell className="font-medium text-gray-900">
                                                {segment.title}
                                            </TableCell>
                                            <TableCell>
                                                {segment.description}
                                            </TableCell>
                                            <TableCell>{segment.segmentType}</TableCell>
                                            <TableCell>{segment.order}</TableCell>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        </Card>
                    ) : (
                        <div className="text-center py-8">
                            <p className="text-gray-500 mb-4">コーナーがまだありません</p>
                            <Button as={Link} to="./segments/create">
                                コーナーを追加
                            </Button>
                        </div>
                    )}
                </TabItem>
                <TabItem title="ラジオキャスト" icon={HiMicrophone}>
                    {programRadioCasts.length > 0 ? (
                        <Card>
                            <Table>
                                <TableHead>
                                    <TableRow>
                                        <TableHeadCell>タイトル</TableHeadCell>
                                        <TableHeadCell>説明</TableHeadCell>
                                        <TableHeadCell>タイプ</TableHeadCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody className="divide-y">
                                    {programRadioCasts.map((cast: RadioCastSchema) => (
                                        <TableRow key={cast.id} className="bg-white">
                                            <TableCell className="font-medium text-gray-900">
                                                {cast.name}
                                            </TableCell>
                                            <TableCell>
                                                {cast.personality && cast.personality.length > 50
                                                    ? `${cast.personality.substring(0, 50)}...`
                                                    : cast.personality}
                                            </TableCell>
                                            <TableCell>{cast.role} / {cast.voiceName}</TableCell>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        </Card>
                    ) : (
                        <div className="text-center py-8">
                            <p className="text-gray-500">ラジオキャストがありません</p>
                        </div>
                    )}
                </TabItem>
                <TabItem title="配信履歴" icon={HiOutlineSignal}>
                    {broadcastHistories && broadcastHistories.length > 0 ? (
                        <Card>
                            <Table>
                                <TableHead>
                                    <TableRow>
                                        <TableHeadCell className="">配信回</TableHeadCell>
                                        <TableHeadCell className="">ステータス</TableHeadCell>
                                        <TableHeadCell className="">作成日時</TableHeadCell>
                                        <TableHeadCell className="text-center">アクション</TableHeadCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody className="divide-y">
                                    {broadcastHistories.sort((a, b) => b.no - a.no).map((history) => (
                                        <TableRow key={history.id} className="bg-white">
                                            <TableCell className="font-medium text-gray-900">
                                                第{history.no}回
                                            </TableCell>
                                            <TableCell>
                                                {renderBroadcastStatus(history.status)}
                                            </TableCell>
                                            <TableCell>
                                                {new Date(history.createdAt).toLocaleString()}
                                            </TableCell>
                                            <TableCell>
                                                <div className="text-center flex items-center justify-center gap-1">
                                                    {history.status === "success" && (
                                                        <Button className="text-nowrap"
                                                                onClick={() => handlePlayAudio(history)}
                                                                size="xs" color="light"
                                                                disabled={showAudioModal || generatePodcastState.show}>
                                                            {history.dryRun ?
                                                                <><HiCheckCircle className="mr-1"/>確認</>
                                                                : <><HiMiniPlay className="mr-1"/>再生</>}
                                                        </Button>
                                                    )}
                                                    {history.status === "success" && history.dryRun && (
                                                        <Button className="text-nowrap"
                                                                onClick={() => handleRegeneratePodcast(history.id!, true)}
                                                                size="xs" color="light"
                                                                disabled={showAudioModal || generatePodcastState.show}>
                                                            <HiOutlineArrowPath className="mr-1"/>再作成
                                                        </Button>
                                                    )}
                                                    {history.status === "success" && history.dryRun && (
                                                        <Button className="text-nowrap"
                                                                onClick={() => handleRegeneratePodcast(history.id!, false)}
                                                                size="xs" color="light"
                                                                disabled={showAudioModal || generatePodcastState.show}>
                                                            <HiMiniMegaphone className="mr-1"/>音声作成
                                                        </Button>
                                                    )}
                                                    {history.status === "failure" && (
                                                        <Button
                                                            className="text-nowrap"
                                                            onClick={() => handleRegeneratePodcast(history.id!, history.dryRun)}
                                                            size="xs"
                                                            color="light"
                                                            disabled={showAudioModal || generatePodcastState.show}>
                                                            <HiOutlineArrowPath className="mr-1"/>再実行
                                                        </Button>
                                                    )}
                                                </div>
                                            </TableCell>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        </Card>
                    ) : (
                        <div className="text-center py-8">
                            <p className="text-gray-500">配信履歴がまだありません</p>
                        </div>
                    )}
                </TabItem>
            </Tabs>

            {generatePodcastState.show && (
                <Toast className="absolute bottom-2 right-2 items-start h-[80vh] overflow-y-auto z-10">
                    <div className="flex flex-col">
                        <h2 className="text-2xl font-bold mb-4">第0回の作成</h2>
                        {generatePodcastState.dryRun && (
                            <p className="text-sm text-gray800 font-normal">
                                お試し版のトークスクリプトのみが作成されます。
                                配信履歴で生成されたトークスクリプトを確認後、「音声作成」ボタンをクリックしてください。
                            </p>
                        )}
                        {generatePodcastState.error && (
                            <p className="text-sm font-normal text-red-700">Error: {generatePodcastState.error}</p>
                        )}
                        <div className="ml-3 text-sm font-normal">
                            <ol className="relative border-s border-gray-200">
                                {generatePodcastSteps
                                    .filter(step => !generatePodcastState.dryRun || step.showDryRun).map((step, index) => (
                                        <GenerateStepItem key={`step-item-${index}`} step={step}
                                                          state={generatePodcastState}/>))}
                            </ol>
                        </div>
                    </div>
                    {generatePodcastState.done && <ToastToggle onDismiss={() => dispatch({type: "hideToast"})}/>}
                </Toast>
            )}

            {/* Audio Player Modal */}
            <Modal size="7xl" show={showAudioModal && !!showingHistory} onClose={() => setShowAudioModal(false)}>
                {showingHistory && (<>
                        <ModalHeader>第{showingHistory!.no!}回 {showingHistory!.dryRun ? "トークスクリプト確認" : "再生"}</ModalHeader>
                        <ModalBody>
                            <div className="flex flex-col">
                                {!showingHistory!.dryRun && <div className="w-full h-full">
                                    {currentAudioUrl ? (
                                        <audio controls className="w-full">
                                            <source src={currentAudioUrl} type="audio/mp3"/>
                                            お使いのブラウザは音楽再生をサポートしていません。
                                        </audio>
                                    ) : (
                                        <p><Spinner className="mr-1"/>データを読み込み中...</p>
                                    )}
                                </div>}
                                <Tabs variant="underline">
                                    {showingHistory!.newsLetterContents && (
                                        <TabItem active title="配信内容" icon={HiEnvelopeOpen}>
                                            <div className="markdown">
                                            <ReactMarkdown
                                                remarkPlugins={[remarkGfm]}>{showingHistory!.newsLetterContents}</ReactMarkdown>
                                            </div>
                                        </TabItem>
                                    )}
                                    {showingHistory.talkScript && (
                                        <TabItem active={!showingHistory!.newsLetterContents} title="トーク内容"
                                                 icon={HiOutlineChatBubbleLeftRight}>
                                            <div className="overflow-hidden w-auto">
                                                <pre
                                                    className="break-all overflow-auto leading-7">{showingHistory!.talkScript}</pre>
                                            </div>
                                        </TabItem>
                                    )}
                                </Tabs>
                            </div>
                        </ModalBody>
                    </>

                )}
            </Modal>
        </div>
    );
}

export default function ListenerProgramDetail() {
    return <ListenerProgramDetailPage/>;
}

export function meta() {
    return [
        {title: "プログラム詳細 - Personalized Podcast Platform"},
        {name: "description", content: "ポッドキャストプログラムの詳細情報"},
    ];
}
