# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings

class Contact(models.Model):

    # product_id = models.CharField(max_length=10)
    contact_name = models.CharField(max_length=100)
    contact_number = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='image/%Y/%m/%d', default='there_is_no_image.jpg')

    def __str__(self):
        return "%s" % self.contact_name