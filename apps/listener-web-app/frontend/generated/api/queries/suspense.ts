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

import { UseQueryOptions, useSuspenseQuery } from "@tanstack/react-query";
import { AgentsService, DefaultService, GoogleOauth2Service, ListenerProgramSegmentsService, ListenerProgramsService, ListenersService, PodcastService, ProgramBroadcastHistoryService, RadioCastsService } from "../requests/services.gen";
import * as Common from "./common";
export const useListenersServiceGetApiV1ListenersMeSuspense = <TData = Common.ListenersServiceGetApiV1ListenersMeDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>(queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UseListenersServiceGetApiV1ListenersMeKeyFn(queryKey), queryFn: () => ListenersService.getApiV1ListenersMe() as TData, ...options });
export const useListenerProgramsServiceGetApiV1ListenerProgramsSuspense = <TData = Common.ListenerProgramsServiceGetApiV1ListenerProgramsDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>(queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UseListenerProgramsServiceGetApiV1ListenerProgramsKeyFn(queryKey), queryFn: () => ListenerProgramsService.getApiV1ListenerPrograms() as TData, ...options });
export const useListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramIdSuspense = <TData = Common.ListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramIdDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ listenerProgramId }: {
  listenerProgramId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UseListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramIdKeyFn({ listenerProgramId }, queryKey), queryFn: () => ListenerProgramsService.getApiV1ListenerProgramsByListenerProgramId({ listenerProgramId }) as TData, ...options });
export const useListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegmentsSuspense = <TData = Common.ListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegmentsDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ programId }: {
  programId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UseListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegmentsKeyFn({ programId }, queryKey), queryFn: () => ListenerProgramSegmentsService.getApiV1ListenerProgramsByProgramIdSegments({ programId }) as TData, ...options });
export const useProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistorySuspense = <TData = Common.ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ programId }: {
  programId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryKeyFn({ programId }, queryKey), queryFn: () => ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistory({ programId }) as TData, ...options });
export const useProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdSuspense = <TData = Common.ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ broadcastHistoryId, programId }: {
  broadcastHistoryId: string;
  programId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdKeyFn({ broadcastHistoryId, programId }, queryKey), queryFn: () => ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryId({ broadcastHistoryId, programId }) as TData, ...options });
export const useProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudioSuspense = <TData = Common.ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudioDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ broadcastHistoryId, programId }: {
  broadcastHistoryId: string;
  programId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudioKeyFn({ broadcastHistoryId, programId }, queryKey), queryFn: () => ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudio({ broadcastHistoryId, programId }) as TData, ...options });
export const useRadioCastsServiceGetApiV1RadioCastsSuspense = <TData = Common.RadioCastsServiceGetApiV1RadioCastsDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ radioCastIds }: {
  radioCastIds?: string[];
} = {}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UseRadioCastsServiceGetApiV1RadioCastsKeyFn({ radioCastIds }, queryKey), queryFn: () => RadioCastsService.getApiV1RadioCasts({ radioCastIds }) as TData, ...options });
export const useRadioCastsServiceGetApiV1RadioCastsByRadioCastIdSuspense = <TData = Common.RadioCastsServiceGetApiV1RadioCastsByRadioCastIdDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ radioCastId }: {
  radioCastId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UseRadioCastsServiceGetApiV1RadioCastsByRadioCastIdKeyFn({ radioCastId }, queryKey), queryFn: () => RadioCastsService.getApiV1RadioCastsByRadioCastId({ radioCastId }) as TData, ...options });
export const usePodcastServiceGetApiV1PodcastRssByProgramIdSuspense = <TData = Common.PodcastServiceGetApiV1PodcastRssByProgramIdDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ privateKey, programId }: {
  privateKey?: string;
  programId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UsePodcastServiceGetApiV1PodcastRssByProgramIdKeyFn({ privateKey, programId }, queryKey), queryFn: () => PodcastService.getApiV1PodcastRssByProgramId({ privateKey, programId }) as TData, ...options });
export const usePodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryIdSuspense = <TData = Common.PodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryIdDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ broadcastHistoryId, privateKey, programId }: {
  broadcastHistoryId: string;
  privateKey?: string;
  programId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UsePodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryIdKeyFn({ broadcastHistoryId, privateKey, programId }, queryKey), queryFn: () => PodcastService.getApiV1PodcastAudioByProgramIdByBroadcastHistoryId({ broadcastHistoryId, privateKey, programId }) as TData, ...options });
export const useGoogleOauth2ServiceGetApiV1GoogleOauth2Suspense = <TData = Common.GoogleOauth2ServiceGetApiV1GoogleOauth2DefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ scopes }: {
  scopes: string[];
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UseGoogleOauth2ServiceGetApiV1GoogleOauth2KeyFn({ scopes }, queryKey), queryFn: () => GoogleOauth2Service.getApiV1GoogleOauth2({ scopes }) as TData, ...options });
export const useGoogleOauth2ServiceGetApiV1GoogleOauth2CallbackSuspense = <TData = Common.GoogleOauth2ServiceGetApiV1GoogleOauth2CallbackDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ code, state }: {
  code: string;
  state: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UseGoogleOauth2ServiceGetApiV1GoogleOauth2CallbackKeyFn({ code, state }, queryKey), queryFn: () => GoogleOauth2Service.getApiV1GoogleOauth2Callback({ code, state }) as TData, ...options });
export const useAgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdSuspense = <TData = Common.AgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ appName, sessionId }: {
  appName: string;
  sessionId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UseAgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdKeyFn({ appName, sessionId }, queryKey), queryFn: () => AgentsService.getApiV1AgentsByAppNameSessionBySessionId({ appName, sessionId }) as TData, ...options });
export const useDefaultServiceGetSuspense = <TData = Common.DefaultServiceGetDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>(queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useSuspenseQuery<TData, TError>({ queryKey: Common.UseDefaultServiceGetKeyFn(queryKey), queryFn: () => DefaultService.get() as TData, ...options });
