from django.views import generic
from .models import Article
from django.shortcuts import get_object_or_404


class ArticleList(generic.ListView):
    template_name = 'blogs/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(status='p')


class ArticleDetail(generic.DetailView):
    template_name = 'blogs/article_detail.html'
    context_object_name = 'article'

    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.filter(status='p'), slug=slug)
        return article
