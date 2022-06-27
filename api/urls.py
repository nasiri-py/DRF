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
router.register('', views.ArticleViewSet)
router.register('users', views.UserViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path("", include(router.urls))
]
