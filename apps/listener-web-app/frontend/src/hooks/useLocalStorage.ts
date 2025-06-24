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

import {useCallback, useState} from "react";

const getLocalStorageValue = <T>(key: string, initValue: T): T => {
  const item = localStorage.getItem(key);
  return item ? JSON.parse(item) satisfies T : initValue;
};

export const useLocalStorage = <T>(key: string, initValue: T) => {
  const [value, setValue] = useState(() =>
    getLocalStorageValue(key, initValue)
  );

  const setLocalStorageValue = useCallback(
    (setStateAction: T | ((prevState: T) => T)) => {
      const newValue =
        setStateAction instanceof Function
          ? setStateAction(value)
          : setStateAction;

      localStorage.setItem(key, JSON.stringify(newValue));
      setValue(() => newValue);
    },
    [key, value]
  );

  return [value, setLocalStorageValue] as const;
};