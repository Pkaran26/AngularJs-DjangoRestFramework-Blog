from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        read_only_fields = ['pk', 'username']

class BlogPostSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    class Meta:
        model = BlogPost
        fields = '__all__'
        read_only_fields = ['pk', 'user']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['pk']

    #def get_queryset(self):
     #   return self.queryset.filter(blogpost=self.kwargs.get('pk'))

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ['pk', 'user', 'blogpost']