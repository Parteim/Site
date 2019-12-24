from django.shortcuts import render
from .models import WorldSkillsContest
from django.views.generic import (
    View,
    DetailView,
)


class WorldSkills(View):
    def get(self, request):
        ctx_data = {
            'title': 'WorldSkills',
            'contest': WorldSkillsContest.objects.all().filter(status='Предстоящий').first(),
            'Past_contest': WorldSkillsContest.objects.all().filter(status='Прошедший').order_by('-date').first(),
        }
        return render(request, 'world_skills\world_skills.html', ctx_data)


class InstanceWorldSkills(DetailView):
    model = WorldSkillsContest
    template_name = 'world_skills\instance_contest_world_skills.html'

    def get_context_data(self, **kwargs):
        ctx = super(InstanceWorldSkills, self).get_context_data(**kwargs)
        ctx['title'] = self.model.objects.filter(pk=self.kwargs['pk']).first()
        return ctx
