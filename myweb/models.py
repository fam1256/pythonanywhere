from django.db import models

class Food(models.Model):
    Name_text = models.CharField(max_length=200,blank=True)
    Img = models.CharField(max_length=200,blank=True)
    Raw_text = models.CharField(max_length=999999,blank=True)
    How_text = models.CharField(max_length=999999,blank=True)
    Calorie_text = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f'{self.Name_text} - {self.Img} - {self.Raw_text} - {self.How_text} - {self.Calorie_text} '


class Exercise(models.Model):
    Exercise_name = models.CharField(max_length=200,blank=True)
    Exercise_text = models.CharField(max_length=999999,blank=True)
    Exercise_time = models.CharField(max_length=200,blank=True)
    Exercise_calorie = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f'{self.Exercise_name} - {self.Exercise_text} - {self.Exercise_time} - {self.Exercise_calorie} '