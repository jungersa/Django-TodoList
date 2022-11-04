"""Module which contains abstract models which can be used for the whole application"""
import uuid

from django.db import models


class BaseModel(models.Model):
    """A base Model to be used almost everywhere on the app is an abstract model


    Attributes:
        id (UUIDField): `id` is an unique .
        created_at (DateTimeField): Contains the date the object was created.
        updated_at (DateTimeField): Contains the date the object was last updated.

    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NameDescModel(BaseModel):
    """A base Model extented with name and description
    to be used almost everywhere on the app is an abstract model


    Attributes:
        id (UUIDField): `id` is an unique .
        created_at (DateTimeField): Contains the date the object was created.
        updated_at (DateTimeField): Contains the date the object was last updated.
        name (str): Contains a name wich can't be > than 50 characters
        description (str): Contains a description of the current object

    """

    name = models.CharField(
        "task name",
        max_length=50,
        blank=False,
        help_text="Is the name: required (max_lenght 50)",
    )
    description = models.TextField(
        "task description",
        blank=True,
        help_text="Is the description: optional",
    )

    class Meta:
        abstract = True
