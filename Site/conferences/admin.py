from django.contrib import admin
from .models import Conferences, ConferencesTopic


class ConferencesTopicAdmin(admin.TabularInline):
    model = ConferencesTopic


@admin.register(Conferences)
class ConferencesAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date')
    inlines = [ConferencesTopicAdmin]
