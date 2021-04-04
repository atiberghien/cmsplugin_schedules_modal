from django.contrib import admin
from .models import Announcement, AnnouncementAttachment


class AnnouncementAttachmentInline(admin.TabularInline):
    model = AnnouncementAttachment

class AnnouncementAdmin(admin.ModelAdmin):
    inlines = [AnnouncementAttachmentInline] 
    list_display = ('title', 'begin_date', 'end_date', 'show_period')
    list_editable = ('begin_date', 'end_date', 'show_period')

    fieldsets = (
        (None, {
            'fields': (('begin_date', 'end_date', 'show_period'), 'title', 'text')
        }),
    )

    class Media:
        css = {
            'all': ('css/admin/announcement.css',)
        }


admin.site.register(Announcement, AnnouncementAdmin)
# admin.site.register(AnnouncementAttachment)
