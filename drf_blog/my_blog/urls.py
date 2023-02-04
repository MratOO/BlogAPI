from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('post/', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostDetailView.as_view()),
]