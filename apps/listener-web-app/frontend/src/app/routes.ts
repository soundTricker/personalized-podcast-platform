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

import {type RouteConfig, route, index, prefix, layout} from "@react-router/dev/routes";

export default [
    layout("../components/PublicRoute.tsx", [
        index("./routes/home.tsx"), // Root index route
        route("login", "./routes/login.tsx"), // Login page
        route("signup", "./routes/signup.tsx"), // Signup page
        route("about", "./routes/about.tsx"), // About page
        route("oauth2-success", "./routes/oauth2-success.tsx"), // Oauth2 success page
    ]),
    layout('../components/ProtectedRoute.tsx', [
        ...prefix('listener-programs', [
            index("./routes/listener-programs/list.tsx"), // Listener program list
            route("create", "./routes/listener-programs/create.tsx"), // Listener program creation form

            ...prefix(':programId', [
                index("./routes/listener-programs/detail.tsx"), // Listener program detail
                route('edit', "./routes/listener-programs/edit.tsx"), // Listener program edit
                // route("edit", "./routes/listener-programs/edit.tsx"), // Listener program edit form
                route("segments/create", "./routes/listener-programs/segments/create.tsx"), // Listener program segment creation/update form
            ])

        ])
    ]),
] satisfies RouteConfig;
