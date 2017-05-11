# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from . import models
from django.forms.models import inlineformset_factory


class OgloszeniaForm(ModelForm):

    class Meta:
        model = models.Ogloszenia
        exclude = ('data', 'autor')
        widgets = {'opis': Textarea(attrs={'rows': 2, 'cols': 80})}

