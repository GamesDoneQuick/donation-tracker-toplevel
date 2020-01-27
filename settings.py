import os

import environ
from django.core.urlresolvers import reverse
from django.utils.translation import gettext_lazy as _

env = environ.Env()
environ.Env.read_env()

BASE_DIR = os.path.dirname(__file__)

DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

DOMAIN = env.str('DOMAIN', default='')

PAYPAL_TEST = env.bool('PAYPAL_TEST', default=True)

# If a database URL is set, set up the db. Else, assume development
# and use sqlite.
if env.str('DATABASE_URL', default=''):
    DATABASES = {
        'default': env.db(),
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db/testdb',
        },
    }

TIME_ZONE = env.str('TIME_ZONE', default='America/New_York')

LANGUAGE_CODE = 'en-us'

# For the sites framework. We should get rid of this someday.
SITE_ID = 1

# Add to this list if you have added localization for more languages.
LANGUAGES = (
#   ('de', _('German')),
	('en', _('English')),
#   ('jp', _('Japanese')),
)

# Always use timezone-aware datetimes and localize all dates and times.
USE_TZ = True
USE_L10N = True

MEDIA_ROOT = env.str('MEDIA_ROOT', default='')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = env.str('MEDIA_URL', default='/media/')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
if env.str('STATIC_ROOT', default=None):
    STATIC_ROOT = env.path('STATIC_ROOT')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
if env.str('STATIC_URL', default=None):
    STATIC_URL = env.str('STATIC_URL')

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.abspath('tracker/static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = env.str('SECRET_KEY')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                "tracker.context_processors.booleans",
            ],
            'debug': DEBUG,
            'string_if_invalid': 'Invalid Variable: %s',
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SESSION_COOKIE_NAME = 'tracker_session'

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'post_office',
    'paypal.standard.ipn',
    'tracker',
    'timezone_field',
    'ajax_select',
    'mptt',
] + env.list('ADDITIONAL_APPS', default=[])

# Pull in the tracker's lookup channels
from tracker.ajax_lookup_channels import AJAX_LOOKUP_CHANNELS

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'tracker.auth.EmailLoginAuthBackend',
)

AUTH_PROFILE_MODULE = 'tracker.UserProfile'

LOGIN_URL = 'tracker:login'
LOGIN_REDIRECT_URL = 'tracker:user_index'

if env.bool('HAS_EMAIL', default=False):
  EMAIL_HOST = env.str('EMAIL_HOST')
  EMAIL_PORT = env.str('EMAIL_PORT')
  EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
  EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
  MANDRILL_API_KEY = env.str('EMAIL_HOST_PASSWORD') # the API key is the same as the SMTP password
  EMAIL_FROM_USER = env.str('EMAIL_FROM_USER')

if env.bool('HAS_GOOGLE_APP_ID', default=False):
    GOOGLE_CLIENT_ID = env.str('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = env.str('GOOGLE_CLIENT_SECRET')

if env.bool('HAS_GIANTBOMB_API_KEY', default=False):
  GIANTBOMB_API_KEY = env.str('GIANTBOMB_API_KEY')

if env.bool('HAS_FILE_STORAGE', default=False):
    DEFAULT_FILE_STORAGE = env.str('DEFAULT_FILE_STORAGE')

if env.bool('HAS_AWS_FILE_STORAGE', default=False):
    AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env.str('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = env.str('AWS_DEFAULT_ACL')

SWEEPSTAKES_URL = env.str('SWEEPSTAKES_URL', default='')
PRIVACY_POLICY_URL = env.str('PRIVACY_POLICY_URL', default='')
GOOGLE_ANALYTICS = env.tuple('GOOGLE_ANALYTICS', default=None)

TRACKER_PAGINATION_LIMIT = env.int('TRACKER_PAGINATION_LIMIT', default=500)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
#        'file': {
#            'level': 'ERROR',
#            'class': 'logging.FileHandler',
#            'filename': '/var/log/uwsgi/django-error.log',
#        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        # 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 'LOCATION': '/var/tmp/django_cache',
    }
}
