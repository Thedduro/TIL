# urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # articles/로 요청이 왔을때
    path('<int:posts_pk>/', views.posts_detail),
]