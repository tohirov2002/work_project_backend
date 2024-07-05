from rest_framework import serializers

from .models import MessageModel

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'
