#!/usr/bin/env python3
import django
from django.conf import settings
from django.core.management import call_command

APP_NAME = 'django_navbar_client'


settings.configure(
    DEBUG=True,
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django_navbar_client',
    ),
    ORION_BROKER='',
    ORION_URL='',
    ORION_SCOPE='',
    SCOPE='',
)

django.setup()
call_command('makemigrations', APP_NAME)
