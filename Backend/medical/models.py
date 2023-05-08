from django.db import models
from authentication.models import User

class Medical(models.Model):
    Diagnosis = models.TextField(max_length=999)