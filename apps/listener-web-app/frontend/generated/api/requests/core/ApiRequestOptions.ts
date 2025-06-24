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

export type ApiRequestOptions<T = unknown> = {
	readonly body?: any;
	readonly cookies?: Record<string, unknown>;
	readonly errors?: Record<number | string, string>;
	readonly formData?: Record<string, unknown> | any[] | Blob | File;
	readonly headers?: Record<string, unknown>;
	readonly mediaType?: string;
	readonly method:
		| 'DELETE'
		| 'GET'
		| 'HEAD'
		| 'OPTIONS'
		| 'PATCH'
		| 'POST'
		| 'PUT';
	readonly path?: Record<string, unknown>;
	readonly query?: Record<string, unknown>;
	readonly responseHeader?: string;
	readonly responseTransformer?: (data: unknown) => Promise<T>;
	readonly url: string;
};