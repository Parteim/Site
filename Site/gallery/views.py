from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Photo


def gallery(request):
    return render(request, 'gallery/gallery.html')


class Gallery(ListView):
    model = Photo
    template_name = 'gallery/gallery.html'
    context_object_name = 'Photos'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        ctx = super(Gallery, self).get_context_data(**kwargs)
        ctx['title'] = 'Галерея'
        return ctx
