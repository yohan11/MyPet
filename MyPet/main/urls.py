from django.urls import path

from . import views

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('upload/', views.upload, name='upload'),
    path('inputform/', views.inputform, name='inputform') 
]


