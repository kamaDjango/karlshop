from django.contrib import admin
from .models import *

admin.site.register((Maincategory,Subcategory,Brand,Product,Checkout,CheckoutProduct,Wishlist,Contact))