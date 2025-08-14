from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 추가 생성하는 시점
    updated_at = models.DateTimeField(auto_now=True)  
    
    def __str__(self): # 매직매서드 
        # PRINT 했을때 사람이 보기 좋게 꾸밀때 쓴다.
        return self.title