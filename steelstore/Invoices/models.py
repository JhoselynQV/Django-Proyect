from django.db import models
from products.models import Producto
from django.utils import timezone
# Create your models here.
class Invoice(models.Model):
	client_name = models.CharField(max_length=50)
	DNI = models.CharField(max_length=10)
	sale_date = models.DateTimeField(editable=False)
	total = models.DecimalField(decimal_places=2, max_digits=6, default=0)

	def __str__(self):
		return self.client_name

	def save(self, *args, **kwargs):
		if not self.id:
			self.sale_date = timezone.now()
		
		else:
			sub_totales = 0
			items = InvoiceItem.objects.filter(factura__id=self.id)
			for i in items:
				sub_totales += i.sub_total
			self.total = sub_totales
		

		return super(Invoice, self). save(*args, **kwargs)


class InvoiceItem(models.Model):
	product = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="product_invoice")
	factura = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="factura_invoice")
	cantidad = models.IntegerField()
	sale_price = models.DecimalField(decimal_places=2, max_digits=6, default=0)
	sub_total = models.DecimalField(decimal_places=2, max_digits=6, default=0)

	def save(self, *args, **kwargs):
		if not self.id:
			self.sub_total = self.product.price * self.cantidad
			self.sale_price = self.product.price
		return super(InvoiceItem, self). save(*args, **kwargs)