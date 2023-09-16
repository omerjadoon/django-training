from rest_framework import serializers
from .models import Books


class BookSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields=['id','name','desc','price']