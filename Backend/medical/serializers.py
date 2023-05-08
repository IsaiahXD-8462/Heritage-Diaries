from rest_framework import serializers
from .models import Medical

class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical
        fields = ['diagnosis']