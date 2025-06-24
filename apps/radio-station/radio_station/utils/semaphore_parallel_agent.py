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

import asyncio
from typing import AsyncGenerator

from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from pydantic import Field


def _set_branch_for_current_agent(
    current_agent: BaseAgent, invocation_context: InvocationContext
):
  invocation_context.branch = (
      f"{invocation_context.branch}.{current_agent.name}"
      if invocation_context.branch
      else current_agent.name
  )

async def _merge_agent_run(
    agents: list[BaseAgent],
    ctx: InvocationContext,
    concurrency: int,
) -> AsyncGenerator[Event, None]:
    """Merges the agent run event generator.

    This implementation guarantees for each agent, it won't move on until the
    generated event is processed by upstream runner.

    Args:
        agent_runs: A list of async generators that yield events from each agent.
        concurrency: concurrency

    Yields:
        Event: The next event from the merged generator.
    """

    async def agent_run(agent: BaseAgent, semaphore: asyncio.Semaphore):
        async with semaphore:
            return agent.run_async(ctx)

    async def agent_event_run(agent_run: AsyncGenerator[Event, None], semaphore: asyncio.Semaphore):
        async with semaphore:
            return await agent_run.__anext__()

    semaphore = asyncio.Semaphore(concurrency)
    agent_runs = [await agent_run(agent, semaphore) for agent in agents]
    tasks = [asyncio.create_task(agent_event_run(a, semaphore)) for a in agent_runs]
    pending_tasks = set(tasks)

    while pending_tasks:
        done, pending_tasks = await asyncio.wait(pending_tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            try:
                yield task.result()

                # Find the generator that produced this event and move it on.
                for i, original_task in enumerate(tasks):
                    if task == original_task:
                        new_task = asyncio.create_task(agent_event_run(agent_runs[i], semaphore))
                        tasks[i] = new_task
                        pending_tasks.add(new_task)
                        break  # stop iterating once found

            except StopAsyncIteration:
                continue


class SemaphoreParallelAgent(BaseAgent):
    concurrency: int = Field(description="Concurrency", default=5)

    def __init__(self, concurrency=5, **kwargs):
        super().__init__(concurrency=concurrency, **kwargs)

    async def _run_async_impl(
      self, ctx: InvocationContext
  ) -> AsyncGenerator[Event, None]:
        _set_branch_for_current_agent(self, ctx)
        async for event in _merge_agent_run(self.sub_agents, ctx, self.concurrency):
            yield event

