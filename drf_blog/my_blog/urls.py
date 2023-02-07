from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.SimpleRouter()
#(basename='') - имя маршрута, обязательно если нет queryset
router.register(r'post', views.PostViewSet, basename='post') # post это префикс который пишется в адрессной строке http://127.0.0.1:8000/api/v1/post/


urlpatterns = [
    path('', include(router.urls)),
]