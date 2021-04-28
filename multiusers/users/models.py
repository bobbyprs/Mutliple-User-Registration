from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.crypto import get_random_string
from django.conf import settings
import random
from django.core.mail import send_mail,EmailMessage
from django.db.models import Q
from multiselectfield import MultiSelectField
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class MyTenentManger(BaseUserManager):
    
    def create_user(self,email,username,phone_number,category,is_active,is_staff,shop_name,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("User must have an username")
        if not phone_number:
            raise  ValueError("User must have an phone number")
        

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
            category=category,
            shop_name=shop_name
        )
        
        use_password=get_random_string(length=12)
        user.set_password(use_password)
        send_mail(
            'Subject',
            use_password,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        user.is_active =True
       
        user.save(using=self._db)
        return user
        
    def create_superuser(self,email,username,phone_number,category,is_active,password):

        if not email:
            raise ValueError("Users must have an email address")

        if not username:
            raise ValueError("User must have an username")

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
           email=self.normalize_email(email),
            username=username,
            password=password,
            phone_number=phone_number,
            
            )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.is_active=True
        user.save(using=self._db)

        return user

class SellerManager(BaseUserManager):

    def get_queryset(self, *args, **kwargs):

        #return super().get_queryset(*args, **kwargs).filter(type = CustomUser.Types.SELLER)
        return super().get_queryset(*args,**kwargs).filter(Q(type__contains = User.Types.SELLER))


    def create_user(self,email,username,phone_number,category,is_active,is_staff,shop_name,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("User must have an username")
        if not phone_number:
            raise  ValueError("User must have an phone number")
        if not type:
            raise ValueError('type error')
        

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
            category=category,
            shop_name=shop_name,
            type =User.Types.SELLER
        )
        
        use_password=get_random_string(length=12)
        user.set_password(use_password)
        send_mail(
            'Subject',
            use_password,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        user.is_active =True
        user.is_staff=True
        user.type =User.Types.SELLER
        user.save(using=self._db)

        return user

class CustomerManager(BaseUserManager):

    def get_queryset(self, *args, **kwargs):

        #return super().get_queryset(*args, **kwargs).filter(type = CustomUser.Types.SELLER)
        return super().get_queryset(*args,**kwargs).filter(Q(type__contains = User.Types.CUSTOMER))


    def create_user(self,email,username,phone_number,is_active,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("User must have an username")
        if not phone_number:
            raise  ValueError("User must have an phone number")
        

        user =self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
            
        )
        
        use_password=get_random_string(length=12)
        user.set_password(use_password)
        send_mail(
            'Subject',
            use_password,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        user.is_active =True
        user.type =User.Types.CUSTOMER
        user.save(using=self._db)
        
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    shop_name=models.CharField(max_length=60,null=True,blank=True)
    email = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = models.CharField(max_length=30,unique=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    password=models.CharField(null=True,max_length=128)
    date_joined =models.DateTimeField(verbose_name='date_joined',auto_now_add=True)
    last_login =models.DateTimeField(verbose_name="last_login",auto_now=True)
    category=models.CharField(max_length=60,null=True,blank=True)
    is_admin =models.BooleanField(default=False)
    is_active =models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',default=True)
    is_staff =models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    

    class Types(models.TextChoices):
        SELLER = "Seller","SELLER"
        CUSTOMER = "Customer","CUSTOMER"

    default_type = Types.CUSTOMER

    type = MultiSelectField(choices=Types.choices, default=[], null=True, blank=True)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['username','phone_number']

    objects =MyTenentManger()

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.default_type
            # self.type.append(self.default_type)
        return super().save(*args, **kwargs)

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_lable):
        return True

class Customer(User):
    default_type = User.Types.CUSTOMER
    objects = CustomerManager()

    class Meta:
        proxy = True


class Seller(User):
    default_type = User.Types.SELLER
    objects = SellerManager()

    class Meta:
        proxy = True

    