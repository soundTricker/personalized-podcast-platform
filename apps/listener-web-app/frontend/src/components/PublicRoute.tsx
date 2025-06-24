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

import {useAuth} from "@/firebase/auth.tsx";
import {Outlet} from 'react-router';

type PublicRouteProps = {
    children: React.ReactNode;
};

/**
 * A component that redirects authenticated users away from public routes like login.
 * If the user is authenticated, they will be redirected to the home page.
 */
export default function PublicRoute({}: PublicRouteProps) {
    const {loading} = useAuth();

    // Don't render anything while checking authentication
    if (loading) {
        return <div className="flex justify-center items-center h-64">読み込み中...</div>;
    }
    return <><Outlet/></>;
}