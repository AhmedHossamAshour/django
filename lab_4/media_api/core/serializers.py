from rest_framework import serializers
from .models import Movie, Series, Category, Cast

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    casts = CastSerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True, source='categories'
    )
    cast_ids = serializers.PrimaryKeyRelatedField(
        queryset=Cast.objects.all(), write_only=True, many=True, source='casts'
    )

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'description', 'release_date',
            'poster_image', 'categories', 'casts', 'category_ids', 'cast_ids'
        ]
