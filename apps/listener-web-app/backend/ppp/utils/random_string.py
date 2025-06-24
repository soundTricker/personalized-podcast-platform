# Copyright 2025 Keisuke Tominaga a.k.a soundTricker
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import secrets
import string


def generate_random_string(length: int = 32) -> str:
    """
    Generate a random string of specified length.
    
    Args:
        length: The length of the random string to generate (default: 32)
        
    Returns:
        A random string containing letters and digits
    """
    if length < 32:
        raise ValueError("Length must be at least 32 characters")
    
    # Use letters and digits for the random string
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))