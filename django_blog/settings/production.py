from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['djangoblogfdo.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd53u4bf4bgod29',
        'USER': 'jhdskrjbuutbed',
        'PASSWORD': '51fb4ea815897477ef6281e0bd45b03ae5860fd8b083f49d857134514ff782fb',
        'HOST': 'ec2-34-201-248-246.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATICFILES_DIRS = (BASE_DIR,'static')
