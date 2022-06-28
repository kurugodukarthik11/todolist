from django.db import models


# Create your models here.
class ToDolist(models.Model):
    work = models.CharField(max_length=100)

    def __str__(self):
        return self.work
