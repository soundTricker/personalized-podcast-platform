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

from ppp.schemas.listener_program_segment import ListenerProgramSegmentCreateBase, ListenerProgramRSSSegmentCreate, ListenerProgramCalendarSegmentCreate, ListenerProgramWebSegmentCreate, ListenerProgramGmailSegmentCreate

print('=== Base Create Schema ===')
schema = ListenerProgramSegmentCreateBase.model_json_schema()
for field_name, field_info in schema.get('properties', {}).items():
    if 'description' in field_info:
        print(f'{field_name}: {field_info["description"]}')

print('\n=== RSS Create Schema ===')
schema = ListenerProgramRSSSegmentCreate.model_json_schema()
for field_name, field_info in schema.get('properties', {}).items():
    if 'description' in field_info:
        print(f'{field_name}: {field_info["description"]}')

print('\n=== Calendar Create Schema ===')
schema = ListenerProgramCalendarSegmentCreate.model_json_schema()
for field_name, field_info in schema.get('properties', {}).items():
    if 'description' in field_info:
        print(f'{field_name}: {field_info["description"]}')

print('\n=== Web Create Schema ===')
schema = ListenerProgramWebSegmentCreate.model_json_schema()
for field_name, field_info in schema.get('properties', {}).items():
    if 'description' in field_info:
        print(f'{field_name}: {field_info["description"]}')

print('\n=== Gmail Create Schema ===')
schema = ListenerProgramGmailSegmentCreate.model_json_schema()
for field_name, field_info in schema.get('properties', {}).items():
    if 'description' in field_info:
        print(f'{field_name}: {field_info["description"]}')
