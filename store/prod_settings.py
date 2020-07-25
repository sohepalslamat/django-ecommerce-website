from os import environ, getenv
import dj_database_url
from .settings import *

SECRET_KEY = environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['store-buy.herokuapp.com']

debug_status = environ.get('DEBUG').lower()
if debug_status == 'true':
    DEBUG = True
else:
    DEBUG = False


DATABASES = {
    'default': dj_database_url.config(
        default=environ.get('DATABASE_URL')
    )
}
# email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL ')

SENDGRID_API_KEY = getenv('SENDGRID_API_KEY')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'  # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
