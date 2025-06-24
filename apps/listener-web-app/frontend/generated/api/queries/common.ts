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

import { UseQueryResult } from "@tanstack/react-query";
import { AgentsService, DefaultService, GoogleOauth2Service, ListenerProgramSegmentsService, ListenerProgramsService, ListenersService, PodcastService, ProgramBroadcastHistoryService, RadioCastsService } from "../requests/services.gen";
export type ListenersServiceGetApiV1ListenersMeDefaultResponse = Awaited<ReturnType<typeof ListenersService.getApiV1ListenersMe>>;
export type ListenersServiceGetApiV1ListenersMeQueryResult<TData = ListenersServiceGetApiV1ListenersMeDefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const useListenersServiceGetApiV1ListenersMeKey = "ListenersServiceGetApiV1ListenersMe";
export const UseListenersServiceGetApiV1ListenersMeKeyFn = (queryKey?: Array<unknown>) => [useListenersServiceGetApiV1ListenersMeKey, ...(queryKey ?? [])];
export type ListenerProgramsServiceGetApiV1ListenerProgramsDefaultResponse = Awaited<ReturnType<typeof ListenerProgramsService.getApiV1ListenerPrograms>>;
export type ListenerProgramsServiceGetApiV1ListenerProgramsQueryResult<TData = ListenerProgramsServiceGetApiV1ListenerProgramsDefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const useListenerProgramsServiceGetApiV1ListenerProgramsKey = "ListenerProgramsServiceGetApiV1ListenerPrograms";
export const UseListenerProgramsServiceGetApiV1ListenerProgramsKeyFn = (queryKey?: Array<unknown>) => [useListenerProgramsServiceGetApiV1ListenerProgramsKey, ...(queryKey ?? [])];
export type ListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramIdDefaultResponse = Awaited<ReturnType<typeof ListenerProgramsService.getApiV1ListenerProgramsByListenerProgramId>>;
export type ListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramIdQueryResult<TData = ListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramIdDefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const useListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramIdKey = "ListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramId";
export const UseListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramIdKeyFn = ({ listenerProgramId }: {
  listenerProgramId: string;
}, queryKey?: Array<unknown>) => [useListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramIdKey, ...(queryKey ?? [{ listenerProgramId }])];
export type ListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegmentsDefaultResponse = Awaited<ReturnType<typeof ListenerProgramSegmentsService.getApiV1ListenerProgramsByProgramIdSegments>>;
export type ListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegmentsQueryResult<TData = ListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegmentsDefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const useListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegmentsKey = "ListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegments";
export const UseListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegmentsKeyFn = ({ programId }: {
  programId: string;
}, queryKey?: Array<unknown>) => [useListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegmentsKey, ...(queryKey ?? [{ programId }])];
export type ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryDefaultResponse = Awaited<ReturnType<typeof ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistory>>;
export type ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryQueryResult<TData = ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryDefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const useProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryKey = "ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistory";
export const UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryKeyFn = ({ programId }: {
  programId: string;
}, queryKey?: Array<unknown>) => [useProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryKey, ...(queryKey ?? [{ programId }])];
export type ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdDefaultResponse = Awaited<ReturnType<typeof ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryId>>;
export type ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdQueryResult<TData = ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdDefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const useProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdKey = "ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryId";
export const UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdKeyFn = ({ broadcastHistoryId, programId }: {
  broadcastHistoryId: string;
  programId: string;
}, queryKey?: Array<unknown>) => [useProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdKey, ...(queryKey ?? [{ broadcastHistoryId, programId }])];
export type ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudioDefaultResponse = Awaited<ReturnType<typeof ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudio>>;
export type ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudioQueryResult<TData = ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudioDefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const useProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudioKey = "ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudio";
export const UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudioKeyFn = ({ broadcastHistoryId, programId }: {
  broadcastHistoryId: string;
  programId: string;
}, queryKey?: Array<unknown>) => [useProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudioKey, ...(queryKey ?? [{ broadcastHistoryId, programId }])];
export type RadioCastsServiceGetApiV1RadioCastsDefaultResponse = Awaited<ReturnType<typeof RadioCastsService.getApiV1RadioCasts>>;
export type RadioCastsServiceGetApiV1RadioCastsQueryResult<TData = RadioCastsServiceGetApiV1RadioCastsDefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const useRadioCastsServiceGetApiV1RadioCastsKey = "RadioCastsServiceGetApiV1RadioCasts";
export const UseRadioCastsServiceGetApiV1RadioCastsKeyFn = ({ radioCastIds }: {
  radioCastIds?: string[];
} = {}, queryKey?: Array<unknown>) => [useRadioCastsServiceGetApiV1RadioCastsKey, ...(queryKey ?? [{ radioCastIds }])];
export type RadioCastsServiceGetApiV1RadioCastsByRadioCastIdDefaultResponse = Awaited<ReturnType<typeof RadioCastsService.getApiV1RadioCastsByRadioCastId>>;
export type RadioCastsServiceGetApiV1RadioCastsByRadioCastIdQueryResult<TData = RadioCastsServiceGetApiV1RadioCastsByRadioCastIdDefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const useRadioCastsServiceGetApiV1RadioCastsByRadioCastIdKey = "RadioCastsServiceGetApiV1RadioCastsByRadioCastId";
export const UseRadioCastsServiceGetApiV1RadioCastsByRadioCastIdKeyFn = ({ radioCastId }: {
  radioCastId: string;
}, queryKey?: Array<unknown>) => [useRadioCastsServiceGetApiV1RadioCastsByRadioCastIdKey, ...(queryKey ?? [{ radioCastId }])];
export type PodcastServiceGetApiV1PodcastRssByProgramIdDefaultResponse = Awaited<ReturnType<typeof PodcastService.getApiV1PodcastRssByProgramId>>;
export type PodcastServiceGetApiV1PodcastRssByProgramIdQueryResult<TData = PodcastServiceGetApiV1PodcastRssByProgramIdDefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const usePodcastServiceGetApiV1PodcastRssByProgramIdKey = "PodcastServiceGetApiV1PodcastRssByProgramId";
export const UsePodcastServiceGetApiV1PodcastRssByProgramIdKeyFn = ({ privateKey, programId }: {
  privateKey?: string;
  programId: string;
}, queryKey?: Array<unknown>) => [usePodcastServiceGetApiV1PodcastRssByProgramIdKey, ...(queryKey ?? [{ privateKey, programId }])];
export type PodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryIdDefaultResponse = Awaited<ReturnType<typeof PodcastService.getApiV1PodcastAudioByProgramIdByBroadcastHistoryId>>;
export type PodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryIdQueryResult<TData = PodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryIdDefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const usePodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryIdKey = "PodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryId";
export const UsePodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryIdKeyFn = ({ broadcastHistoryId, privateKey, programId }: {
  broadcastHistoryId: string;
  privateKey?: string;
  programId: string;
}, queryKey?: Array<unknown>) => [usePodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryIdKey, ...(queryKey ?? [{ broadcastHistoryId, privateKey, programId }])];
export type GoogleOauth2ServiceGetApiV1GoogleOauth2DefaultResponse = Awaited<ReturnType<typeof GoogleOauth2Service.getApiV1GoogleOauth2>>;
export type GoogleOauth2ServiceGetApiV1GoogleOauth2QueryResult<TData = GoogleOauth2ServiceGetApiV1GoogleOauth2DefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const useGoogleOauth2ServiceGetApiV1GoogleOauth2Key = "GoogleOauth2ServiceGetApiV1GoogleOauth2";
export const UseGoogleOauth2ServiceGetApiV1GoogleOauth2KeyFn = ({ scopes }: {
  scopes: string[];
}, queryKey?: Array<unknown>) => [useGoogleOauth2ServiceGetApiV1GoogleOauth2Key, ...(queryKey ?? [{ scopes }])];
export type GoogleOauth2ServiceGetApiV1GoogleOauth2CallbackDefaultResponse = Awaited<ReturnType<typeof GoogleOauth2Service.getApiV1GoogleOauth2Callback>>;
export type GoogleOauth2ServiceGetApiV1GoogleOauth2CallbackQueryResult<TData = GoogleOauth2ServiceGetApiV1GoogleOauth2CallbackDefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const useGoogleOauth2ServiceGetApiV1GoogleOauth2CallbackKey = "GoogleOauth2ServiceGetApiV1GoogleOauth2Callback";
export const UseGoogleOauth2ServiceGetApiV1GoogleOauth2CallbackKeyFn = ({ code, state }: {
  code: string;
  state: string;
}, queryKey?: Array<unknown>) => [useGoogleOauth2ServiceGetApiV1GoogleOauth2CallbackKey, ...(queryKey ?? [{ code, state }])];
export type AgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdDefaultResponse = Awaited<ReturnType<typeof AgentsService.getApiV1AgentsByAppNameSessionBySessionId>>;
export type AgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdQueryResult<TData = AgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdDefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const useAgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdKey = "AgentsServiceGetApiV1AgentsByAppNameSessionBySessionId";
export const UseAgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdKeyFn = ({ appName, sessionId }: {
  appName: string;
  sessionId: string;
}, queryKey?: Array<unknown>) => [useAgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdKey, ...(queryKey ?? [{ appName, sessionId }])];
export type DefaultServiceGetDefaultResponse = Awaited<ReturnType<typeof DefaultService.get>>;
export type DefaultServiceGetQueryResult<TData = DefaultServiceGetDefaultResponse, TError = unknown> = UseQueryResult<TData, TError>;
export const useDefaultServiceGetKey = "DefaultServiceGet";
export const UseDefaultServiceGetKeyFn = (queryKey?: Array<unknown>) => [useDefaultServiceGetKey, ...(queryKey ?? [])];
export type ListenersServicePostApiV1ListenersSignupMutationResult = Awaited<ReturnType<typeof ListenersService.postApiV1ListenersSignup>>;
export type ListenerProgramsServicePostApiV1ListenerProgramsMutationResult = Awaited<ReturnType<typeof ListenerProgramsService.postApiV1ListenerPrograms>>;
export type ListenerProgramsServicePostApiV1ListenerProgramsByListenerProgramIdGeneratePodcastMutationResult = Awaited<ReturnType<typeof ListenerProgramsService.postApiV1ListenerProgramsByListenerProgramIdGeneratePodcast>>;
export type ProgramBroadcastHistoryServicePostApiV1ListenerProgramsByProgramIdBroadcastHistoryMutationResult = Awaited<ReturnType<typeof ProgramBroadcastHistoryService.postApiV1ListenerProgramsByProgramIdBroadcastHistory>>;
export type ProgramBroadcastHistoryServicePostApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdGeneratePodcastMutationResult = Awaited<ReturnType<typeof ProgramBroadcastHistoryService.postApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdGeneratePodcast>>;
export type RadioCastsServicePostApiV1RadioCastsMutationResult = Awaited<ReturnType<typeof RadioCastsService.postApiV1RadioCasts>>;
export type AgentsServicePostApiV1AgentsByAppNameSessionMutationResult = Awaited<ReturnType<typeof AgentsService.postApiV1AgentsByAppNameSession>>;
export type AgentsServicePostApiV1AgentsChatMutationResult = Awaited<ReturnType<typeof AgentsService.postApiV1AgentsChat>>;
export type ListenerProgramsServicePutApiV1ListenerProgramsByListenerProgramIdMutationResult = Awaited<ReturnType<typeof ListenerProgramsService.putApiV1ListenerProgramsByListenerProgramId>>;
export type ListenerProgramSegmentsServicePutApiV1ListenerProgramsByProgramIdSegmentsMutationResult = Awaited<ReturnType<typeof ListenerProgramSegmentsService.putApiV1ListenerProgramsByProgramIdSegments>>;
export type ProgramBroadcastHistoryServicePutApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdMutationResult = Awaited<ReturnType<typeof ProgramBroadcastHistoryService.putApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryId>>;
export type RadioCastsServicePutApiV1RadioCastsByRadioCastIdMutationResult = Awaited<ReturnType<typeof RadioCastsService.putApiV1RadioCastsByRadioCastId>>;
export type ListenerProgramsServiceDeleteApiV1ListenerProgramsByListenerProgramIdMutationResult = Awaited<ReturnType<typeof ListenerProgramsService.deleteApiV1ListenerProgramsByListenerProgramId>>;
export type ProgramBroadcastHistoryServiceDeleteApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdMutationResult = Awaited<ReturnType<typeof ProgramBroadcastHistoryService.deleteApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryId>>;
export type RadioCastsServiceDeleteApiV1RadioCastsByRadioCastIdMutationResult = Awaited<ReturnType<typeof RadioCastsService.deleteApiV1RadioCastsByRadioCastId>>;
