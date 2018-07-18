#-*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models import CMSPlugin
from .models import Announcement

from datetime import datetime

@plugin_pool.register_plugin  # register the plugin
class ScheduledModalPlugin(CMSPluginBase):
    module = u"Modal programmée"
    name = u"Modal programmée"
    render_template = "scheduled_modal/scheduled_modal.html"

    def render(self, context, instance, placeholder):
        today = datetime.now()
        context.update({
            'announcements': Announcement.objects.filter(begin_date__lte=today, end_date__gte=today)
        })
        return context
