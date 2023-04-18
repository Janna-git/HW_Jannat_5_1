from rest_framework import generics

from .models import Tweet, Comment, Mark
from .serializers import TweetSerializer, CommetSerializer, MarkSerializer


class TweetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommetSerializer


class MarkListCreateAPIView(generics.ListCreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

