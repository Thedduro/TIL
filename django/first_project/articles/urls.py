from django.urls import path
# 나랑 같은 폴더의 views
from . import views

urlpatterns = [
    path('index/', views.index),
    path('<int:article_pk>/', views.detail),
]
