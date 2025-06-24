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

from typing import Generic, Type, TypeVar

from firedantic import AsyncModel, ModelNotFoundError

# Define type variables for models and schemas
ModelType = TypeVar("ModelType", bound=AsyncModel)


class BaseService(Generic[ModelType]):
    """
    Base service for all services in the application.

    This class provides common CRUD operations for all services.
    """

    def __init__(self, model: Type[ModelType]):
        """
        Initialize the service with a model.

        Args:
            model: The model class to use for CRUD operations.
        """
        self.model = model

    async def get_by_id(self, id: str) -> ModelType | None:
        """
        Get a model instance by ID.

        Args:
            id: The ID of the model instance to get.

        Returns:
            The model instance if found, None otherwise.
        """
        try:
            return await self.model.get_by_id(id)
        except ModelNotFoundError:
            return None

    async def list(self, **kwargs) -> list[ModelType]:
        """
        List model instances.

        Args:
            **kwargs: Query parameters.

        Returns:
            A list of model instances.
        """
        return await self.model.find(kwargs)

    async def create(self, **kwargs) -> ModelType:
        """
        Create a model instance.

        Args:
            **kwargs: Model fields.

        Returns:
            The created model instance.
        """
        instance = self.model(**kwargs)
        await instance.save()
        return instance

    async def update(self, id: str, **kwargs) -> ModelType | None:
        """
        Update a model instance.

        Args:
            id: The ID of the model instance to update.
            **kwargs: Model fields to update.

        Returns:
            The updated model instance if found, None otherwise.
        """
        instance = await self.get_by_id(id)
        if instance is None:
            return None

        for key, value in kwargs.items():
            setattr(instance, key, value)

        await instance.save()
        return instance

    async def delete(self, id: str) -> bool:
        """
        Delete a model instance.

        Args:
            id: The ID of the model instance to delete.

        Returns:
            True if the model instance was deleted, False otherwise.
        """
        instance = await self.get_by_id(id)
        if instance is None:
            return False

        await instance.delete()
        return True
