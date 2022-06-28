from .serializers import ArticleSerializer, UserSerializer
from blogs.models import Article
# from django.contrib.auth.models import User
# from rest_framework import generics
# from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsSuperUser, IsAuthorOrReadOnly, IsSuperUserOrStaffReadOnly, IsStaffOrReadOnly
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model


# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     # lookup_field = 'slug'
#     permission_classes = [IsAuthorOrReadOnly]


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()

        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)

        author = self.request.query_params.get('author')
        if author is not None:
            queryset = queryset.filter(author__username=author)

        return queryset

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsSuperUserOrStaffReadOnly]
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsSuperUserOrStaffReadOnly]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUserOrStaffReadOnly]


# class RevokeToken(APIView):
#     def delete(self):
#         self.request.auth.delete()
#         return Response(status=204)
