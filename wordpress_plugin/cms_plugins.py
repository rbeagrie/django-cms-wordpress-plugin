from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from models import WordpressPosts
from wordpress.models import Post
import string

def sanitize_string(my_string):
    return ''.join([ c for c in my_string if c in string.printable ])

def excerptize_string(my_string):
    words = my_string.split()
    words = words[:50]
    words.append(u'...')
    words = u' '.join(words)
    return sanitize_string(words)

class WordpressPostsPlugin(CMSPluginBase):
    model = WordpressPosts
    render_template = "posts_plugin.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
	posts = Post.objects.published()[:instance.max_posts]
        posts = [ {'title':sanitize_string(p.title),
                   'excerpt':excerptize_string(p.content),
                   #'date':'this is my date',
                   'date':p.post_date,
                  } for p in posts]

	context['posts'] = posts
        return context

plugin_pool.register_plugin(WordpressPostsPlugin)
