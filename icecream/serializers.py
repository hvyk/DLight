# from django.contrib.auth.models import User, Group
from rest_framework import serializers

from icecream.models import Flavour, Container, Order, FLAVOUR_CHOICES


class FlavourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavour
        fields = ['pk', 'name', 'price', 'stock']


class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = ['pk', 'name', 'stock']

        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['container', 'scoops']

