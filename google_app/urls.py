from django.urls import path
from . import views

urlpatterns = [
  path('', views.photo_wall, name='photo_wall'),
  path('create/', views.photo_create, name='photo_create'),
  path('update/<int:row>/', views.photo_update, name='photo_update'),
  path('delete/<int:row>/', views.photo_delete, name='photo_delete'),
  path('api/', views.photo_api, name='photo_api'),
]