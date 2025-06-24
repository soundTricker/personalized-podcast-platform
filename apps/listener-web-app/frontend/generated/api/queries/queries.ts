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

import { UseMutationOptions, UseQueryOptions, useMutation, useQuery } from "@tanstack/react-query";
import { AgentsService, DefaultService, GoogleOauth2Service, ListenerProgramSegmentsService, ListenerProgramsService, ListenersService, PodcastService, ProgramBroadcastHistoryService, RadioCastsService } from "../requests/services.gen";
import { AgentRunRequest, ListenerCreateSchema, ListenerProgramCalendarSegmentUpdate, ListenerProgramCreateSchema, ListenerProgramGmailSegmentUpdate, ListenerProgramRSSSegmentUpdate, ListenerProgramUpdateSchema, ListenerProgramWebSegmentUpdate, ProgramBroadcastHistoryCreate, ProgramBroadcastHistoryUpdate, RadioCastCreateSchema, RadioCastUpdateSchema } from "../requests/types.gen";
import * as Common from "./common";
export const useListenersServiceGetApiV1ListenersMe = <TData = Common.ListenersServiceGetApiV1ListenersMeDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>(queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UseListenersServiceGetApiV1ListenersMeKeyFn(queryKey), queryFn: () => ListenersService.getApiV1ListenersMe() as TData, ...options });
export const useListenerProgramsServiceGetApiV1ListenerPrograms = <TData = Common.ListenerProgramsServiceGetApiV1ListenerProgramsDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>(queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UseListenerProgramsServiceGetApiV1ListenerProgramsKeyFn(queryKey), queryFn: () => ListenerProgramsService.getApiV1ListenerPrograms() as TData, ...options });
export const useListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramId = <TData = Common.ListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramIdDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ listenerProgramId }: {
  listenerProgramId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UseListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramIdKeyFn({ listenerProgramId }, queryKey), queryFn: () => ListenerProgramsService.getApiV1ListenerProgramsByListenerProgramId({ listenerProgramId }) as TData, ...options });
export const useListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegments = <TData = Common.ListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegmentsDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ programId }: {
  programId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UseListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegmentsKeyFn({ programId }, queryKey), queryFn: () => ListenerProgramSegmentsService.getApiV1ListenerProgramsByProgramIdSegments({ programId }) as TData, ...options });
export const useProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistory = <TData = Common.ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ programId }: {
  programId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryKeyFn({ programId }, queryKey), queryFn: () => ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistory({ programId }) as TData, ...options });
export const useProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryId = <TData = Common.ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ broadcastHistoryId, programId }: {
  broadcastHistoryId: string;
  programId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdKeyFn({ broadcastHistoryId, programId }, queryKey), queryFn: () => ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryId({ broadcastHistoryId, programId }) as TData, ...options });
export const useProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudio = <TData = Common.ProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudioDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ broadcastHistoryId, programId }: {
  broadcastHistoryId: string;
  programId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudioKeyFn({ broadcastHistoryId, programId }, queryKey), queryFn: () => ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudio({ broadcastHistoryId, programId }) as TData, ...options });
export const useRadioCastsServiceGetApiV1RadioCasts = <TData = Common.RadioCastsServiceGetApiV1RadioCastsDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ radioCastIds }: {
  radioCastIds?: string[];
} = {}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UseRadioCastsServiceGetApiV1RadioCastsKeyFn({ radioCastIds }, queryKey), queryFn: () => RadioCastsService.getApiV1RadioCasts({ radioCastIds }) as TData, ...options });
export const useRadioCastsServiceGetApiV1RadioCastsByRadioCastId = <TData = Common.RadioCastsServiceGetApiV1RadioCastsByRadioCastIdDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ radioCastId }: {
  radioCastId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UseRadioCastsServiceGetApiV1RadioCastsByRadioCastIdKeyFn({ radioCastId }, queryKey), queryFn: () => RadioCastsService.getApiV1RadioCastsByRadioCastId({ radioCastId }) as TData, ...options });
export const usePodcastServiceGetApiV1PodcastRssByProgramId = <TData = Common.PodcastServiceGetApiV1PodcastRssByProgramIdDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ privateKey, programId }: {
  privateKey?: string;
  programId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UsePodcastServiceGetApiV1PodcastRssByProgramIdKeyFn({ privateKey, programId }, queryKey), queryFn: () => PodcastService.getApiV1PodcastRssByProgramId({ privateKey, programId }) as TData, ...options });
export const usePodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryId = <TData = Common.PodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryIdDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ broadcastHistoryId, privateKey, programId }: {
  broadcastHistoryId: string;
  privateKey?: string;
  programId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UsePodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryIdKeyFn({ broadcastHistoryId, privateKey, programId }, queryKey), queryFn: () => PodcastService.getApiV1PodcastAudioByProgramIdByBroadcastHistoryId({ broadcastHistoryId, privateKey, programId }) as TData, ...options });
export const useGoogleOauth2ServiceGetApiV1GoogleOauth2 = <TData = Common.GoogleOauth2ServiceGetApiV1GoogleOauth2DefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ scopes }: {
  scopes: string[];
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UseGoogleOauth2ServiceGetApiV1GoogleOauth2KeyFn({ scopes }, queryKey), queryFn: () => GoogleOauth2Service.getApiV1GoogleOauth2({ scopes }) as TData, ...options });
export const useGoogleOauth2ServiceGetApiV1GoogleOauth2Callback = <TData = Common.GoogleOauth2ServiceGetApiV1GoogleOauth2CallbackDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ code, state }: {
  code: string;
  state: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UseGoogleOauth2ServiceGetApiV1GoogleOauth2CallbackKeyFn({ code, state }, queryKey), queryFn: () => GoogleOauth2Service.getApiV1GoogleOauth2Callback({ code, state }) as TData, ...options });
export const useAgentsServiceGetApiV1AgentsByAppNameSessionBySessionId = <TData = Common.AgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>({ appName, sessionId }: {
  appName: string;
  sessionId: string;
}, queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UseAgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdKeyFn({ appName, sessionId }, queryKey), queryFn: () => AgentsService.getApiV1AgentsByAppNameSessionBySessionId({ appName, sessionId }) as TData, ...options });
export const useDefaultServiceGet = <TData = Common.DefaultServiceGetDefaultResponse, TError = unknown, TQueryKey extends Array<unknown> = unknown[]>(queryKey?: TQueryKey, options?: Omit<UseQueryOptions<TData, TError>, "queryKey" | "queryFn">) => useQuery<TData, TError>({ queryKey: Common.UseDefaultServiceGetKeyFn(queryKey), queryFn: () => DefaultService.get() as TData, ...options });
export const useListenersServicePostApiV1ListenersSignup = <TData = Common.ListenersServicePostApiV1ListenersSignupMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  requestBody?: ListenerCreateSchema;
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  requestBody?: ListenerCreateSchema;
}, TContext>({ mutationFn: ({ requestBody }) => ListenersService.postApiV1ListenersSignup({ requestBody }) as unknown as Promise<TData>, ...options });
export const useListenerProgramsServicePostApiV1ListenerPrograms = <TData = Common.ListenerProgramsServicePostApiV1ListenerProgramsMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  requestBody: ListenerProgramCreateSchema;
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  requestBody: ListenerProgramCreateSchema;
}, TContext>({ mutationFn: ({ requestBody }) => ListenerProgramsService.postApiV1ListenerPrograms({ requestBody }) as unknown as Promise<TData>, ...options });
export const useListenerProgramsServicePostApiV1ListenerProgramsByListenerProgramIdGeneratePodcast = <TData = Common.ListenerProgramsServicePostApiV1ListenerProgramsByListenerProgramIdGeneratePodcastMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  dryRun?: boolean;
  listenerProgramId: string;
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  dryRun?: boolean;
  listenerProgramId: string;
}, TContext>({ mutationFn: ({ dryRun, listenerProgramId }) => ListenerProgramsService.postApiV1ListenerProgramsByListenerProgramIdGeneratePodcast({ dryRun, listenerProgramId }) as unknown as Promise<TData>, ...options });
export const useProgramBroadcastHistoryServicePostApiV1ListenerProgramsByProgramIdBroadcastHistory = <TData = Common.ProgramBroadcastHistoryServicePostApiV1ListenerProgramsByProgramIdBroadcastHistoryMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  programId: string;
  requestBody: ProgramBroadcastHistoryCreate;
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  programId: string;
  requestBody: ProgramBroadcastHistoryCreate;
}, TContext>({ mutationFn: ({ programId, requestBody }) => ProgramBroadcastHistoryService.postApiV1ListenerProgramsByProgramIdBroadcastHistory({ programId, requestBody }) as unknown as Promise<TData>, ...options });
export const useProgramBroadcastHistoryServicePostApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdGeneratePodcast = <TData = Common.ProgramBroadcastHistoryServicePostApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdGeneratePodcastMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  broadcastHistoryId: string;
  dryRun?: boolean;
  programId: string;
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  broadcastHistoryId: string;
  dryRun?: boolean;
  programId: string;
}, TContext>({ mutationFn: ({ broadcastHistoryId, dryRun, programId }) => ProgramBroadcastHistoryService.postApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdGeneratePodcast({ broadcastHistoryId, dryRun, programId }) as unknown as Promise<TData>, ...options });
export const useRadioCastsServicePostApiV1RadioCasts = <TData = Common.RadioCastsServicePostApiV1RadioCastsMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  requestBody: RadioCastCreateSchema;
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  requestBody: RadioCastCreateSchema;
}, TContext>({ mutationFn: ({ requestBody }) => RadioCastsService.postApiV1RadioCasts({ requestBody }) as unknown as Promise<TData>, ...options });
export const useAgentsServicePostApiV1AgentsByAppNameSession = <TData = Common.AgentsServicePostApiV1AgentsByAppNameSessionMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  appName: string;
  requestBody?: { [key: string]: unknown; };
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  appName: string;
  requestBody?: { [key: string]: unknown; };
}, TContext>({ mutationFn: ({ appName, requestBody }) => AgentsService.postApiV1AgentsByAppNameSession({ appName, requestBody }) as unknown as Promise<TData>, ...options });
export const useAgentsServicePostApiV1AgentsChat = <TData = Common.AgentsServicePostApiV1AgentsChatMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  requestBody: AgentRunRequest;
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  requestBody: AgentRunRequest;
}, TContext>({ mutationFn: ({ requestBody }) => AgentsService.postApiV1AgentsChat({ requestBody }) as unknown as Promise<TData>, ...options });
export const useListenerProgramsServicePutApiV1ListenerProgramsByListenerProgramId = <TData = Common.ListenerProgramsServicePutApiV1ListenerProgramsByListenerProgramIdMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  listenerProgramId: string;
  requestBody: ListenerProgramUpdateSchema;
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  listenerProgramId: string;
  requestBody: ListenerProgramUpdateSchema;
}, TContext>({ mutationFn: ({ listenerProgramId, requestBody }) => ListenerProgramsService.putApiV1ListenerProgramsByListenerProgramId({ listenerProgramId, requestBody }) as unknown as Promise<TData>, ...options });
export const useListenerProgramSegmentsServicePutApiV1ListenerProgramsByProgramIdSegments = <TData = Common.ListenerProgramSegmentsServicePutApiV1ListenerProgramsByProgramIdSegmentsMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  programId: string;
  requestBody: (ListenerProgramCalendarSegmentUpdate | ListenerProgramGmailSegmentUpdate | ListenerProgramRSSSegmentUpdate | ListenerProgramWebSegmentUpdate)[];
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  programId: string;
  requestBody: (ListenerProgramCalendarSegmentUpdate | ListenerProgramGmailSegmentUpdate | ListenerProgramRSSSegmentUpdate | ListenerProgramWebSegmentUpdate)[];
}, TContext>({ mutationFn: ({ programId, requestBody }) => ListenerProgramSegmentsService.putApiV1ListenerProgramsByProgramIdSegments({ programId, requestBody }) as unknown as Promise<TData>, ...options });
export const useProgramBroadcastHistoryServicePutApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryId = <TData = Common.ProgramBroadcastHistoryServicePutApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  broadcastHistoryId: string;
  programId: string;
  requestBody: ProgramBroadcastHistoryUpdate;
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  broadcastHistoryId: string;
  programId: string;
  requestBody: ProgramBroadcastHistoryUpdate;
}, TContext>({ mutationFn: ({ broadcastHistoryId, programId, requestBody }) => ProgramBroadcastHistoryService.putApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryId({ broadcastHistoryId, programId, requestBody }) as unknown as Promise<TData>, ...options });
export const useRadioCastsServicePutApiV1RadioCastsByRadioCastId = <TData = Common.RadioCastsServicePutApiV1RadioCastsByRadioCastIdMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  radioCastId: string;
  requestBody: RadioCastUpdateSchema;
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  radioCastId: string;
  requestBody: RadioCastUpdateSchema;
}, TContext>({ mutationFn: ({ radioCastId, requestBody }) => RadioCastsService.putApiV1RadioCastsByRadioCastId({ radioCastId, requestBody }) as unknown as Promise<TData>, ...options });
export const useListenerProgramsServiceDeleteApiV1ListenerProgramsByListenerProgramId = <TData = Common.ListenerProgramsServiceDeleteApiV1ListenerProgramsByListenerProgramIdMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  listenerProgramId: string;
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  listenerProgramId: string;
}, TContext>({ mutationFn: ({ listenerProgramId }) => ListenerProgramsService.deleteApiV1ListenerProgramsByListenerProgramId({ listenerProgramId }) as unknown as Promise<TData>, ...options });
export const useProgramBroadcastHistoryServiceDeleteApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryId = <TData = Common.ProgramBroadcastHistoryServiceDeleteApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  broadcastHistoryId: string;
  programId: string;
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  broadcastHistoryId: string;
  programId: string;
}, TContext>({ mutationFn: ({ broadcastHistoryId, programId }) => ProgramBroadcastHistoryService.deleteApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryId({ broadcastHistoryId, programId }) as unknown as Promise<TData>, ...options });
export const useRadioCastsServiceDeleteApiV1RadioCastsByRadioCastId = <TData = Common.RadioCastsServiceDeleteApiV1RadioCastsByRadioCastIdMutationResult, TError = unknown, TContext = unknown>(options?: Omit<UseMutationOptions<TData, TError, {
  radioCastId: string;
}, TContext>, "mutationFn">) => useMutation<TData, TError, {
  radioCastId: string;
}, TContext>({ mutationFn: ({ radioCastId }) => RadioCastsService.deleteApiV1RadioCastsByRadioCastId({ radioCastId }) as unknown as Promise<TData>, ...options });
