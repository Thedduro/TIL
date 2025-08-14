from django.shortcuts import render
from django.http import JsonResponse
# RESTful한 API를 만들도록 해주는 famework
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def menu_list(request):
    data =[
        {"name": "Espresso", "price": 3000},
        {"name": "Americano", "price": 3500},
        {"name": "Latte", "price": 4000}
    ]
    return JsonResponse(data)
