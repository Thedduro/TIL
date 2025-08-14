from rest_framework import serializers
from .models import post

class PostSerializer(serializers.ModelSerializer):
    # 직렬화를 한다.
    class Meta:
        # 모델에 대한 정보를 토대로
        model = post
        # fields = '__all__'
        fields = '__all__'