from rest_framework import serializers
from blogs.models import Article
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name']


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Article
        # fields = ['author', 'title', 'slug', 'publish', 'text', 'status']
        exclude = ['created', 'updated']

    def validate_title(self, value):
        filter_list = ['php', 'laravel']
        for i in filter_list:
            if i in value.lower():
                raise serializers.ValidationError(f"Don't use bad words!: {i}")
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
