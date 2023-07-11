from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import *
class ProductSort(ImportExportModelAdmin):
    list_display = ('product_name','price','desc','pub_date')
    list_filter = ('product_name',)
    ordering=["product_name"]
admin.site.register(Product,ProductSort)
admin.site.register(Orders)