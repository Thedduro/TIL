from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class SignupView(generics.CreateAPIView):
    """회원가입 뷰"""
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email', '')
        
        if not username or not password:
            return Response(
                {'error': 'Username and password are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'Username already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        return Response(
            {'message': 'User created successfully.', 'user_id': user.id},
            status=status.HTTP_201_CREATED
        )

# # 수정된 LoginView

from rest_framework.authtoken.models import Token # 이 import는 이미 있습니다.

class LoginView(generics.CreateAPIView):
    """로그인 뷰"""
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response(
                {'error': 'Username and password are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = authenticate(username=username, password=password)
        
        if user:
            # ✅ 이 부분이 핵심입니다!
            # 사용자에 대한 토큰을 가져오거나, 없으면 새로 생성합니다.
            token, created = Token.objects.get_or_create(user=user)
            
            # 응답에 토큰을 포함시켜 반환합니다.
            return Response(
                {
                    'message': 'Login successful.',
                    'token': token.key,  # 👈 여기에 토큰 추가!
                    'user_id': user.id,
                    'username': user.username
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'error': 'Invalid credentials.'},
                status=status.HTTP_401_UNAUTHORIZED
            )