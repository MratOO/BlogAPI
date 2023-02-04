from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('post_list/', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostUpdate.as_view()),
    path('postdetail/<int:pk>/', views.PostDetailView.as_view()),
]