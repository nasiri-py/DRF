from rest_framework import serializers
from blogs.models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['author', 'title', 'slug', 'publish', 'text', 'status']
        exclude = ['created', 'updated']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
