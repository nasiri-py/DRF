from rest_framework import serializers
from blogs.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['author', 'title', 'slug', 'publish', 'text', 'status']
        exclude = ['created', 'updated']
