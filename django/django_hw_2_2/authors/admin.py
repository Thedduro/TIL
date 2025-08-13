from django.contrib import admin
from .models import Author

# Register your models here.

# 관리자 사이트에 저자정보 등록
admin.site.register(Author)