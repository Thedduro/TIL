from rest_framework import serializers
from .models import Author


# class SomeSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     content = serializers.CharField()
#     opening_time = serializers.TimeField()

#     class Meta: # 어떻게 최종적으로 client한테 넘길지


class AuthorSerializers(serializers.ModleSerializers):
    # book_count = serializers.IntegerField(source='book_set.all()')
    book_count = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = '__all__'