from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import InvoiceItem
from .models import Invoice
# Register your models here.

class InvoiceItemTabularline(admin.TabularInline):
	model = InvoiceItem
	extra = 0

@register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
	inlines = [InvoiceItemTabularline,]
	list_display = ('client_name', 'DNI', 'total', )
admin.site.register(InvoiceItem)
#admin.site.register(Invoice)
