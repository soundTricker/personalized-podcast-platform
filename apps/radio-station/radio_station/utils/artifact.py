# Copyright 2025 Keisuke Tominaga a.k.a soundTricker
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents.invocation_context import InvocationContext
from google.genai import types


async def save_artifact(ctx: InvocationContext, filename: str, part: types.Part) -> int | None:
    if ctx.artifact_service:
        return await ctx.artifact_service.save_artifact(
            app_name=ctx.session.app_name,
            user_id=ctx.session.user_id,
            session_id=ctx.session.id,
            filename=filename,
            artifact=part,
        )
    return None


async def load_artifact(ctx: InvocationContext, filename: str) -> types.Part | None:
    if ctx.artifact_service:
        return await ctx.artifact_service.load_artifact(
            app_name=ctx.session.app_name,
            user_id=ctx.session.user_id,
            session_id=ctx.session.id,
            filename=filename,
        )
    return None


async def delete_artifact(ctx: InvocationContext, filename: str) -> None:
    if ctx.artifact_service:
        return await ctx.artifact_service.delete_artifact(
            app_name=ctx.session.app_name,
            user_id=ctx.session.user_id,
            session_id=ctx.session.id,
            filename=filename,
        )
    return None


async def list_artifact(ctx: InvocationContext) -> list[str]:
    if ctx.artifact_service:
        return await ctx.artifact_service.list_artifact_keys(app_name=ctx.session.app_name, user_id=ctx.session.user_id, session_id=ctx.session.id)
    return []
