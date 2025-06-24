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

import { useState } from 'react';
import { Button, Card, Label, TextInput, Alert } from 'flowbite-react';
import { useAuth } from '@/firebase/auth';
import { useNavigate, Link } from 'react-router';
import { FcGoogle } from 'react-icons/fc';
import { useListenersServicePostApiV1ListenersSignup } from '@api/queries';

function SignupPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { signUpWithEmail, signInWithGoogle, currentUser } = useAuth();
  const navigate = useNavigate();
  const signupMutation = useListenersServicePostApiV1ListenersSignup({
    onSuccess: () => navigate('/'),
    onError: error => {
      console.error(error);
      setError('バックエンドでのアカウント作成に失敗しました。もう一度お試しください。');
    }
  });

  if (currentUser) {
    navigate('/');
    return;
  }

  const handleEmailSignup = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    // パスワードの確認
    if (password !== confirmPassword) {
      setError('パスワードが一致しません。');
      return;
    }

    setLoading(true);

    try {
      // Firebase認証
      await signUpWithEmail(email, password);
      await signupMutation.mutateAsync({requestBody: {}});
    } catch (err: any) {
      // Firebase エラーメッセージをユーザーフレンドリーなメッセージに変換
      if (err.code === 'auth/email-already-in-use') {
        setError('このメールアドレスは既に使用されています。');
      } else if (err.code === 'auth/invalid-email') {
        setError('有効なメールアドレスを入力してください。');
      } else if (err.code === 'auth/weak-password') {
        setError('パスワードは6文字以上である必要があります。');
      } else {
        setError('アカウント作成に失敗しました。もう一度お試しください。');
      }
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleSignup = async () => {
    setError('');
    setLoading(true);

    try {
      // Firebase認証
      await signInWithGoogle();
      await signupMutation.mutateAsync({requestBody: {}});
    } catch (err) {
      setError('Googleでのアカウント作成に失敗しました。');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex justify-center items-center py-12">
      <Card className="w-full max-w-md">
        <h2 className="text-2xl font-bold text-center mb-6">アカウント作成</h2>

        {error && (
          <Alert color="failure" className="mb-4">
            {error}
          </Alert>
        )}

        <form onSubmit={handleEmailSignup} className="flex flex-col gap-4">
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

          <div>
            <div className="mb-2 block">
              <Label htmlFor="confirmPassword">パスワード（確認）</Label>
            </div>
            <TextInput
              id="confirmPassword"
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />
          </div>

          <Button type="submit" disabled={loading}>
            {loading ? 'アカウント作成中...' : 'アカウント作成'}
          </Button>
        </form>

        <div className="my-4 flex items-center before:mt-0.5 before:flex-1 before:border-t before:border-gray-300 after:mt-0.5 after:flex-1 after:border-t after:border-gray-300">
          <p className="mx-4 mb-0 text-center font-medium text-gray-500">または</p>
        </div>

        <Button color="light" onClick={handleGoogleSignup} disabled={loading}>
          <FcGoogle className="mr-2 h-5 w-5" />
          Googleでアカウント作成
        </Button>

        <div className="mt-4 text-center">
          <p>
            既にアカウントをお持ちの方は{' '}
            <Link to="/login" className="text-blue-600 hover:underline">
              こちら
            </Link>
          </p>
        </div>
      </Card>
    </div>
  );
}

export default function Signup() {
  return (
    <SignupPage />
  );
}

export function meta() {
  return [
    { title: "Personalized Podcast Platform - アカウント作成" },
    { name: "description", content: "PPPに新規登録してパーソナライズされたポッドキャストを楽しもう" },
  ];
}
