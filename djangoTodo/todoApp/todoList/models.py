from django.db import models

class Liste(models.Mode):
    taskText = models.CharField
    taskDate = models.DateField (null=True)
    taskDerc = models.IntegerField(null=True)