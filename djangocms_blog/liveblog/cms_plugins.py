# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.cms_plugins import TextPlugin

from djangocms_blog.settings import get_setting

from .models import Liveblog


class LiveblogPlugin(TextPlugin):
    module = get_setting('PLUGIN_MODULE_NAME')
    name = _('Liveblog item')
    model = Liveblog

    def _get_render_template(self, context, instance, placeholder):
        if instance.publish:
            return 'liveblog/plugins/liveblog.html'
        else:
            return 'liveblog/plugins/unpublished.html'

    def render(self, context, instance, placeholder):
        context = super(LiveblogPlugin, self).render(context, instance, placeholder)
        instance.content = context['body']
        context['instance'] = instance
        return context

plugin_pool.register_plugin(LiveblogPlugin)
