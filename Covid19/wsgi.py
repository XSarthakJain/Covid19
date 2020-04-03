"""
WSGI config for Covid19 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

path="/home/xsarthak/Covid19"
if path not in sys.path:
    sys.path.insert(0,path)#todo


os.environ['DJANGO_SETTINGS_MODULE'] = 'Covid19.settings'
from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application


application = StaticFilesHandler(get_wsgi_application())
