from django.shortcuts import render
from .models import Ads, News, Recipe
from django.views.generic import ListView, DetailView
from gallery.models import Photo


def ShowMainPage(request):
    photos = Photo.objects.all().order_by('-date')
    data = {
        'ads': Ads.objects.all().order_by('-date')[0],
        'photo_one': photos[0],
        'photo_two': photos[1],
        'photo_three': photos[2],
        'title': 'Главная',
        'news': News.objects.all().order_by('-date')[:2],
        'recipe': Recipe.objects.all().order_by('-date')[0]

    }
    return render(request, 'home/index.html', data)


class ShowNews(ListView):
    model = News
    template_name = 'home/news.html'
    context_object_name = 'News'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        ctx = super(ShowNews, self).get_context_data(**kwargs)
        ctx['title'] = 'Новости'
        return ctx


class SingleShowNews(DetailView):
    model = News
    template_name = 'home/news_instance.html'

    def get_context_data(self, **kwargs):
        ctx = super(SingleShowNews, self).get_context_data(**kwargs)
        ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        return ctx


class ShowRecipe(ListView):
    model = Recipe
    template_name = 'home/recipe.html'
    context_object_name = 'Recipe'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        ctx = super(ShowRecipe, self).get_context_data(**kwargs)
        ctx['title'] = 'Рецепты'
        return ctx


class SingleShowRecipe(DetailView):
    model = Recipe
    template_name = 'home/recipe_instance.html'

    def get_context_data(self, **kwargs):
        ctx = super(SingleShowRecipe, self).get_context_data(**kwargs)
        ctx['title'] = Recipe.objects.filter(pk=self.kwargs['pk']).first()
        return ctx
