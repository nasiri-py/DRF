from .serializers import ArticleSerializer, UserSerializer
from blogs.models import Article
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsSuperUser, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly
# from rest_framework.views import APIView
# from rest_framework.response import Response


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # lookup_field = 'slug'
    permission_classes = [IsAuthorOrReadOnly]


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUserOrStaffReadOnly]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUserOrStaffReadOnly]


# class RevokeToken(APIView):
#     def delete(self):
#         self.request.auth.delete()
#         return Response(status=204)
