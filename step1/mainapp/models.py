from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=99.99)

    def __str__(self):
        return self.title

    @property
    def sale_price(self):
        return "%.2f" % (self.price + ((self.price / 100) * 15))

    def get_discount(self):
        return (self.price / 100) * 30