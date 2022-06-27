from rest_framework import serializers
from blogs.models import Article
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['author', 'title', 'slug', 'publish', 'text', 'status']
        exclude = ['created', 'updated']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
