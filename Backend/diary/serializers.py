from rest_framework import serializers
from .models import Diary

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ['picture', 'first_name', 'middle_name', 'last_name', 'hair_color', 'eye_color', 'height', 'weight', 'medical_conditions', 'life_story', 'DNA_profile']
        depth = 1

medical_conditions = serializers.IntegerField(write_only=True)
life_story = serializers.IntegerField(write_only=True)
DNA_profile = serializers.IntegerField(write_only=True)