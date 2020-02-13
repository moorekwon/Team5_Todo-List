from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title, self.text


class TodoStatus(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)