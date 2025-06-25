// generated with @7nohe/openapi-react-query-codegen@1.6.2 

import { type QueryClient } from "@tanstack/react-query";
import { AgentsService, DefaultService, GoogleOauth2Service, ListenerProgramSegmentsService, ListenerProgramsService, ListenersService, PodcastService, ProgramBroadcastHistoryService, RadioCastsService } from "../requests/services.gen";
import * as Common from "./common";
export const ensureUseListenersServiceGetApiV1ListenersMeData = (queryClient: QueryClient) => queryClient.ensureQueryData({ queryKey: Common.UseListenersServiceGetApiV1ListenersMeKeyFn(), queryFn: () => ListenersService.getApiV1ListenersMe() });
export const ensureUseListenerProgramsServiceGetApiV1ListenerProgramsData = (queryClient: QueryClient) => queryClient.ensureQueryData({ queryKey: Common.UseListenerProgramsServiceGetApiV1ListenerProgramsKeyFn(), queryFn: () => ListenerProgramsService.getApiV1ListenerPrograms() });
export const ensureUseListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramIdData = (queryClient: QueryClient, { listenerProgramId }: {
  listenerProgramId: string;
}) => queryClient.ensureQueryData({ queryKey: Common.UseListenerProgramsServiceGetApiV1ListenerProgramsByListenerProgramIdKeyFn({ listenerProgramId }), queryFn: () => ListenerProgramsService.getApiV1ListenerProgramsByListenerProgramId({ listenerProgramId }) });
export const ensureUseListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegmentsData = (queryClient: QueryClient, { programId }: {
  programId: string;
}) => queryClient.ensureQueryData({ queryKey: Common.UseListenerProgramSegmentsServiceGetApiV1ListenerProgramsByProgramIdSegmentsKeyFn({ programId }), queryFn: () => ListenerProgramSegmentsService.getApiV1ListenerProgramsByProgramIdSegments({ programId }) });
export const ensureUseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryData = (queryClient: QueryClient, { programId }: {
  programId: string;
}) => queryClient.ensureQueryData({ queryKey: Common.UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryKeyFn({ programId }), queryFn: () => ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistory({ programId }) });
export const ensureUseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdData = (queryClient: QueryClient, { broadcastHistoryId, programId }: {
  broadcastHistoryId: string;
  programId: string;
}) => queryClient.ensureQueryData({ queryKey: Common.UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdKeyFn({ broadcastHistoryId, programId }), queryFn: () => ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryId({ broadcastHistoryId, programId }) });
export const ensureUseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudioData = (queryClient: QueryClient, { broadcastHistoryId, programId }: {
  broadcastHistoryId: string;
  programId: string;
}) => queryClient.ensureQueryData({ queryKey: Common.UseProgramBroadcastHistoryServiceGetApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudioKeyFn({ broadcastHistoryId, programId }), queryFn: () => ProgramBroadcastHistoryService.getApiV1ListenerProgramsByProgramIdBroadcastHistoryByBroadcastHistoryIdAudio({ broadcastHistoryId, programId }) });
export const ensureUseRadioCastsServiceGetApiV1RadioCastsData = (queryClient: QueryClient, { radioCastIds }: {
  radioCastIds?: string[];
} = {}) => queryClient.ensureQueryData({ queryKey: Common.UseRadioCastsServiceGetApiV1RadioCastsKeyFn({ radioCastIds }), queryFn: () => RadioCastsService.getApiV1RadioCasts({ radioCastIds }) });
export const ensureUseRadioCastsServiceGetApiV1RadioCastsByRadioCastIdData = (queryClient: QueryClient, { radioCastId }: {
  radioCastId: string;
}) => queryClient.ensureQueryData({ queryKey: Common.UseRadioCastsServiceGetApiV1RadioCastsByRadioCastIdKeyFn({ radioCastId }), queryFn: () => RadioCastsService.getApiV1RadioCastsByRadioCastId({ radioCastId }) });
export const ensureUsePodcastServiceGetApiV1PodcastRssByProgramIdData = (queryClient: QueryClient, { privateKey, programId }: {
  privateKey?: string;
  programId: string;
}) => queryClient.ensureQueryData({ queryKey: Common.UsePodcastServiceGetApiV1PodcastRssByProgramIdKeyFn({ privateKey, programId }), queryFn: () => PodcastService.getApiV1PodcastRssByProgramId({ privateKey, programId }) });
export const ensureUsePodcastServiceGetApiV1PodcastCoverByProgramIdData = (queryClient: QueryClient, { privateKey, programId }: {
  privateKey?: string;
  programId: string;
}) => queryClient.ensureQueryData({ queryKey: Common.UsePodcastServiceGetApiV1PodcastCoverByProgramIdKeyFn({ privateKey, programId }), queryFn: () => PodcastService.getApiV1PodcastCoverByProgramId({ privateKey, programId }) });
export const ensureUsePodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryIdData = (queryClient: QueryClient, { broadcastHistoryId, privateKey, programId }: {
  broadcastHistoryId: string;
  privateKey?: string;
  programId: string;
}) => queryClient.ensureQueryData({ queryKey: Common.UsePodcastServiceGetApiV1PodcastAudioByProgramIdByBroadcastHistoryIdKeyFn({ broadcastHistoryId, privateKey, programId }), queryFn: () => PodcastService.getApiV1PodcastAudioByProgramIdByBroadcastHistoryId({ broadcastHistoryId, privateKey, programId }) });
export const ensureUseGoogleOauth2ServiceGetApiV1GoogleOauth2Data = (queryClient: QueryClient, { scopes }: {
  scopes: string[];
}) => queryClient.ensureQueryData({ queryKey: Common.UseGoogleOauth2ServiceGetApiV1GoogleOauth2KeyFn({ scopes }), queryFn: () => GoogleOauth2Service.getApiV1GoogleOauth2({ scopes }) });
export const ensureUseGoogleOauth2ServiceGetApiV1GoogleOauth2CallbackData = (queryClient: QueryClient, { code, state }: {
  code: string;
  state: string;
}) => queryClient.ensureQueryData({ queryKey: Common.UseGoogleOauth2ServiceGetApiV1GoogleOauth2CallbackKeyFn({ code, state }), queryFn: () => GoogleOauth2Service.getApiV1GoogleOauth2Callback({ code, state }) });
export const ensureUseAgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdData = (queryClient: QueryClient, { appName, sessionId }: {
  appName: string;
  sessionId: string;
}) => queryClient.ensureQueryData({ queryKey: Common.UseAgentsServiceGetApiV1AgentsByAppNameSessionBySessionIdKeyFn({ appName, sessionId }), queryFn: () => AgentsService.getApiV1AgentsByAppNameSessionBySessionId({ appName, sessionId }) });
export const ensureUseDefaultServiceGetData = (queryClient: QueryClient) => queryClient.ensureQueryData({ queryKey: Common.UseDefaultServiceGetKeyFn(), queryFn: () => DefaultService.get() });
