# dashboard_app/serializers.py
from rest_framework import serializers
from .models import Category, Tag, Item, ProductionOrder  # Add the import statement for ProductionOrder

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Item
        fields = '__all__'

class ProductionOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionOrder
        fields = '__all__'
