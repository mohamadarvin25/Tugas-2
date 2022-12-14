from django.db import models

class CatalogItem(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.BigIntegerField()
    description = models.TextField()
    item_stock = models.IntegerField()
    rating = models.IntegerField()
    item_url = models.URLField()