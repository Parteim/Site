from django.contrib import admin
from .models import Contests, PastContests, Winners, FutureContests

admin.site.register(Contests)
admin.site.register(PastContests)
admin.site.register(Winners)
admin.site.register(FutureContests)


