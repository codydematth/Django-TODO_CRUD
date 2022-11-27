from django.db import models


# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=250, blank=False, null=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task
