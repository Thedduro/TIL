from django.shortcuts import render
# django가 가지고 있는 http에 따른 응답 방식
from django.http import JsonResponse
# RESTful한 API를 만들도록 해주는 famework
from rest_framework.decorators import api_view

# Create your views here.
# 행위 -> RESTful API를 위한 것
# GET 요청일 떄만 아래 함수가 동작하도록 하고 싶어, 그렇게 함수를 꾸밀꺼야
@api_view(['GET', 'POST'])
def index(request):
    # 모든 view 함수는 첫번째 인자 request 고정
        # 아, 물론 인자명 request는 다른 이름이어도 상관은 없지만
        # django의 가이드 상, request이므로, 다른 이름으로 적지않음
    # 응답: JSON 형태로 Response -> {'message': 'Hello, Django!'}
    # request에는 사용자의 모든 요청과 관련된 정보가
    if request.method == 'POST':
        return JsonResponse({'message': 'Hello, Django!'})
    elif request.method == 'GET':
        return JsonResponse({'message': 'Hello, Django!'})

def detail(request, article_pk):
    # 원래는 여기서 model 거쳐서 실제 1번 게시글을 가져와야하는디
    # 지금은 모델이 없으니 그냥 반환
    data = {
        'id': article_pk,
        'message': f'{article_pk}번 게시글에 대한 정보입니다.'
    }
    return JsonResponse(data)