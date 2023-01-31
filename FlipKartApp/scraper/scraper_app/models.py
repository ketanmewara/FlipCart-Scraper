from django.db import models


class Product(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.TextField()
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    size = models.CharField(max_length=10, blank=True, null=True)
    product_image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title
