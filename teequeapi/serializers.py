from rest_framework import serializers
from teequeapp.models import *
from decimal import Decimal

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ['created_at', 'updated_at']

    taxedPrice = serializers.SerializerMethodField(method_name='price_w_tax')
    # seller = serializers.HyperlinkedRelatedField(
    #     queryset=Seller.objects.all(),
    #     view_name='seller-detail'
    # )
    # category = CategorySerializer()
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all())

    # destructure 
    # tags = TagSerializer(many=True)

    def price_w_tax(self, service: Service):
        return (service.price * Decimal(0.15)) + service.price
    
    # def create(self, validated_data):
    #     categoryobj = Category.objects.get(pk=validated_data['category'])
    #     validated_data['category'] = categoryobj
    #     service = Service(**validated_data)
    #     service.save()
    #     return service

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = ['service_id']

    def create(self, validated_data):
        service_id = self.context['service_id']
        service = Service.objects.get(pk=service_id)
        return Rating.objects.create(service_id=service, **validated_data)