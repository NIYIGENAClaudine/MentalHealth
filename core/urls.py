from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='rticle_list'),  # Example view
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    #path('article/<int:pk>/', views.article_detail, name='article_detail'),  # Example detail view
    # Add more URL patterns for your views here
]