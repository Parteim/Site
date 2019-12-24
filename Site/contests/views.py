from django.shortcuts import render, redirect
from .models import Contests, Participants
from django.shortcuts import get_list_or_404
from django.views.generic import ListView, DetailView
from .forms import ParticipantForm


def ShowContestsPage(request):
    if request.method == 'POST':
        user_valid = request.user.profile.studentprofile
        form = ParticipantForm()
        if user_valid.age == 0 or user_valid.course == 0 or user_valid.faculty == 'Не указан':
            return redirect('change-profile')
        contest_name = request.POST.get('contest')
        contest = Contests.objects.filter(title=contest_name)[0]
        Participants.objects.create(contest=contest, user=request.user)
    data = {
        'participant_form': ParticipantForm(),
        'past_contests': Contests.objects.all().filter(status='Прошедший').order_by('-date')[:5],
        'contests': Contests.objects.all().filter(status='Предстоящий').order_by('-date'),
        'title': 'Конкурсы',
    }

    return render(request, 'contests/contests.html', data)


class ShowContests(ListView):
    model = Contests
    template_name = 'contests/all_contests.html'

    def get_context_data(self, **kwargs):
        ctx = super(ShowContests, self).get_context_data(**kwargs)
        ctx['title'] = 'Все конкурсы'
        ctx['Contests'] = Contests.objects.all().filter(status='Предстоящий').order_by('-date')
        return ctx


class ShowPastContests(ListView):
    model = Contests
    template_name = 'contests/all_contests.html'

    def get_context_data(self, **kwargs):
        ctx = super(ShowPastContests, self).get_context_data(**kwargs)
        ctx['title'] = 'Прошедшие конкурсы'
        ctx['Contests'] = Contests.objects.all().filter(status='Прошедший').order_by('-date')
        return ctx


class SingleShowContests(DetailView):
    model = Contests
    template_name = 'contests/contest_instance.html'

    def get_context_data(self, **kwargs):
        ctx = super(SingleShowContests, self).get_context_data(**kwargs)
        ctx['title'] = Contests.objects.filter(pk=self.kwargs['pk']).first()
        return ctx
