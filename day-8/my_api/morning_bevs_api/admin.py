from django.contrib import admin
from .models import Beverage, Brand, Category

admin.site.register(Beverage)
admin.site.register(Brand)
admin.site.register(Category)