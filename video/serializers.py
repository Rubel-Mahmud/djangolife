from rest_framework.serializers import ModelSerializer
from .models import video

class VideoSerializer(ModelSerializer):
    class Meta:
        model = video
        fields = ['title', 'embed']
