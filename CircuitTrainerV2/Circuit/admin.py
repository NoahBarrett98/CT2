from django.contrib import admin
from .models import Profile, Routine, Exercise
# Register your models here.
admin.site.register(Profile)
admin.site.register(Routine)
admin.site.register(Exercise)
