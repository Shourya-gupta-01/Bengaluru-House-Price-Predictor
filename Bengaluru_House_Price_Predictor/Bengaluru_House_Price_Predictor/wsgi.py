"""
WSGI config for Bengaluru_House_Price_Predictor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bengaluru_House_Price_Predictor.settings')

application = get_wsgi_application()

app=application
