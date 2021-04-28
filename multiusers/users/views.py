from django.shortcuts import render
from .models import User,Seller,Customer
from .serializers import SellerSerializer,CustomerSerializer
from django.shortcuts import render
from rest_framework import request, viewsets
from django.conf import settings

# Create your views here.
class SellerViewSet(viewsets.ModelViewSet):

    queryset=Seller.objects.all()
    serializer_class = SellerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class = CustomerSerializer