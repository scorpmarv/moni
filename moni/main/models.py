# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext as _


class LoanApplication(models.Model):
    GENDER_CHOICES = (
        (u'M', _('Masculino')),
        (u'F', _('Femenino')),
        (u'O', _('Otro')),
    )

    document_number = models.PositiveIntegerField(
        verbose_name=_('DNI'),
        help_text=_('Utilice únicamente números')
    )
    name = models.CharField(max_length=40, verbose_name=_('Nombre'))
    surname = models.CharField(max_length=40, verbose_name=_('Apellido'))
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        verbose_name=_('Género')
    )
    email = models.EmailField(verbose_name=_('Email'))
    amount = models.FloatField(
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name=_('Monto')
    )
    approved = models.BooleanField()
    error = models.BooleanField()
