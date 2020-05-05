from django.db import models
from django.contrib.auth.models import User


class Routine(models.Model):
    Creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Routine_Name = models.CharField(max_length=100)
    Description =  models.CharField(max_length=500)
    Focus_Group = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Creator.get_username() +", "+self.Routine_Name


class Exercise(models.Model):
    Routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Target_Group = models.CharField(max_length=50)
    Time_Seconds = models.IntegerField(default=0)
    def __str__(self):
        return self.Name
