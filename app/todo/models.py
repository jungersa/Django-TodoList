"""This modules contains all the models used by the todo app"""

from django.db import models
from django.urls import reverse
from app.utils.models import BaseModel


class Tasks(BaseModel):
    """A model which represents taks

    Args:
        name (str): Is the task name: required
        description (str): Is the task description: optional
        due_date (date): Is the task due date: optional
        state (bool): Completion state of the task

    """
    name = models.CharField(
        "task name",
        max_length=25,
        blank=False,
        help_text="Is the task name: required",
    )
    description = models.CharField(
        "task description",
        max_length=150,
        null=False,
        blank=True,
        help_text="Is the task description: optional",
    )
    due_date = models.DateField(
        "task due date",
        null=True,
        blank=True,
        help_text="Is the task due date: optional",
    )
    state = models.BooleanField(
        "task state",
        default=False,
        help_text="Completion state of the task",
    )

    def __str__(self) -> str:
        """Return the Task string representation"""
        return self.name

    def get_absolute_url(self) -> str:
        """Return the url related to self"""
        return reverse("todo:detail", kwargs={"pk": self.pk})
