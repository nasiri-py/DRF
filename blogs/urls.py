from django.urls import path
from . import views


app_name = 'blogs'
urlpatterns = [
    path('', views.ArticleList.as_view(), name='home')
]
