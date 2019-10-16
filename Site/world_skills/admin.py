from django.contrib import admin
from .models import WorldSkillsContest, PastWorldSkillsContest
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages

# noinspection PyUnresolvedReferences
from gallery.widgets import MultiFileInput


class PhotoAdminForm(forms.ModelForm):
    class Meta:
        model = PastWorldSkillsContest
        widgets = {'gallery_img': MultiFileInput}
        fields = '__all__'


class PastContestsWorldSkillsAdmin(admin.ModelAdmin):
    form = PhotoAdminForm
    list_display = ['past_contest']

    def add_view(self, request, form_url='', extra_context=None, *args, **kwargs):
        images = request.FILES.getlist('gallery_img', [])
        is_valid = PhotoAdminForm(request.POST, request.FILES).is_valid()

        if request.method == 'GET' or len(images) <= 1 or not is_valid:
            return super(PastContestsWorldSkillsAdmin, self).add_view(request, *args, **kwargs)

        for image in images:
            past_contest = request.POST['past_contest']
            # past_contest = WorldSkillsContest.objects.get(id=request.POST['past_contest'])
            try:
                photo = PastWorldSkillsContest(past_contest=past_contest, gallery_img=image)
                photo.save()

            except Exception as e:
                messages.error(request, e)

        return redirect('world-skills')


admin.site.register(PastWorldSkillsContest, PastContestsWorldSkillsAdmin)
admin.site.register(WorldSkillsContest)
