"""Module which contains abstract models which can be used for the whole application"""
import uuid

from django.db import models
from django.utils import timezone


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
