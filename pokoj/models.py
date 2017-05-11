# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Ogloszenia(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    tytul = models.CharField(verbose_name='Tytuł', max_length=30)
    opis = models.TextField(blank=False, help_text='Opis Ogłoszenia')
    data = models.DateField('dodano', auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.tytul)

    class Meta:
        verbose_name = "ogłoszenie"
        verbose_name_plural = 'ogłoszenia'