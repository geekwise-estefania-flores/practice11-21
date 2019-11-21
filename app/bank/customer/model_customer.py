from django.db import models

class Customer(models.Model):
  customer_name = models.CharField(max_length = 30)
  customer_email = models.EmailField(max_length = 100)

  account = models.ForeignKey('auth.User', related_name='account', null=True,
    on_delete=models.CASCADE)

  def __str__(self):
    return self.account