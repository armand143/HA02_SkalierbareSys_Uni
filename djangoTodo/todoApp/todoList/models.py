from django.db import models

class List(models.Model):
    taskText = models.CharField
    taskDate = models.DateField (null=True)
    taskDerc = models.IntegerField(null=True)