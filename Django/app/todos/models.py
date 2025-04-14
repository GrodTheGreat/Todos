from django.db import models

from accounts.models import User


class Todo(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.is_complete}"
