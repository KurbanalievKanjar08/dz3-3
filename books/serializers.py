from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'publication_date', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def validate_publication_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Publication date cannot be in the future.")
        return value