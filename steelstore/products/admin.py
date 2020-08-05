from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Order
from .models import Producto
from .models import Account


# Register your models here.

@register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre_producto', 'stock_level', 'price', 'create', )

admin.site.register(Order)
# admin.site.register(Producto)
admin.site.register(Account)
