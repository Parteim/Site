from django.contrib import admin
from django import forms
from .models import Photo
from .widgets import MultiFileInput
from django.shortcuts import render, redirect
from django.contrib import messages


class PhotoAdminForm(forms.ModelForm):
    class Meta:
        model = Photo
        widgets = {'img': MultiFileInput}
        fields = '__all__'


class PhotoAdmin(admin.ModelAdmin):
    form = PhotoAdminForm

    def add_view(self, request, form_url='', extra_context=None, *args, **kwargs):
        images = request.FILES.getlist('img', [])
        is_valid = PhotoAdminForm(request.POST, request.FILES).is_valid()

        if request.method == 'GET' or len(images) <= 1 or not is_valid:
            return super(PhotoAdmin, self).add_view(request, *args, **kwargs)

        for image in images:
            description = request.POST['description']
            try:
                photo = Photo(description=description, img=image)
                photo.save()
            except Exception as e:
                messages.error(request, e)

        return redirect('gallery')


admin.site.register(Photo, PhotoAdmin)
