from django.contrib import admin
from django.urls import path
from myweb import views


urlpatterns = [

    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name='register'),
    path('food', views.food, name='food'),
    path('addfood', views.addfood, name='addfood'),
    path('Exercise', views.exercise, name='exercise'),
    path('addExercise', views.addexercise, name='addexercise'),
]