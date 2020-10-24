from .models import Food ,Exercise
from django.forms import ModelForm

class Foodform (ModelForm):
    class Meta:
        model = Food
        fields = ['Name_text','Img','Raw_text','How_text','Calorie_text']
        
class Exerciseform (ModelForm):
    class Meta:
        model = Exercise
        fields = ['Exercise_name','Exercise_text','Exercise_time','Exercise_calorie']
