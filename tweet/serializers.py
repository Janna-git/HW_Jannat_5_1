from rest_framework import serializers

from .models import Tweet, Comment, Mark


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"


class CommetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = "__all__"
