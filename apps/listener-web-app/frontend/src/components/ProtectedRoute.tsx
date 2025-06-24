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

import {useEffect} from 'react';
import {Outlet, useLocation, useNavigate} from 'react-router';
import {useAuth} from '@/firebase/auth';

type ProtectedRouteProps = {
    children: React.ReactNode;
};

/**
 * A component that protects routes by checking if the user is authenticated.
 * If the user is not authenticated, they will be redirected to the login page.
 */
export default function ProtectedRoute({}: ProtectedRouteProps) {
    const {currentUser, loading} = useAuth();
    const location = useLocation();
    const navigate = useNavigate();

    useEffect(() => {
        if (!loading && !currentUser) {
            console.log("not logged in , redirect to login")
            navigate('/login', {state: {from: location.pathname }});
        }
    }, [currentUser, loading, navigate]);

    // Don't render anything while checking authentication
    if (loading) {
        return <div className="flex justify-center items-center h-64">読み込み中...</div>;
    }

    // If user is authenticated, render the children
    return currentUser ? <>
        <Outlet/>
    </> : null;
}
