from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Post
from rest_framework import permissions
# Create your views here.

class PostList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated ,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated ,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer    
