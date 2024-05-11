from django.db import models


class MenuItem(models.Model):
  title = models.CharField(max_length=255, null=False)
  price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
  inventory = models.IntegerField(default=1, null=False)

  def __str__(self):
    return f'{self.title} : {str(self.price)}'


class Reservation(models.Model):
  customer_name = models.CharField(max_length=255, null=False)
  reservation_date = models.DateField(null=False)
  guests_qty = models.SmallIntegerField(default=4, null=False)

  def __str__(self):
      return self.customer_name