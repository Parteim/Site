from django.contrib import admin
from .models import Contests, Participants


class ParticipantsAdmin(admin.TabularInline):
    model = Participants


@admin.register(Contests)
class ContestsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    inlines = [ParticipantsAdmin]
