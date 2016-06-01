"""
WSGI config for rate_counter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/opt/bitnami/apps/django/django_projects/rate_counter/rate_counter')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/rate_counter/rate_counter/egg_cache")


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rate_counter.settings")

application = get_wsgi_application()
