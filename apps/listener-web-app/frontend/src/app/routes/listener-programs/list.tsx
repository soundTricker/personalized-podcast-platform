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

import {Link} from "react-router";
import {Button, Card, Table, TableBody, TableCell, TableHead, TableHeadCell, TableRow} from "flowbite-react";
import {useListenerProgramsServiceGetApiV1ListenerPrograms, useListenerProgramsServiceDeleteApiV1ListenerProgramsByListenerProgramId} from "@api/queries";
import {ListenerProgramSchema} from "@api/requests";
import ProgramStatusBadge from "@/components/ProgramStatusBadge.tsx";
import {useState} from "react";

function ListenerProgramsListPage() {
    const [deletingId, setDeletingId] = useState<string | null>(null);

    const {data: programs, isLoading: loading, error, refetch} = useListenerProgramsServiceGetApiV1ListenerPrograms([]);

    const deleteMutation = useListenerProgramsServiceDeleteApiV1ListenerProgramsByListenerProgramId({
        onSuccess: () => {
            setDeletingId(null);
            refetch(); // Refresh the list after successful deletion
        },
        onError: (error) => {
            setDeletingId(null);
            console.error('Failed to delete program:', error);
            // You could add a toast notification here
        }
    });

    const handleDelete = async (programId: string, programTitle: string) => {
        if (window.confirm(`「${programTitle}」を削除してもよろしいですか？この操作は取り消せません。`)) {
            setDeletingId(programId);
            deleteMutation.mutate({ listenerProgramId: programId });
        }
    };

    return (
        <div className="mx-auto px-4 py-8">
            <header className="mb-8 flex justify-between items-center">
                <div>
                    <h1 className="text-3xl font-bold mb-2">マイプログラム</h1>
                    <p className="text-gray-600">あなたが作成したポッドキャストプログラム</p>
                </div>
                <Button as={Link} to="./create">
                    新規プログラム作成
                </Button>
            </header>

            <Card>
                {loading ? (
                    <div className="text-center py-4">読み込み中...</div>
                ) : error ? (
                    <div className="text-red-500 text-center py-4">エラーが発生しました</div>
                ) : programs && programs.length === 0 ? (
                    <div className="text-center py-8">
                        <p className="text-gray-500 mb-4">プログラムがまだありません</p>
                        <Button as={Link} to="./create">
                            最初のプログラムを作成
                        </Button>
                    </div>
                ) : (
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableHeadCell>タイトル</TableHeadCell>
                                <TableHeadCell>説明</TableHeadCell>
                                <TableHeadCell>時間</TableHeadCell>
                                <TableHeadCell>ステータス</TableHeadCell>
                                <TableHeadCell>
                                    <span className="sr-only">アクション</span>
                                </TableHeadCell>
                            </TableRow>
                        </TableHead>
                        <TableBody className="divide-y">
                            {programs && programs.map((program: ListenerProgramSchema) => (
                                <TableRow key={program.id} className="bg-white">
                                    <TableCell className="font-medium text-gray-900">
                                        {program.title}
                                    </TableCell>
                                    <TableCell>
                                        {program.description.length > 50
                                            ? `${program.description.substring(0, 50)}...`
                                            : program.description}
                                    </TableCell>
                                    <TableCell>{program.programMinutes}分</TableCell>
                                    <TableCell>
                                        <ProgramStatusBadge status={program.status}></ProgramStatusBadge>
                                    </TableCell>
                                    <TableCell>
                                        <div className="flex gap-1">
                                            <Button size="sm" color="light" as={Link} to={`/listener-programs/${program.id}`}>
                                                詳細
                                            </Button>
                                            <Button size="sm" color="light" as={Link} to={`/listener-programs/${program.id}/edit`}>
                                                編集
                                            </Button>
                                            <Button 
                                                size="sm" 
                                                color="failure" 
                                                onClick={() => program.id && handleDelete(program.id, program.title)}
                                                disabled={deletingId === program.id || !program.id}
                                            >
                                                {deletingId === program.id ? '削除中...' : '削除'}
                                            </Button>
                                        </div>
                                    </TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                )}
            </Card>
        </div>
    );
}

export default function ListenerProgramsList() {
    return (
        <ListenerProgramsListPage />
    );
}

export function meta() {
    return [
        {title: "マイプログラム - Personalized Podcast Platform"},
        {name: "description", content: "あなたが作成したポッドキャストプログラムの一覧"},
    ];
}
