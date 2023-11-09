from rest_framework import serializers
from . import models

# Vendor
class VendorSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Vendor
        fields = ['id','user','address']

    def __init__(self,*args,**kwargs):
        super(VendorSerializer,self).__init__(*args,**kwargs)
        # self.Meta.depth = 1

class VendorDetailedSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Vendor
        fields = ['id','user','address']

    def __init__(self,*args,**kwargs):
        super(VendorDetailedSerializer,self).__init__(*args,**kwargs)
        # self.Meta.depth = 1




# Product
class productListSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Product
        fields = ['id','category','vendor','title','detail','price']

    def __init__(self,*args,**kwargs):
        super(productListSerializer,self).__init__(*args,**kwargs)
        # self.Meta.depth = 1


class productDetailedSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Product
        fields = ['id','category','vendor','title','detail','price']

    def __init__(self,*args,**kwargs):
        super(productDetailedSerializer,self).__init__(*args,**kwargs)
        # self.Meta.depth = 1




# Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Customer
        fields = ['id','user','mobile']

    def __init__(self,*args,**kwargs):
        super(CustomerSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1

class CustomerDetailedSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Customer
        fields = ['id','user','mobile']

    def __init__(self,*args,**kwargs):
        super(CustomerDetailedSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1
