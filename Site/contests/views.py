from django.shortcuts import render
from .models import Contests, PastContests, Winners, FutureContests
from django.utils import timezone
from django.views.generic import ListView, DetailView


def ShowContestsPage(request):
    # date = timezone.now().date()
    # contests = Contests.objects.filter(date=date)
    data = {
        'winners': Winners.objects.all(),
        'past_contests': PastContests.objects.all().order_by('-date')[:5],
        'contests': FutureContests.objects.all().order_by('-date'),
        'title': 'Конкурсы',
    }

    return render(request, 'contests/contests.html', data)


class ShowContests(ListView):
    model = FutureContests
    template_name = 'contests/all_contests.html'
    context_object_name = 'Contests'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        ctx = super(ShowContests, self).get_context_data(**kwargs)
        ctx['title'] = 'Все конкурсы'
        return ctx


class ShowPastContests(ListView):
    model = PastContests
    template_name = 'contests/past_contests.html'
    context_object_name = 'Contests'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        ctx = super(ShowPastContests, self).get_context_data(**kwargs)
        ctx['title'] = 'Прошедшие конкурсы'
        return ctx


class SingleShowContests(DetailView):
    model = Contests
    template_name = 'contests/contest_instance.html'

    def get_context_data(self, **kwargs):
        ctx = super(SingleShowContests, self).get_context_data(**kwargs)
        ctx['title'] = Contests.objects.filter(pk=self.kwargs['pk']).first()
        return ctx


class SingleShowPastContests(DetailView):
    model = PastContests
    context_object_name = 'contests'
    template_name = 'contests/contest_instance.html'

    def get_context_data(self, **kwargs):
        ctx = super(SingleShowPastContests, self).get_context_data(**kwargs)
        ctx['title'] = PastContests.objects.filter(pk=self.kwargs['pk']).first()
        return ctx
