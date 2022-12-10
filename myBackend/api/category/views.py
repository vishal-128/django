from django.shortcuts import render
from .serializers import CategorySerializer
from .models import Category    
from rest_framework import viewsets
#from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly,]