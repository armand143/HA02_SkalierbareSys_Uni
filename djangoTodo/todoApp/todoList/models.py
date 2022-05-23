from django.db import models

class List(models.Model):
    taskText = models.CharField(max_length=150, null=True)
    taskDate = models.DateField (null=True)
    taskDerc = models.IntegerField(null=True)
   
