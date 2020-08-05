import ast
import simplejson as json
from django.db import models
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from products.models import Producto

# Create your models here.

class ImportExcel(models.Model):
	name_file = models.CharField(max_length=50)
	excel_file = models.FileField(upload_to="excel_files")
	status_file = models.BooleanField(default=False)

	__original_excel = None

	def __init__(self, *args, **kwargs):
		super(ImportExcel, self).__init__(*args, **kwargs)
		self.__original_excel = self.excel_file

	def __str__(self):
		return self.name_file

	def save(self, *args, **kwargs):
		super(ImportExcel, self).save(*args, **kwargs)

		if self.excel_file != self.__original_excel:
			print("save excel")
		else:
			print("read excel")
			ef = self.excel_file.url
			data = xls_get(ef, column_limit=4)
			data_json = ast.literal_eval(json.dumps(data)).values()
			data_iterator = iter(data_json)
			data_only = next(data_iterator)

			if self.status_file == False:
				for item in data_only:
					try:
						model_product = Producto()
						model_product.nombre_producto = str(item[0])
						model_product.stock_level = int(item[1])
						model_product.price = float(item[2])
						model_product.save()
					except:
						print("Se omite %s" % (item))
				self.status_file = True
				self.save()
		
