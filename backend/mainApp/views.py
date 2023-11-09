from django.shortcuts import render
from rest_framework import generics,permissions
from . serializers import *
from . models import *

# Create your views here.
# Vendor
class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorDetailedSerializer



# Product
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = productListSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = productDetailedSerializer 



# Customer
class CusomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailedSerializer
