from django.db import models
from __future__ import unicode_literals

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, Field, RegexField, Select
from django.utils.translation import ugettext_lazy as _


class Mywallet(models.Model):
    name = models.CharField("Name", max_lenght=240)
    last = models.CharField("Last", max_length=240)
    email = models.EmailField()
    birthday = models.DateField(max_length=8)
    ssn = models.IntegerField(max_length=9)
    address = models.CharField("StreetAdress", max_length=100)
    city = models.CharField("City", max_length=50)
    zipcode = models.IntegerField(max_length=12)
    state = models.CharField("State", max_length=15)
