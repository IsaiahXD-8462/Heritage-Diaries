from django.db import models
from authentication.models import User

class Diary(models.Model):
    Diagnosis = models.CharField(max_length=255)