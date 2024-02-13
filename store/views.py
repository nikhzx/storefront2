from urllib import response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Collection
from.serializers import CollectionSerializer, ProductSerializer
from store import serializers

# Create your views here.
#func based views
@api_view()
def product_list(request):
    queryset = Product.objects.select_related("collection").all()
    serializer = ProductSerializer(queryset, many = True, context={'request': request})
    return Response(serializer.data)

@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id) #pk is lookup parameter
    serializer = ProductSerializer(product)
    return Response(serializer.data)
    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response(status = status.HTTP_404_NOT_FOUND)

@api_view()
def collection_detail(request, pk):
    return Response('ok')
