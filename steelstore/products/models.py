from django.db import models
from django.utils import timezone


# Create your models here

class Order(models.Model):

	creation_date = models.DateTimeField(editable=False)
	especial_instruccion = models.TextField()
	number_order = models.PositiveIntegerField()
	payment_method = models.CharField(max_length=225)

	def __str__(self):
		return self.especial_instruccion

	def save(self, *args, **kwargs):
		if not self.id:
			self.creation_date = timezone.now()
		return super(Order, self). save(*args, **kwargs)

class Producto(models.Model):

	nombre_producto = models.CharField(max_length=225)
	stock_level = models.IntegerField()
	create = models.DateTimeField(editable=False)
	price = models.DecimalField(decimal_places=2, max_digits=6)
	
	def __str__(self):
		return self.nombre_producto

	def save(self, *args, **kwargs):
		if not self.id:
			self.create = timezone.now()
		return super(Producto, self).save(*args, **kwargs)


class Account(models.Model):

	creation_date = models.DateTimeField(editable=False)
	e_mail = models.EmailField()
	user_name = models.CharField(max_length=11)
	password = models.CharField(max_length=50)
	active = models.BooleanField()

	def __str__(self):
		return str(self.user_name)

	def save(self, *args, **kwargs):
		if not self.id:
			self.creation_date = timezone.now()
		return super(Account, self).save(*args, **kwargs)

