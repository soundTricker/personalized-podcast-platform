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

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import EmailStr, Field

from ppp.models.base import BaseModel


class MailStatus(str, Enum):
    """
    Mail status enumeration.
    """

    YET = "yet"
    SENDING = "sending"
    DONE = "done"


class Mail(BaseModel):
    """
    Mail model for storing email information in Firestore.

    This model is used to store email data before sending through Cloud Tasks.
    """

    __collection__ = "mails"

    # Email content
    subject: str = Field(description="Email subject")
    body: str = Field(description="Email body content")
    attachments: List[str] = Field(description="List of GCS URIs for attachments", default_factory=list)

    # Email addresses
    from_email: EmailStr = Field(description="Sender email address", alias="from")
    to: List[EmailStr] = Field(description="List of recipient email addresses")
    cc: List[EmailStr] = Field(description="List of CC email addresses", default_factory=list)

    # Status and timestamp
    status: MailStatus = Field(description="Mail sending status", default=MailStatus.YET)
    sent_at: Optional[datetime] = Field(description="Timestamp when email was sent", default=None)

    @classmethod
    async def send(
        cls,
        subject: str,
        body: str,
        from_email: str,
        to: List[str],
        cc: Optional[List[str]] = None,
        attachments: Optional[List[str]] = None,
    ) -> "Mail":
        """
        Create a mail document and enqueue it for sending via Cloud Tasks.

        Args:
            subject: Email subject
            body: Email body content
            from_email: Sender email address
            to: List of recipient email addresses
            cc: List of CC email addresses (optional)
            attachments: List of GCS URIs for attachments (optional)

        Returns:
            Created Mail instance
        """
        # Create mail document
        mail = cls(
            subject=subject,
            body=body,
            from_email=from_email,
            to=to,
            cc=cc or [],
            attachments=attachments or [],
            status=MailStatus.YET,
        )

        # Save to Firestore
        await mail.save()

        # TODO: Create Cloud Tasks task for async email sending
        # This will be implemented when Cloud Tasks infrastructure is ready

        return mail
