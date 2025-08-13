from django.urls import path
from . import views

urlpatterns = [
    # 사용자가 PK에 대한 정보를 url에 보낼 예정
    # 그때 경로는 variable routing'
    path('<int:author_pk>/', views.author_detail)
]
