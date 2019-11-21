from django.db import models

class Product(models.Model):
  
  product_options = (
    ('savings', 'SAVINGS'),
    ('checking', 'CHECKING'),
    )
  card_options = (
    ('debit', 'DEBIT'),
    ('credit', 'CREDIT')
  )
  product_options = models.CharField(max_length = 8, choices = product_options, default = product_options[0])

  card_options = models.CharField(max_length = 8,
  choices = card_options, default = card_options[0])

  product = models.OneToOneField(
    Branch, 
    on_delete=models.CASCADE, 
    primary_key=True)

  def __str__(self):
    return f'{self.bank}'