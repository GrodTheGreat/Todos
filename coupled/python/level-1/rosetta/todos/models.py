from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_complete = models.BooleanField(default=False)
