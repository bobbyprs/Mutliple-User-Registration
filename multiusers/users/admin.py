from django.contrib import admin
from .models import User,Customer,Seller
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import SellerSignUpForm,CustomerSignUpForm
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
import pprint

# Register your models here.


User = get_user_model()

# class UsersAdmin(BaseUserAdmin):
    
#     add_form = SellerSignUpForm
#     list_display =('username', 'email', 'phone_number','shop_name','category','is_active','is_staff','is_superuser','is_seller','is_customer','date_joined','last_login',)
#     search_fields =('email','username')
#     readonly_fields =('id','date_joined','last_login')
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ( 'username','email','phone_number','shop_name','category','is_active','is_staff','is_superuser','is_seller','is_customer',)}
#         ),
#     )    
#     filter_horizontal =()
#     list_filter =('email','username')
#     fieldsets =()
    
#     ordering = ['email']
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return pprint.pformat(obj.get_decoded()).replace('\n', '<br>\n')
    _session_data.allow_tags=True
    list_display = ['session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']
    exclude = ['session_data']

admin.site.register(Session, SessionAdmin)

admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Customer)