from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['place_of_birth', 'education', 'number_of_siblings', 'number_of_children', 'number_of_grandchildren', 'biography']