from rest_framework import serializers
from .models import Text_to_speech


class TextToSpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text_to_speech
        fields = ['text', 'file_name']