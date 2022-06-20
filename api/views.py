from .serializers import ArticleSerializer
from blogs.models import Article
from rest_framework import generics


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
