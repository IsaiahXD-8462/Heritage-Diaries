from rest_framework import serializers
from .models import Diary

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ['picture', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'hair_color', 'eye_color', 'height', 'weight', 'status_conditions', 'life_experience', 'DNA_profile']
        depth = 1

status_conditions = serializers.IntegerField(write_only=True)
life_experience = serializers.IntegerField(write_only=True)
DNA_profile = serializers.IntegerField(write_only=True)