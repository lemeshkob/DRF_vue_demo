from rest_framework import serializers
from .models import *


class CartSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cart
        fields = (
            'id',
            'title',
            'products'
            )


class ProductSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'price',
        )

