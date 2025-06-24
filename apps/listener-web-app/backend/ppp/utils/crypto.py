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

"""
Utility functions for encryption and decryption using cryptography.fernet.

This module provides functions to encrypt and decrypt sensitive data using AES encryption.
The encryption key is retrieved from the SECRET_KEY environment variable.
"""

import base64
import os
from typing import Optional

from cryptography.fernet import Fernet


def get_encryption_key() -> bytes:
    """
    Get the encryption key from the SECRET_KEY environment variable.

    Returns:
        bytes: The encryption key.

    Raises:
        ValueError: If the SECRET_KEY environment variable is not set.
    """
    secret_key = os.environ.get("SECRET_KEY")
    if not secret_key:
        raise ValueError("SECRET_KEY environment variable is not set")

    # Ensure the key is valid for Fernet (32 url-safe base64-encoded bytes)
    # If the key is not 32 bytes, we'll use it as a seed to generate a valid key
    if len(secret_key) < 32:
        # Pad the key to 32 bytes
        secret_key = secret_key.ljust(32, "0")
    elif len(secret_key) > 32:
        # Truncate the key to 32 bytes
        secret_key = secret_key[:32]

    # Convert to bytes and encode as url-safe base64
    key_bytes = secret_key.encode("utf-8")
    return base64.urlsafe_b64encode(key_bytes)


def encrypt(data: str) -> str:
    """
    Encrypt the given data using AES encryption.

    Args:
        data: The data to encrypt.

    Returns:
        str: The encrypted data as a string.
    """
    if not data:
        return ""

    key = get_encryption_key()
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode("utf-8"))
    return encrypted_data.decode("utf-8")


def decrypt(encrypted_data: str) -> Optional[str]:
    """
    Decrypt the given encrypted data using AES encryption.

    Args:
        encrypted_data: The encrypted data to decrypt.

    Returns:
        Optional[str]: The decrypted data as a string, or None if decryption fails.
    """
    if not encrypted_data:
        return None

    key = get_encryption_key()
    f = Fernet(key)
    try:
        decrypted_data = f.decrypt(encrypted_data.encode("utf-8"))
        return decrypted_data.decode("utf-8")
    except Exception:
        return None
