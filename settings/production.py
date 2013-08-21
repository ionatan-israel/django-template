#encoding:utf-8
"""Production settings and globals."""
from settings.base import *
import dj_database_url


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG


########## DATABASE CONFIGURATION
DATABASES = {
    'default': dj_database_url.config()
}
########## END DATABASE CONFIGURATION


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS += [
    'south',
]

####################################
### CONFIGURACION DE CORREO
"""
EMAIL_HOST = '127.0.0.1'
MAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False
"""
