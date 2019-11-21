# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from bank.branch.model_branch import Branch
from bank.product.model_product import Product
from bank.account.model_account import Account
from bank.customer.model_customer import Customer

admin.site.register((
  Branch,
  Product,
  Account,
  Customer,
))