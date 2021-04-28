from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Customer, User,Seller


class CustomerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','phone_number',]
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        return user

class SellerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'phone_number','shop_name','category']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seller = True
        user.is_staff = True
        user.is_active = True
        if commit:
            user.save()
        seller = Seller.objects.create(user=user)
        return user