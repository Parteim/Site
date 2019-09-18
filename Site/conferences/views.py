from django.shortcuts import render
from .models import ConferencesTopic, Conferences
from django.views.generic import ListView, DetailView


def conferences(request):
    upcoming_conference = Conferences.objects.get(status='Предстоящий')
    past_conference = Conferences.objects.order_by('-date').filter(status='Прошедший')[0]

    data = {
        'upcoming_conference': upcoming_conference,
        'past_conference': past_conference,
        'winner': past_conference.conferencestopic_set.filter(status='Победитель').get(),
        'title': 'Конверенции',
    }

    return render(request, 'conferences/conferences.html', data)


class AllPastConferences(ListView):
    model = Conferences
    template_name = 'conferences/all_conferences.html'

    def get_context_data(self, **kwargs):
        ctx = super(AllPastConferences, self).get_context_data(**kwargs)
        conferences_queryset = Conferences.objects.all().filter(status='Прошедший').order_by('-date')
        ctx['title'] = 'Прошедшие конференции'
        ctx['conferences_queryset'] = conferences_queryset
        return ctx


class SingleShowConference(DetailView):
    model = Conferences
    template_name = 'conferences/conference_instance.html'

    def get_context_data(self, **kwargs):
        ctx = super(SingleShowConference, self).get_context_data(**kwargs)
        ctx['title'] = Conferences.objects.filter(pk=self.kwargs['pk']).first()
        return ctx