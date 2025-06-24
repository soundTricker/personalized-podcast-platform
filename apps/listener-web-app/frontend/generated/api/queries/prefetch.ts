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

// generated with @7nohe/openapi-react-query-codegen@1.6.2 

import { type QueryClient } from "@tanstack/react-query";
import { AgentsService, DefaultService, GoogleOauth2Service, ListenerProgramSegmentsService, ListenerProgramsService, ListenersService, PodcastService, ProgramBroadcastHistoryService, RadioCastsService } from "../requests/services.gen";
import * as Common from "./common";
export const prefetchUseListenersServiceGetApiV1ListenersMe = (queryClient: QueryClient) => queryClient.prefetchQuery({ queryKey: Common.UseListenersServiceGetApiV1ListenersMeKeyFn(), queryFn: () => ListenersService.getApiV1ListenersMe() });
export const prefetchUseListenerProgramsServiceGetApiV1ListenerPrograms = (queryClient: QueryClient) => queryClient.prefetchQuery({ queryKey: Common.UseListenerProgramsServiceGetApiV1ListenerProgramsKeyFn(), queryFn: () => ListenerProgramsService.getApiV1ListenerPrograms() });
export const prefetchUseListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramId = (queryClient: QueryClient, { listenerProgramId }: {
  listenerProgramId: string;
}) => queryClient.prefetchQuery({ queryKey: Common.UseListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramIdKeyFn({ listenerProgramId }), queryFn: () => ListenerProgramsService.getApiV1ListenerProgramsByListenerProgramId({ listenerProgramId }) });
export const prefetchUseListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegments = (queryClient: QueryClient, { programId }: {
  programId: string;
}) => queryClient.prefetchQuery({ queryKey: Common.UseListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegmentsKeyFn({ programId }), queryFn: () => ListenerProgramSegmentsService.getApiV1ListenerProgramsByProgramIdSegments({ programId }) });
export const prefetchUseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistory = (queryClient: QueryClient, { programId }: {
  programId: string;
}) => queryClient.prefetchQuery({ queryKey: Common.UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryKeyFn({ programId }), queryFn: () => ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistory({ programId }) });
export const prefetchUseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryId = (queryClient: QueryClient, { broadcastHistoryId, programId }: {
  broadcastHistoryId: string;
  programId: string;
}) => queryClient.prefetchQuery({ queryKey: Common.UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdKeyFn({ broadcastHistoryId, programId }), queryFn: () => ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryId({ broadcastHistoryId, programId }) });
export const prefetchUseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudio = (queryClient: QueryClient, { broadcastHistoryId, programId }: {
  broadcastHistoryId: string;
  programId: string;
}) => queryClient.prefetchQuery({ queryKey: Common.UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudioKeyFn({ broadcastHistoryId, programId }), queryFn: () => ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudio({ broadcastHistoryId, programId }) });
export const prefetchUseRadioCastsServiceGetApiV1RadioCasts = (queryClient: QueryClient, { radioCastIds }: {
  radioCastIds?: string[];
} = {}) => queryClient.prefetchQuery({ queryKey: Common.UseRadioCastsServiceGetApiV1RadioCastsKeyFn({ radioCastIds }), queryFn: () => RadioCastsService.getApiV1RadioCasts({ radioCastIds }) });
export const prefetchUseRadioCastsServiceGetApiV1RadioCastsByRadioCastId = (queryClient: QueryClient, { radioCastId }: {
  radioCastId: string;
}) => queryClient.prefetchQuery({ queryKey: Common.UseRadioCastsServiceGetApiV1RadioCastsByRadioCastIdKeyFn({ radioCastId }), queryFn: () => RadioCastsService.getApiV1RadioCastsByRadioCastId({ radioCastId }) });
export const prefetchUsePodcastServiceGetApiV1PodcastRssByProgramId = (queryClient: QueryClient, { privateKey, programId }: {
  privateKey?: string;
  programId: string;
}) => queryClient.prefetchQuery({ queryKey: Common.UsePodcastServiceGetApiV1PodcastRssByProgramIdKeyFn({ privateKey, programId }), queryFn: () => PodcastService.getApiV1PodcastRssByProgramId({ privateKey, programId }) });
export const prefetchUsePodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryId = (queryClient: QueryClient, { broadcastHistoryId, privateKey, programId }: {
  broadcastHistoryId: string;
  privateKey?: string;
  programId: string;
}) => queryClient.prefetchQuery({ queryKey: Common.UsePodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryIdKeyFn({ broadcastHistoryId, privateKey, programId }), queryFn: () => PodcastService.getApiV1PodcastAudioByProgramIdByBroadcastHistoryId({ broadcastHistoryId, privateKey, programId }) });
export const prefetchUseGoogleOauth2ServiceGetApiV1GoogleOauth2 = (queryClient: QueryClient, { scopes }: {
  scopes: string[];
}) => queryClient.prefetchQuery({ queryKey: Common.UseGoogleOauth2ServiceGetApiV1GoogleOauth2KeyFn({ scopes }), queryFn: () => GoogleOauth2Service.getApiV1GoogleOauth2({ scopes }) });
export const prefetchUseGoogleOauth2ServiceGetApiV1GoogleOauth2Callback = (queryClient: QueryClient, { code, state }: {
  code: string;
  state: string;
}) => queryClient.prefetchQuery({ queryKey: Common.UseGoogleOauth2ServiceGetApiV1GoogleOauth2CallbackKeyFn({ code, state }), queryFn: () => GoogleOauth2Service.getApiV1GoogleOauth2Callback({ code, state }) });
export const prefetchUseAgentsServiceGetApiV1AgentsByAppNameSessionBySessionId = (queryClient: QueryClient, { appName, sessionId }: {
  appName: string;
  sessionId: string;
}) => queryClient.prefetchQuery({ queryKey: Common.UseAgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdKeyFn({ appName, sessionId }), queryFn: () => AgentsService.getApiV1AgentsByAppNameSessionBySessionId({ appName, sessionId }) });
export const prefetchUseDefaultServiceGet = (queryClient: QueryClient) => queryClient.prefetchQuery({ queryKey: Common.UseDefaultServiceGetKeyFn(), queryFn: () => DefaultService.get() });
