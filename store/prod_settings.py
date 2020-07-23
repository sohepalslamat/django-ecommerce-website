from os import environ
import dj_database_url
from .settings import *

SECRET_KEY = environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['https://store-buy.herokuapp.com']

DEBUG = False


DATABASES = {
    'default': dj_database_url.config(
        default=environ.get('DATABASE_URL')
    )
}
