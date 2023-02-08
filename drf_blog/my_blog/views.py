from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated
    )

from .permissons import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import PostListSerializer, PostDetailSerializer
from .models import *


class PostPagination(PageNumberPagination):
    '''Своя пагинация'''
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    '''CRUD'''
    # queryset = Post.objects.all()  раскомментить при jwt токене
    serializer_class = PostListSerializer
    pagination_class = PostPagination
    permission_classes = (IsAuthenticated,) # доступ IsAdminOrReadOnly, IsOwnerOrReadOnly
    # authentication_classes =  доступ по определенной авторизации
    

# закомментить ниже при jwt токене

    def get_queryset(self):
        '''возвращает список определенных данных'''
        pk = self.kwargs.get('pk')
        if not pk:
            return Post.objects.all()[:5]

        return Post.objects.filter(pk=pk)


    @action(methods=['get'], detail=True)
    def authors(self, request, pk=None):
        '''создаёт новый url'''
        authors = User.objects.get(pk=pk)
        return Response({'authors': authors.username})
