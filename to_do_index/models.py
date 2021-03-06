from django.db import models


class Task(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

