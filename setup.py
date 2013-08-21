#!/usr/bin/env python

from distutils.core import setup

setup(name='django_cms_wordpress_plugin',
      version='0.1',
      description='Plugin to display posts from a wordpress hosted blog through the JSON API',
      author='Rob Beagrie',
      author_email='rob@beagrie.com',
      url='https://github.com/rbeagrie/django-cms-wordpress-plugin',
      packages=['wordpress_plugin'],
     )
