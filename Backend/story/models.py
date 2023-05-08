from django.db import models
from authentication.models import User

class Story(models.Model):
    place_of_birth = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    number_of_siblings = models.IntegerField()
    number_of_children = models.IntegerField()
    number_of_grandchildren = models.IntegerField()
    biography = models.TextField(max_length=999)