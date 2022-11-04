"""This modules contains all the models used by the todo app"""

from django.db import models
from django.urls import reverse

from app.utils.models import NameDescModel

# Create your models here.


class Project(NameDescModel):
    """A project which stores a list of tasks

    A project with a name, description and a list of tasks. Related to :model: `app.todo.Task`

    Args:
        name (str): Is the project name: required (max_lenght 50)
        description (str): Is the project description: optional
        tasks (Task): a foreign key in the :model: `app.todo.Task`

    """

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"

    def __str__(self) -> str:
        """Return the representation of self"""
        return self.name

    def get_absolute_url(self) -> str:
        """Return the url related to self Project (Project detail page)"""
        return reverse("todo:project_detail", kwargs={"pk": self.pk})

    def todo_restante(self) -> int:
        return self.tasks.filter(state=False).count()


class Task(NameDescModel):
    """A model which represents taks

    Args:
        name (str): Is the task name: required (max_lenght 50)
        description (str): Is the task description: optional
        due_date (date): Is the task due date: optional
        state (bool): Completion state of the task
        project (Project): The :model: `app.todo.Project` to which the task is related

    """

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
    project = models.ForeignKey(
        "todo.Project",
        null=True,
        on_delete=models.CASCADE,
        related_name='tasks',
    )

    def __str__(self) -> str:
        """Return the Task string representation"""
        return self.name

    def get_absolute_url(self) -> str:
        """Return the url related to self Task (Task detail page)"""
        return reverse("todo:detail", kwargs={"pk": self.pk})
