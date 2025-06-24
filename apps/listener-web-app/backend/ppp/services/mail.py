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

from ppp.models.mail import Mail
from ppp.services.base import BaseService


class MailService(BaseService[Mail]):
    """
    Service for managing mail operations.

    This service provides CRUD operations for Mail model.
    """

    def __init__(self):
        """
        Initialize the MailService with Mail model.
        """
        super().__init__(Mail)

    async def get_mail_by_id(self, mail_id: str) -> Mail | None:
        """
        Get a mail by its ID.

        Args:
            mail_id: The ID of the mail to retrieve.

        Returns:
            The mail instance if found, None otherwise.
        """
        return await self.get_by_id(mail_id)

    async def update_mail_status(self, mail_id: str, status: str, sent_at=None) -> Mail | None:
        """
        Update the status of a mail.

        Args:
            mail_id: The ID of the mail to update.
            status: The new status of the mail.
            sent_at: The timestamp when the mail was sent (optional).

        Returns:
            The updated mail instance if found, None otherwise.
        """
        update_data = {"status": status}
        if sent_at is not None:
            update_data["sent_at"] = sent_at

        return await self.update(mail_id, **update_data)


def get_mail_service() -> MailService:
    """
    Dependency function to get MailService instance.

    Returns:
        MailService instance.
    """
    return MailService()
