from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


from .serializers import PostListSerializer, PostDetailSerializer
from .models import *
# from .permissons import IsAdminOrReadOnly

class PostListView(APIView):
    '''Вывод списка постов'''
    def get(self, request):
        post = Post.objects.all()
        serializer = PostListSerializer(post, many=True) 
        return Response(serializer.data)


class PostDetailView(APIView):
    '''Вывод инфы о посте'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostDetailSerializer(post) 
        return Response(serializer.data)        




# class PostPagination(PageNumberPagination):
#     '''Своя пагинация'''
#     page_size = 5
#     page_query_param = 'page_size'
#     max_page_size = 100

# class PostViewSet(viewsets.ModelViewSet):
#     '''CRUD'''
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     pagination_class = PostPagination
    

#     def get_queryset(self):
#         '''возвращает список определенных постов'''
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Post.objects.all()[:5]

#         return Post.objects.filter(pk=pk)


#     @action(methods=['get'], detail=False)
#     def authors(self, request):
#         '''создаёт новый url'''
#         authors = User.objects.all()
#         return Response({'authors': [a.username for a in authors]})
