from django.shortcuts import render
from .serializers import PostSerializer , UserSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Post
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
# # Create your views here.

# class PostList(ListCreateAPIView):
# #    permission_classes = (permissions.IsAuthenticated ,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(RetrieveUpdateDestroyAPIView):
# #    permission_classes = (permissions.IsAuthenticated ,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer    

# class UserList(ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly , )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(ModelViewSet):
    queryset = get_user_model.objects.all()
    serializer_class = UserSerializer    