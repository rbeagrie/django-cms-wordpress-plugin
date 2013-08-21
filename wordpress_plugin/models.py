from wordpress_api_models import Post
from cms.models.pluginmodel import CMSPlugin

from django.db import models

class WordpressPosts(CMSPlugin):
    site_id = models.IntegerField(default=54754621)
    max_posts = models.IntegerField(default=20)

