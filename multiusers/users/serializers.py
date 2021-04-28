from rest_framework import serializers
from .models import Seller,Customer,User
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.views import Token
from django.contrib.auth.password_validation import validate_password
from django.conf import settings
from django.db.models import Q

class SellerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Seller.objects.all())]
            )
    is_active =serializers.BooleanField(default=True)
    is_staff =serializers.BooleanField(default=True)
    
    class Meta:
        model = Seller
        fields =['id','shop_name','username', 'password','email','date_joined','phone_number','category','last_login','is_active','is_staff']
        extra_kwargs ={'password':{
            'write_only':True,
           
        }}

    def create(self,validated_data):
        seller=Seller.objects.create_user(**validated_data)
        return seller


class CustomerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Customer.objects.all())]
            )
    is_active =serializers.BooleanField(default=False)
    class Meta:
        model = Customer
        fields =['id','username', 'password','email','date_joined','phone_number','last_login','is_active']
        extra_kwargs ={'password':{
            'write_only':True,
           
        }}

    def create(self,validated_data):
        customer=Customer.objects.create_user(**validated_data)
        return customer

