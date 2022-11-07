from rest_framework import serializers

from .models import Post



class PostSerializer(serializers.ModelSerializer):
    '''Сериалайзер модели из базы данных'''

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'