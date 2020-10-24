from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('food', views.food ,name='food'),
    path('addfood', views.addfood, name='addfood'),
    path('Exercise', views.exercise, name='exercise'),
    path('addExercise', views.addexercise, name='addexercise'),
]