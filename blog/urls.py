from django.urls import path
from blog import views

urlpatterns = [
    path('', views.posts, name='blog'),
    path('category/<int:category_id>/', views.category, name='category'),
]
