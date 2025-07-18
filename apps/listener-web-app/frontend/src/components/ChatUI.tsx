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

import React, {useState, useRef, useEffect} from 'react';
import {Button, Avatar, TextInput, Spinner, Popover} from 'flowbite-react';
import {HiChat, HiX, HiPaperAirplane} from 'react-icons/hi';
import {AgentRunRequest, FunctionCall, FunctionResponse, OpenAPI, Part} from "@api/requests";
import type {Event as AdkEvent} from "@api/requests/types.gen";
import {useAuth} from "@/firebase/auth.tsx";
import {useLocalStorage} from "@/hooks/useLocalStorage.ts";
import {
    useAgentsServicePostApiV1AgentsByAppNameSession,
    useAgentsServiceGetApiV1AgentsByAppNameSessionBySessionId
} from '@api/queries';
import {UseAgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdKeyFn} from '@api/queries';
import ReactMarkdown from "react-markdown";
import {HiCheckCircle} from "react-icons/hi2";
import remarkGfm from "remark-gfm";

interface ChatMessage {
    id: string;
    content?: string | null;
    functionCall?: FunctionCall | null;
    functionResponse?: FunctionResponse | null;
    runningState?: 'running' | 'done';
    isUser: boolean;
    timestamp: Date;
}

interface ChatUIProps {
    appName: string;
    agentName: string;
    icon?: string;
}

const functionCallNameMap: {[key: string]: string} = {
    "rss_rag_tool": "P2-RS (RSS AI Agent)",
    "create_listener_program": "P4-CA (Program Generate Agent)",
    "update_listener_program_segments": "P4-SCA (Program Segment Generate Agent)",
    "get_radio_casts": "P4-RC (Radio Casts Agent)"
};

function getFunctionCallName(message: ChatMessage) {
    if (!message.functionCall && !message.functionResponse) {
        return '';
    }

    const functionName = message.functionCall?.name || message.functionResponse?.name;

    const name = functionCallNameMap[functionName!];
    if (!name) {
        return "P2-NF"
    }
    return name;
}

function getFunctionCallMessage(message: ChatMessage) {
    if (!message.functionCall && !message.functionResponse) {
        return '';
    }
    const name = getFunctionCallName(message);
    if (!name) {
        return '';
    }
    const stateIcon = message.runningState === 'running' ? <Spinner /> : <HiCheckCircle className="text-green-400 text-xl" />
    const stateMessage = message.runningState === 'running' ? 'に問い合わせ中' : ' 完了'
    return <div className="flex items-center gap-1"><span>{stateIcon}</span><span>{name + stateMessage}</span></div>
}


function isAgentRunRequest(input: any): input is AgentRunRequest {
    if (typeof input === "string") {
        return false;
    }

    return 'appName' in input;
}

function getRunningState(part: Part): ChatMessage['runningState'] {
    if (!part.functionCall && !part.functionResponse) {
        return undefined;
    }
    if (!part.functionResponse) {
        return 'running';
    }
    return 'done';
}

function createMessageFromEvent(event: AdkEvent & { detail?: string; error?: string }, ignoreCalling = false): ChatMessage[] {
    console.log(event);
    if (!event || !event.content || !event.content.parts || !event.content.parts.length) {
        return [];
    }

    const parts = event.content.parts.filter(part => !ignoreCalling || !part.functionCall);

    return parts.map((part, index) => ({
        id: `${event.id}-${index}` || `message-${index}-${new Date().getTime()}`,
        content: part.text,
        functionCall: part.functionCall,
        functionResponse: part.functionResponse,
        runningState: getRunningState(part),
        isUser: event.content!.role === "user" && !part.functionResponse,
        timestamp: new Date(),
    }));
}

/**
 * Floating Chat UI Component
 * Displays as a FAB in the bottom right corner and opens a floating chat interface
 */
export default function ChatUI({appName, icon, agentName}: ChatUIProps) {
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState<ChatMessage[]>([{
        id: "initial",
        content: `ピー！リスナーさん、こんにちはっピ！P3がラジオ番組作りのお手伝いをしちゃうっピ！どんなラジオ番組を作りたいか、P3に教えてほしいっピ！`,
        isUser: false,
        timestamp: new Date()
    }]);
    const [sending, setSending] = useState(false);
    const [partialMessage, setPartialMessage] = useState<ChatMessage | null>(null);
    const [inputValue, setInputValue] = useState('');
    const {currentUser} = useAuth();
    const [sessionId, setSessionId] = useLocalStorage<string | null>("currentSessionId", null);
    const messagesEndRef = useRef<HTMLDivElement>(null);
    const inputRef = useRef<HTMLInputElement>(null);
    const {
        mutate: createSessionMutate,
        isPending: isPendingCreateSession
    } = useAgentsServicePostApiV1AgentsByAppNameSession({
        onSuccess: data => {
            setSessionId(data.id);
        }
    });
    const {data: session, error: sessionError} = useAgentsServiceGetApiV1AgentsByAppNameSessionBySessionId({
        appName, sessionId: sessionId!
    }, UseAgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdKeyFn({
        appName,
        sessionId: sessionId!
    }), {enabled: !!sessionId && !!currentUser})

    if (session && session.events?.length && messages.length == 1) {
        session.events.filter(event => event.content && event.content.parts && event.content.parts.length).map((event) => {
            const messages = createMessageFromEvent(event, true);
            if (messages.length) {
                setMessages(prev => prev.concat(messages))
            }
        });
    }
    if (sessionError && !isPendingCreateSession && currentUser) {
        createSessionMutate({appName, requestBody: {}});
    }

    const handleSSE = (callback?: () => void) => (response: Response) => {
        setSending(false);
        const reader = response.body?.getReader();
        const decoder = new TextDecoder('utf-8');
        let prevLine: string = '';
        const read = () => {
            reader?.read()
                .then(({done, value}) => {
                    if (done) {
                        callback && callback();
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
                            const event: AdkEvent & { detail?: string, error?: string } = JSON.parse(data);
                            prevLine = '';

                            if (event.detail && event.detail === "Session not found") {
                                setSessionId(null);
                                return;
                            }

                            if (event.errorMessage || event.error) {

                                if (partialMessage) {
                                    setMessages(prev => [...prev, partialMessage]);
                                    setPartialMessage(null);
                                }

                                setMessages(prev => [...prev, {
                                    id: event.id || `error${new Date().getTime()}`,
                                    content: event.errorMessage! || event.error!,
                                    isUser: false,
                                    timestamp: new Date(),
                                }]);
                                return;
                            }

                            const messages = createMessageFromEvent(event);
                            if (!messages.length) {
                                return;
                            }
                            if (event.partial) {
                                // partial message
                                const message = messages.pop()!;
                                setPartialMessage(partialMessage => partialMessage ? {
                                    ...partialMessage,
                                    ...message,
                                    content: (partialMessage.content || '') + (message.content || ''),
                                } : message);
                            } else {
                                setPartialMessage(null);
                                setMessages(prev => {

                                    const runningDone = messages.some(m => m.runningState === "done");

                                    if (runningDone) {
                                        prev.pop();
                                        return [...prev, ...messages];
                                    } else {
                                        return [...prev, ...messages]
                                    }
                                })
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

    const sendMessage = async (input: string | AgentRunRequest, sessionId: string | null, callback?: () => void) => {
        if (!sessionId) {
            return;
        }
        if (sending) {
            return;
        }
        setSending(true);

        const req: AgentRunRequest = isAgentRunRequest(input) ? input : {
            appName: appName,
            sessionId: sessionId,
            streaming: true,
            newMessage: input
        };

        fetch(
            `${OpenAPI.BASE}/api/v1/agents/chat`,
            {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'text/event-stream',
                    'Authorization': `bearer ${await currentUser?.getIdToken()}`
                },
                body: JSON.stringify(req)
            }
        )
            .then(handleSSE(callback))
            .catch(error => console.log(error));
    };


    useEffect(() => {
        if (!sessionId && !isPendingCreateSession && currentUser) {
            createSessionMutate({appName: appName, requestBody: {}})
        }
    }, [sessionId, createSessionMutate, appName, currentUser]);

    // Auto-scroll to bottom when new messages are added
    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({behavior: 'smooth'});
    }, [messages, partialMessage]);

    // Focus input when chat opens
    useEffect(() => {
        if (isOpen && inputRef.current) {
            inputRef.current.focus();
        }
    }, [isOpen]);


    const handleSendMessage = () => {
        if (!inputValue.trim()) {
            return;
        }

        const userMessage: ChatMessage = {
            id: Date.now().toString(),
            content: inputValue,
            isUser: true,
            timestamp: new Date(),
        };

        setMessages(prev => [...prev, userMessage]);
        setInputValue('');

        sendMessage(inputValue, sessionId);
    };

    const handleKeyPress = (e: React.KeyboardEvent) => {
        // support for japanese IME
        if (e.nativeEvent.isComposing) {
            return;
        }

        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage();
        }
    };

    const toggleChat = () => {
        setIsOpen(!isOpen);
    };

    function MessageItem(message: ChatMessage) {
        return <div
            key={message.id}
            className={`flex ${message.isUser ? 'justify-end' : 'justify-start'}`}
        >
            <div
                className={`flex items-start space-x-2 ${message.isUser ? 'flex-row-reverse space-x-reverse' : ''}`}>
                {!message.isUser && (
                    <div className="h-6 w-6 flex-shrink-0">
                        <Avatar
                            img={icon}
                            alt={`${agentName} icon`}
                            size="xs"
                            rounded
                            placeholderInitials={appName.charAt(0).toUpperCase()}
                        />
                    </div>
                )}

                <div
                    className={`px-4 py-2 rounded-lg ${
                        message.isUser
                            ? 'bg-blue-500 text-white rounded-br-none'
                            : 'bg-gray-100 text-gray-900 rounded-bl-none'
                    }`}
                >
                    {message.content && <div className="text-sm">
                        {message.isUser ? message.content : <div className="markdown"><ReactMarkdown remarkPlugins={[remarkGfm]}>{message.content}</ReactMarkdown></div>}
                    </div>}
                    {message.runningState && <div className="text-sm">{getFunctionCallMessage(message)}</div>}
                    <p className={`text-xs mt-1 ${message.isUser ? 'text-blue-100' : 'text-gray-500'}`}>
                        {message.timestamp.toLocaleTimeString('ja-JP', {
                            hour: '2-digit',
                            minute: '2-digit'
                        })}
                    </p>
                </div>
            </div>
        </div>;
    }

    if (!currentUser) {
        // does not show if current user is not found
        return <></>
    }

    return (
        <>
            {/* Floating Action Button */}
            <div className="fixed bottom-6 right-6 z-50">
                <Popover content={
                    <div className="w-64 text-sm text-gray-500 dark:text-gray-400">
                        <div className="px-3 py-2">
                            <p>何か困ってることはないっピ？ P3-COがお助けするっピ！</p>
                        </div>
                    </div>
                } trigger="hover">
                    <Button
                        onClick={toggleChat}
                        className="rounded-full w-14 h-14 p-0 shadow-lg hover:shadow-xl transition-shadow duration-200"
                        color="light"
                    >
                        {isOpen ? (
                            <HiX className="w-6 h-6"/>
                        ) : (
                            <Avatar
                                img={icon}
                                alt={`${agentName} icon`}
                                size="sm"
                                rounded
                                placeholderInitials={agentName.charAt(0).toUpperCase()}
                            />
                        )}
                    </Button>
                </Popover>
            </div>

            {/* Floating Chat Interface */}
            {isOpen && (
                <div
                    className="fixed bottom-24 right-6 w-160 h-[80vh] bg-white rounded-lg shadow-2xl border border-gray-200 z-40 flex flex-col">
                    {/* Chat Header */}
                    <div
                        className="flex items-center justify-between p-4 border-b border-gray-200 bg-blue-50 rounded-t-lg">
                        <div className="flex items-center space-x-3">
                            <Avatar
                                img={icon}
                                alt={`${agentName} icon`}
                                size="sm"
                                rounded
                                placeholderInitials={agentName.charAt(0).toUpperCase()}
                            />
                            <div>
                                <h3 className="font-semibold text-gray-900">{agentName}</h3>
                                <p className="text-xs text-gray-500">オンライン</p>
                            </div>
                        </div>
                        <Button
                            onClick={toggleChat}
                            size="xs"
                            color="gray"
                            className="p-1"
                        >
                            <HiX className="w-4 h-4"/>
                        </Button>
                    </div>

                    {/* Messages Area */}
                    <div className="flex-1 overflow-y-auto p-4 space-y-4">
                        {(!sessionId) && <Spinner size="xl"/>}
                        {messages.map((message) => MessageItem(message))}
                        {partialMessage && MessageItem(partialMessage)}
                        {sending && <Spinner size="xl"/>}
                        <div ref={messagesEndRef}/>
                    </div>

                    {/* Input Area */}
                    <div className="p-4 border-t border-gray-200">
                        <div className="flex space-x-2">
                            <TextInput
                                ref={inputRef}
                                value={inputValue}
                                onChange={(e) => setInputValue(e.target.value)}
                                onKeyPress={handleKeyPress}
                                placeholder="メッセージを入力..."
                                className="flex-1"
                                sizing="sm"
                            />
                            <Button
                                onClick={handleSendMessage}
                                disabled={!sessionId || !inputValue.trim()}
                                size="sm"
                                color="blue"
                                className="px-3"
                            >
                                <HiPaperAirplane className="w-4 h-4"/>
                            </Button>
                        </div>
                    </div>
                </div>
            )}
        </>
    );
}