# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
from django.db import models


FLAVOUR_CHOICES = (
    ('chocolate', 'chocolate'), 
    ('strawberry', 'strawberry'),
    ('vanilla', 'vanilla'),
    ('cherry', 'cherry'),
    ('blueberry', 'blueberry'),
    ('peanut butter', 'peanut butter'),
)

class Flavour(models.Model):
    name = models.CharField(choices=FLAVOUR_CHOICES, max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # stock = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)])
    stock = models.IntegerField()


class Container(models.Model):

    # Fields
    name = models.CharField(max_length=20)
    stock = models.IntegerField()


class Order(models.Model):

    # Max number of scoops per cone
    SCOOP_LIMIT = 3

    # Fields
    container = models.ForeignKey(Container, on_delete=models.PROTECT)
    scoops = models.ManyToManyField(Flavour)

