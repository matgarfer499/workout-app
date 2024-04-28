from django.contrib import admin
from .models import User, Workout, Exercise, WorkoutExercise, Set, WorkoutExerciseSet

# Register your models here.
admin.site.register([User, Workout, Exercise, WorkoutExercise, Set, WorkoutExerciseSet])
