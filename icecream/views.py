# Create your views here.
from rest_framework import viewsets
from icecream.models import Flavour, Container, Order
from icecream.serializers import FlavourSerializer, ContainerSerializer, OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt


class FlavourList(APIView):

    def get(self, request, format=None):
        flavours = Flavour.objects.all()
        serializer = FlavourSerializer(flavours, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):  
        data = JSONParser().parse(request)
        serializer = FlavourSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FlavourDetail(APIView):

    def get_objects(self, pk):
        try:
            return Flavour.objects.get(pk=pk)
        except Flavour.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        flavour = self.get_objects(pk)
        serializer = FlavourSerializer(flavour)
        return Response(serializer.data)


class ContainerList(APIView):

    def get(self, request, format=None):
        containers = Container.objects.all()
        serializer = ContainerSerializer(containers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):  
        data = JSONParser().parse(request)
        serializer = ContainerSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContainerDetail(APIView):

    def get_objects(self, pk):
        try:
            print('Returing get_objects with pk')
            return Container.objects.get(pk=pk)
        except Container.DoesNotExist:
            print('Returing get_objects with Http404')
            raise Http404

    def get(self, request, pk, format=None):
        container = self.get_objects(pk)
        serializer = ContainerSerializer(container)
        return Response(serializer.data)



class OrderList(APIView):

    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)

        # Remove any scoops beyond the SCOOP_LIMIT
        # Note - Django models don't store duplicates in ManyToManyFields
        #  therefore, you can only have unique flavours in this simple ordering
        #  implementation
        for order in data:
            if len(order['scoops']) > Order.SCOOP_LIMIT:
                del order['scoops'][3:]

        serializer = OrderSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):

    def get_objects(self, pk):
        try:
            print('Returing get_objects with pk')
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            print('Returing get_objects with Http404')
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_objects(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)