from rest_framework import serializers

from .models import CommentsModel


class CommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = CommentsModel
        fields = '__all__'
