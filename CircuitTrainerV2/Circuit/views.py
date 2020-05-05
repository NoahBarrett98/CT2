from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RoutineSerializer, ExerciseSerializer, UserSerializer
from .models import Routine, Exercise
from django.contrib.auth.models import User


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
