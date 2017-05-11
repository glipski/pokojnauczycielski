# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from . import forms
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def index(request):
    """Strona główna"""
    kontekst = {'komunikat': 'Witaj w aplikacji Pokoj Nauczycielski!'}
    return render(request, 'pokoj/index.html', kontekst)
  
@method_decorator(login_required, 'dispatch')
class OgloszenieCreate(CreateView):
    model = models.Ogloszenia
    form_class = forms.OgloszeniaForm
    success_url = reverse_lazy('pokoj:lista')  # '/pokoj/lista'
    
    def get_context_data(self, **kwargs):
        context = super(OgloszenieCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['ogloszenia'] = forms.OgloszeniaForm(self.request.POST)
        else:
            context['ogloszenia'] = forms.OgloszeniaForm()
        return context
      
    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.autor = self.request.user
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form)
        )
      
@method_decorator(login_required, 'dispatch')
class OgloszenieUpdate(UpdateView):
    """Widok aktualizuacji"""

    model = models.Ogloszenia
    form_class = forms.OgloszeniaForm
    success_url = reverse_lazy('pokoj:lista')  # '/pizza/lista'

    def get_context_data(self, **kwargs):
        context = super(OgloszenieUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['ogloszenia'] = forms.OgloszeniaForm(
                self.request.POST,
                instance=self.object)
        else:
            context['ogloszenia'] = forms.OgloszeniaForm(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.autor = self.request.user
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form)
        )

@method_decorator(login_required, 'dispatch')
class OgloszenieDelete(DeleteView):
    model = models.Ogloszenia
    success_url = reverse_lazy('pokoj:lista')  # '/pizza/lista'

    def get_context_data(self, **kwargs):
        context = super(OgloszenieDelete, self).get_context_data(**kwargs)
        return context
      
@method_decorator(login_required, 'dispatch')
class OgloszenieDetailView(DetailView):
    model = models.Ogloszenia

    def get_context_data(self, **kwargs):
        context = super(OgloszenieDetailView, self).get_context_data(**kwargs)
        return context