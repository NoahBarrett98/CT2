from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Routine(models.Model):
    Creator = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    Routine_Name = models.CharField(max_length=100)
    Focus_Group = models.CharField(max_length=100)
    def __str__(self):
        return self.Creator.get_username() +", "+self.Routine_Name

class Exercise(models.Model):
    Routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Target_Group = models.CharField(max_length=50)
    Time_Seconds = models.IntegerField(default=0)
    def __str__(self):
        return self.Name
