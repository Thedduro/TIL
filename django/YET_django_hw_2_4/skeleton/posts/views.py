from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def posts_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'GET': # article 객체를 직렬화하여 반환
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        # instance: 업데이트할 article 객체
        # data: 업데이트할 데이터
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid(raise_exception=True):  # serializer를 통해 입력 데이터의 유효성 검사
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        # :partial = True로 설정하면 일부 필드만 업데이트 가능 // request Method Patch 일 때
        serializer = PostSerializer(instance=post, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):  # serializer를 통해 입력 데이터의 유효성 검사
            serializer.save(raise_exception=True)
            return Response(serializer.data)