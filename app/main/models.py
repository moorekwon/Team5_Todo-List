from django.db import models


# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    priority = models.PositiveIntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title, self.text
