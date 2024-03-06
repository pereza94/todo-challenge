from enum import Enum

from django.db import models
from django.conf import settings


class TaskStatus(Enum):
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    NOT_STARTED = "NOT_STARTED"


class Task(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def general_task_status(self) -> str:
        subtasks = self.subtasks.all()
        if subtasks:
            if all(subtask.completed for subtask in subtasks):
                return TaskStatus.COMPLETED.value
            return TaskStatus.IN_PROGRESS.value
        return TaskStatus.NOT_STARTED.value

    @property
    def subtasks_amount(self) -> int:
        return len(self.subtasks.all())


class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="2")
    name = models.CharField(max_length=70, null=False, blank=False)
    description = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
