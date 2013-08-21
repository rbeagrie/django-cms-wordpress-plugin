from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from models import Post, WordpressPosts

class WordpressPostsPlugin(CMSPluginBase):
    model = WordpressPosts
    render_template = "posts_plugin.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
	context['posts'] = Post.objects.filter(site_id=instance.site_id)[:instance.max_posts]
        return context

plugin_pool.register_plugin(WordpressPostsPlugin)
