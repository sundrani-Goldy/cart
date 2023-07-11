from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.TextField()
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=90)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=70, default="")
    address = models.TextField()
    city = models.CharField(max_length=90, default="")
    state = models.CharField(max_length=90,  default="")
    zipcode = models.CharField(max_length=90,  default="")

    def __str__(self):
        return self.name + self.phone
