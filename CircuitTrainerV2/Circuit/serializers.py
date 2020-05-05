from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Routine, Exercise


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
