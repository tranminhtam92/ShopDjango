from rest_framework import serializers
from src.models import Comment

class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
