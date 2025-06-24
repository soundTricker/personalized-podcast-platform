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

import {useState} from 'react';
import {Button, Card, Label, TextInput, Alert} from 'flowbite-react';
import {useAuth} from '@/firebase/auth';
import {useNavigate, Link} from 'react-router';
import {FcGoogle} from 'react-icons/fc';
import {ListenersService} from '@api/requests/services.gen';

function LoginPage() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const {signInWithEmail, signInWithGoogle} = useAuth();
    const navigate = useNavigate();

    const handleEmailLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            await signInWithEmail(email, password);
            await ListenersService.getApiV1ListenersMe().catch(async () => {
                await ListenersService.postApiV1ListenersSignup();
            });

            navigate('/');
        } catch (err) {
            setError('ログインに失敗しました。メールアドレスとパスワードを確認してください。');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleGoogleLogin = async () => {
        setError('');
        setLoading(true);

        try {
            await signInWithGoogle();
            await ListenersService.getApiV1ListenersMe().catch(async () => {
                await ListenersService.postApiV1ListenersSignup();
            });

            navigate('/');
        } catch (err) {
            setError('Googleログインに失敗しました。');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="flex justify-center items-center py-12">
            <Card className="w-full max-w-md">
                <h2 className="text-2xl font-bold text-center mb-6">ログイン</h2>

                {error && (
                    <Alert color="failure" className="mb-4">
                        {error}
                    </Alert>
                )}

                <form onSubmit={handleEmailLogin} className="flex flex-col gap-4">
                    <div>
                        <div className="mb-2 block">
                            <Label htmlFor="email">メールアドレス</Label>
                        </div>
                        <TextInput
                            id="email"
                            type="email"
                            placeholder="name@example.com"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>

                    <div>
                        <div className="mb-2 block">
                            <Label htmlFor="password">パスワード</Label>
                        </div>
                        <TextInput
                            id="password"
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </div>

                    <Button type="submit" disabled={loading}>
                        {loading ? 'ログイン中...' : 'ログイン'}
                    </Button>
                </form>

                <div
                    className="my-4 flex items-center before:mt-0.5 before:flex-1 before:border-t before:border-gray-300 after:mt-0.5 after:flex-1 after:border-t after:border-gray-300">
                    <p className="mx-4 mb-0 text-center font-medium text-gray-500">または</p>
                </div>

                <Button color="light" onClick={handleGoogleLogin} disabled={loading}>
                    <FcGoogle className="mr-2 h-5 w-5"/>
                    Googleでログイン
                </Button>

                <div className="mt-4 text-center">
                    <p>
                        アカウントをお持ちでない方は{' '}
                        <Link to="/signup" className="text-blue-600 hover:underline">
                            新規ユーザ登録
                        </Link>
                    </p>
                </div>
            </Card>
        </div>
    );
}

export default function Login() {
    return (
        <LoginPage/>
    );
}

export function meta() {
    return [
        {title: "Personalized Podcast Platform - ログイン"},
        {name: "description", content: "PPPにログインしてパーソナライズされたポッドキャストを楽しもう"},
    ];
}
