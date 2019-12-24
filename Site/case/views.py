from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Case

class CasePage(ListView):
    model = Case
    template_name = 'case/case_page.html'
    context_object_name = 'Case'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CasePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Кейсы'

        return ctx
