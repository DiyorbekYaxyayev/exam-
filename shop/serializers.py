from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['subcategories'] = SubCategorySerializer(instance.subcategories, many=True).data
        return representation

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'category', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'subcategory', 'name', 'slug', 'price', 'stock', 'image', 'created_at']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', "first_name", "last_name")