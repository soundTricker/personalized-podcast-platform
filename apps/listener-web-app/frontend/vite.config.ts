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

import {defineConfig} from 'vite';
import tailwindcss from '@tailwindcss/vite';
import {reactRouter} from '@react-router/dev/vite';
import flowbiteReact from "flowbite-react/plugin/vite";
import tsconfigPaths from 'vite-tsconfig-paths';

// https://vitejs.dev/config/
export default defineConfig({
    build: {
        sourcemap: "inline",
        ssr: true
    },
    plugins: [tailwindcss(), reactRouter(), flowbiteReact(), tsconfigPaths()],
    server: {
        port: 3000,
        open: true,
        proxy: {
            '/api/v1': {
                target: 'http://0.0.0.0:8000',
                changeOrigin: true,
            },
            '/apps': {
                target: 'http://0.0.0.0:8004',
                changeOrigin: true,
            },
        },
    }
});