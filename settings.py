# Django settings for donations project.

import local
from django.core.urlresolvers import reverse
import itertools
import os

BASE_DIR = os.path.dirname(__file__)

DEBUG = local.DEBUG
TEMPLATE_DEBUG = DEBUG
TEMPLATE_STRING_IF_INVALID = 'Invalid Variable: %s'

ALLOWED_HOSTS = local.ALLOWED_HOSTS

DOMAIN = local.DOMAIN

ADMINS = local.ADMINS

MANAGERS = ADMINS

DATABASES = local.DATABASES

SITE_PREFIX = local.SITE_PREFIX

LOGIN_URL = SITE_PREFIX + 'user/login/'
LOGIN_REDIRECT_URL = SITE_PREFIX + 'user/index/'
LOGOUT_REDIRECT_URL = SITE_PREFIX + 'index/'

# Append slash seems to be the way to go overall
APPEND_SLASH = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = local.TIME_ZONE

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

gettext = lambda x: x
LANGUAGES = (
#	('de',gettext('German')),
	('en',gettext('English')),
#	('ja',gettext('Japanese')),
#	('nl',gettext('Dutch')),
#	('pl',gettext('Polish')),
)

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = local.STATIC_ROOT

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = local.STATIC_URL #'/static/'

# Additional locations of static files
STATICFILES_DIRS = local.STATICFILES_DIRS

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = local.SECRET_KEY

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
)

SESSION_COOKIE_NAME = 'tracker_session'

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "tracker.context_processors.booleans",
)

INSTALLED_APPS = (
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
    'tracker_ui',
    'timezone_field',
    'ajax_select',
    'mptt',
)

EMAIL_BACKEND = local.EMAIL_BACKEND

#You will also want to add the following to your server's crontab:
# * * * * * ($DONATIONS_LOCATION/manage.py send_queued_mail >> send_mail.log 2>&1)

# Pull in the tracker's lookup channels
from tracker.ajax_lookup_channels import AJAX_LOOKUP_CHANNELS

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'tracker.auth.EmailLoginAuthBackend',
)

AUTH_PROFILE_MODULE = 'tracker.UserProfile'

if local.HAS_GDOC:
  GDOC_USERNAME = local.GDOC_USERNAME
  GDOC_PASSWORD = local.GDOC_PASSWORD

if local.HAS_EMAIL:
  EMAIL_HOST = local.EMAIL_HOST
  EMAIL_PORT = local.EMAIL_PORT
  EMAIL_HOST_USER = local.EMAIL_HOST_USER
  EMAIL_HOST_PASSWORD = local.EMAIL_HOST_PASSWORD
  MANDRILL_API_KEY = local.EMAIL_HOST_PASSWORD # the API key is the same as the SMTP password
  EMAIL_FROM_USER = local.EMAIL_FROM_USER

if local.HAS_GOOGLE_APP_ID:
  GOOGLE_CLIENT_ID = local.GOOGLE_CLIENT_ID
  GOOGLE_CLIENT_SECRET = local.GOOGLE_CLIENT_SECRET

if local.HAS_GIANTBOMB_API_KEY:
  GIANTBOMB_API_KEY = local.GIANTBOMB_API_KEY

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
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
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}
