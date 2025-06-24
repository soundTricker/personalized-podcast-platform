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

import {
  Button,
  Label,
  TextInput,
  Textarea,
  Select,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  HelperText
} from "flowbite-react";
import { useForm } from "@tanstack/react-form";
import { z } from "zod";
import { RadioCastCreateSchema, RadioCastRole } from "@api/requests/types.gen";

// Voice name options with descriptions
const VOICE_NAME_OPTIONS = {
  "Bright": "明るい",
  "Upbeat": "アップビートな",
  "Informative": "情報通な",
  "Firm": "しっかりした",
  "Excitable": "エキサイティングな",
  "Youthful": "若々しい",
  "Breezy": "軽快な",
  "Easy-going": "のんびりした",
  "Breathy": "息遣いの感じられる",
  "Clear": "クリアな",
  "Smooth": "スムーズな",
  "Gravelly": "しゃがれた",
  "Soft": "ソフトな",
  "Even": "落ち着いた",
  "Mature": "成熟した",
  "Forward": "積極的な",
  "Friendly": "フレンドリーな",
  "Casual": "カジュアルな",
  "Gentle": "優しい",
  "Lively": "生き生きとした",
  "Knowledgeable": "知識豊富な",
  "Warm": "温かい",
};

// Form schema definition
const formSchema = z.object({
  name: z.string().min(1, "名前は必須です"),
  role: z.nativeEnum(RadioCastRole),
  voiceName: z.string().min(1, "声の名前は必須です"),
  personality: z.string().optional(),
});

type FormValues = z.infer<typeof formSchema>;

// Props for the RadioCastCreateModal component
interface RadioCastCreateModalProps {
  // Whether the modal is visible
  show: boolean;
  // Callback when the modal is closed
  onClose: () => void;
  // Callback when a radio cast is created
  onCreateRadioCast: (radioCast: RadioCastCreateSchema) => void;
  // Whether the creation is in progress
  isCreating: boolean;
  // Initial values for the form
  initialValues?: Partial<RadioCastCreateSchema>;
}

/**
 * Modal component for creating a new radio cast
 */
export function RadioCastCreateModal({
  show,
  onClose,
  onCreateRadioCast,
  isCreating,
  initialValues
}: RadioCastCreateModalProps) {
  // Default form values
  const defaultValues: FormValues = {
    name: initialValues?.name || '',
    role: initialValues?.role || RadioCastRole.RADIO_PERSONALITY,
    voiceName: initialValues?.voiceName || '',
    personality: initialValues?.personality || '',
  };

  // Initialize TanStack Form
  const form = useForm({
    defaultValues,
    onSubmit: ({ value }) => {
      onCreateRadioCast(value as RadioCastCreateSchema);
    },
  });

  return (
    <Modal show={show} onClose={onClose}>
      <ModalHeader>ラジオキャスト作成</ModalHeader>
      <ModalBody>
        <form
          className="space-y-4"
          onSubmit={(e) => {
            e.preventDefault();
            e.stopPropagation();
            form.handleSubmit();
          }}
        >
          {form.Field({
            name: "name",
            children: (field) => (
              <div>
                <div className="mb-2 block">
                  <Label htmlFor={field.name}>名前</Label>
                </div>
                <TextInput
                  id={field.name}
                  name={field.name}
                  value={field.state.value}
                  onChange={(e) => field.handleChange(e.target.value)}
                  placeholder="ラジオキャストの名前を入力"
                  required
                />
                {field.state.meta.errors && (
                  <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                )}
              </div>
            )
          })}

          {form.Field({
            name: "role",
            children: (field) => (
              <div>
                <div className="mb-2 block">
                  <Label htmlFor={field.name}>役割</Label>
                </div>
                <Select 
                  id={field.name} 
                  name={field.name}
                  value={field.state.value}
                  onChange={(e) => field.handleChange(e.target.value)}
                  required
                >
                  <option value={RadioCastRole.RADIO_PERSONALITY}>ラジオパーソナリティ</option>
                  <option value={RadioCastRole.ASSISTANT}>アシスタント</option>
                  <option value={RadioCastRole.GUEST}>ゲスト</option>
                </Select>
                {field.state.meta.errors && (
                  <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                )}
              </div>
            )
          })}

          {form.Field({
            name: "voiceName",
            children: (field) => (
              <div>
                <div className="mb-2 block">
                  <Label htmlFor={field.name}>声の名前</Label>
                </div>
                <Select
                  id={field.name}
                  name={field.name}
                  value={field.state.value}
                  onChange={(e) => field.handleChange(e.target.value)}
                  required
                >
                  <option value="">選択してください</option>
                  {Object.entries(VOICE_NAME_OPTIONS).map(([value, description]) => (
                    <option key={value} value={value}>
                      {value}: {description}
                    </option>
                  ))}
                </Select>
                <HelperText className="mt-1">
                    どのような音声かは<a className="font-medium text-blue-600 dark:text-blue-500 hover:underline" href="https://aistudio.google.com/generate-speech" target="_blank">AI Studio</a>か<a className="font-medium text-blue-600 dark:text-blue-500 hover:underline" href="https://cloud.google.com/text-to-speech/docs/chirp3-hd?hl=en" target="_blank">Chirp 3サイト</a>から確認してください。
                </HelperText>
                {field.state.meta.errors && (
                  <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                )}
              </div>
            )
          })}

          {form.Field({
            name: "personality",
            children: (field) => (
              <div>
                <div className="mb-2 block">
                  <Label htmlFor={field.name}>性格</Label>
                </div>
                <Textarea
                  id={field.name}
                  name={field.name}
                  value={field.state.value || ''}
                  onChange={(e) => field.handleChange(e.target.value)}
                  placeholder="性格の特徴を入力"
                  rows={3}
                />
                <HelperText className="mt-1">
                    例:<br/>
                    <ul className="list-disc list-inside ml-2">
                      <li>明るく陽気だけど丁寧な話し方 少し早口 でもしっかり司会進行をする</li>
                      <li>事実を秘書風に淡々と説明する</li>
                      <li>静かな声でゆっくりと丁寧に話す</li>
                    </ul>
                </HelperText>
                {field.state.meta.errors && (
                  <div className="text-red-500 text-sm mt-1">{field.state.meta.errors}</div>
                )}
              </div>
            )
          })}
        </form>
      </ModalBody>
      <ModalFooter>
          <div className="grow"></div>
          <Button color="gray" onClick={onClose}>
            キャンセル
          </Button>
          <Button onClick={() => form.handleSubmit()} disabled={isCreating}>
            {isCreating ? "登録中..." : "登録"}
          </Button>
      </ModalFooter>
    </Modal>
  );
}
