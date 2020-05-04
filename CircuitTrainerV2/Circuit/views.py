from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RoutineSerializer, ExerciseSerializer
from .models import Routine, Exercise



class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
