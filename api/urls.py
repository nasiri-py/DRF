from django.urls import path
from . import views


app_name = 'api'
urlpatterns = [
    path('', views.ArticleList.as_view(), name='list')
]
