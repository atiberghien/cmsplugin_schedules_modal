from django.contrib import admin
from .models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'begin_date', 'end_date', 'show_period')
    list_editable = ('begin_date', 'end_date', 'show_period')


admin.site.register(Announcement, AnnouncementAdmin)
