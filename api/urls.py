from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'api'
# urlpatterns = [
#     path('', views.ArticleList.as_view(), name='list'),
#     path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
#     path('users/', views.UserList.as_view(), name='user_list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
# ]

router = routers.SimpleRouter()
router.register('articles', views.ArticleViewSet, basename='articles')
router.register('users', views.UserViewSet, basename='users')

# urlpatterns = router.urls
urlpatterns = [
    path("", include(router.urls)),
    # path("authors/<int:pk>/", views.AuthorRetrieve.as_view(), name='author_detail'),
]
