from django.db import models
#for choosing the field format
# date": "2020-08-10", 
# "trade_code": "1JANATAMF", 
# "high": "4.3", 
# "low": "4.1", 
# "open": "4.2", 
# "close": "4.1", 
# "volume": "2,285,416"

# Create your models here.
class stock_market_data(models.Model):
    date = models.DateField(editable=True)
    trade_code = models.CharField(max_length=255)
    high = models.DecimalField(max_digits=10, decimal_places=1)
    low = models.DecimalField(max_digits=10, decimal_places=1)
    open= models.DecimalField(max_digits=10, decimal_places=1)
    close= models.DecimalField(max_digits=10, decimal_places=1)
    volume = models.CharField(max_length=255)

   

