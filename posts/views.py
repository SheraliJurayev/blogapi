from django.shortcuts import render
from .serializers import PostSerializer , UserSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Post
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
# Create your views here.

class PostList(ListCreateAPIView):
#    permission_classes = (permissions.IsAuthenticated ,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
#    permission_classes = (permissions.IsAuthenticated ,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer    

class UserList(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
