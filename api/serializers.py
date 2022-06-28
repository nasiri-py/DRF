from rest_framework import serializers
from blogs.models import Article
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ['id', 'username', 'first_name', 'last_name']


# class AuthorUsernameField(serializers.RelatedField):
#     def to_representation(self, value):
#         return value.username


class ArticleSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()
    # author = serializers.HyperlinkedIdentityField(view_name='api:author_detail')
    # author = AuthorUsernameField(read_only=True)
    # author = serializers.CharField(source="author.username", read_only=True)

    def get_author(self, obj):
        return {
            "username": obj.author.username,
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name
        }

    author = serializers.SerializerMethodField("get_author")

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
        # fields = '__all__'
