from django.db import models
from authentication.models import User

class Diary(models.Model):
    picture = models.ImageField()
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    hair_color = models.CharField(max_length=255)
    eye_color = models.CharField(max_length=255)
    height = models.IntegerField()
    weight = models.IntegerField()
    status_conditions = models.ForeignKey(User, related_name='diary_status_conditions', on_delete=models.CASCADE)
    life_experience = models.ForeignKey(User, related_name='diary_life_experience', on_delete=models.CASCADE)
    DNA_profile = models.ForeignKey(User, related_name='diary_DNA', on_delete=models.CASCADE)
    isAccepted = models.BooleanField()