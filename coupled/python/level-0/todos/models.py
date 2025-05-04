from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
