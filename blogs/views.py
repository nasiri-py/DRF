from django.shortcuts import render
from django.views import generic
from .models import Article


class ArticleList(generic.ListView):
    template_name = 'blogs/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(status='p')
