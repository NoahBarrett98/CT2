from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer, RoutineSerializer, ExerciseSerializer
from .models import Profile, Routine, Exercise


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
