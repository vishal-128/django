# from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product  
#from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly,]