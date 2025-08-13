from django.shortcuts import render
from .models import Author
from .serializers import AuthorSerializers
from rest_framework.response import Response
from rest_framework.decorator import api_view
from django.db.models import Count


# Create your views here.
@api_view(['GET'])
def author_detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)

    author = Author.objects.annotate(book_count=Count('book')).get(pk=author_pk)

    # 역참조 매니저를 통해 어떤 정보든 얻어옴 ( 참조중인 N들을 불러오기)
    print(author.pk, author.name, author.book_set.all())
    serializers = AuthorSerializers(author)
    return Response(serializers.data)