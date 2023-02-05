from rest_framework import serializers

from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    '''Список постов'''

    author = serializers.SlugRelatedField(slug_field='username', read_only=True) # чтобы выводился не id, а имя автора
    author = serializers.HiddenField(default=serializers.CurrentUserDefault()) # при создании поста используюется текущий юзер

    class Meta:
        model = Post
        fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
    '''Данные о посте'''

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
                