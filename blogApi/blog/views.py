from .models import *
from .serializer import *
from rest_framework import generics, pagination
from django.contrib.auth.models import User

#pagination
class ApiPagination(pagination.PageNumberPagination):
    page_size = 1

#BlogPost
class CreatePost(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class ManagePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    pagination_class = ApiPagination

class BlogPostList(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    pagination_class = ApiPagination

class BlogDetail(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

#Category
class CreateCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ManageCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ApiPagination

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class GetCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(pk=self.kwargs.get('pk'))

#Comment
class CreateComment(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

class ManageComment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

class GetComment(generics.RetrieveAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comments.objects.filter(blogpost=self.kwargs.get('pk'))

#User
class GetUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer