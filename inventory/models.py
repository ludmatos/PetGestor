from django.db import models
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=0)
    category_tag = models.CharField(max_length=20, blank=True, null=True)
    NCM = models.CharField(max_length=8, default=00000000)
    bar_code = models.IntegerField(unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name