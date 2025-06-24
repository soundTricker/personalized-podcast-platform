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

import {ReactNode} from "react";
import {Popover} from "flowbite-react";
import {HiQuestionMarkCircle} from "react-icons/hi2";
import {PopoverProps} from "flowbite-react";

type HelpIconProps = {
    header?: ReactNode
    children: ReactNode
    className?: string
} & Omit<PopoverProps, 'trigger'|'content'>;

export const HelpIcon = ({children, header, className, ...props}: HelpIconProps) => {
    const popoverContent = (
        <div className="w-128 text-sm text-gray-500">
            <div className="border-b border-gray-200 bg-gray-100 px-3 py-2">
                <h3 className="font-semibold text-gray-900">{header ? header : 'ヘルプ'}</h3>
            </div>
            <div className="px-3 py-2">
                {children}
            </div>
        </div>
    )


    return (<Popover content={popoverContent} trigger="hover" {...props}>
        <a href="#" className={"text-blue-600 underline hover:no-underline " + className || ''}>
            <HiQuestionMarkCircle className="h-5 w-5 inline-block ml-1 cursor-pointer"></HiQuestionMarkCircle>
        </a>
    </Popover>)
}

export default HelpIcon;