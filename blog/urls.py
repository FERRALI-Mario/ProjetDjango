from django.contrib import admin
from django.urls import path

from blog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add/', views.add_post, name='add_post'),
    path('<slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:category>/', views.post_list, name='category_post_list'),

]
