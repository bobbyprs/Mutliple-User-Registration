
from django.urls import path,include
from .views import CustomerViewSet,SellerViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

router = DefaultRouter()
router.register('seller',SellerViewSet,basename='seller'),
router.register('customer',CustomerViewSet,basename='customer')


urlpatterns = [
    path('user/',include(router.urls) ),
]
