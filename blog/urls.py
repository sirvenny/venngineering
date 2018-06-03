from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail,name='post_detail'),
    path('about/', views.about, name='about'),
]
