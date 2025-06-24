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

// Function to render status badge with appropriate color
import {ProgramStatus} from "@api/requests";
import {Badge} from "flowbite-react";

// Function to convert status to Japanese
const getStatusText = (status: ProgramStatus) => {
    switch (status) {
        case "draft":
            return "下書き";
        case "active":
            return "定義実行中";
        case "pause":
            return "停止中";
        default:
            return status;
    }
};

type ProgramStatusBadgeProp = {
    status: ProgramStatus
}

export default function ProgramStatusBadge({status}: ProgramStatusBadgeProp) {
    let color: string;

    switch (status) {
        case "draft":
            color = "gray";
            break;
        case "active":
            color = "success";
            break;
        case "pause":
            color = "gray"
            break
        default:
            color = "info";
    }

    return <Badge className="inline-block" color={color}>{getStatusText(status)}</Badge>;
};

