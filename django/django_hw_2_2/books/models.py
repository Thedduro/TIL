from django.db import models
from authors.models import Author

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    # 저자랑 1:N 관계 만들기
    # 저자의 pk 값을 FK로 정의할 필드 생성
    author = models.ForeignKey('authors.author', on_delete=models.CASCADE)

    def __str__(self): # 매직 메소드
        return self.title