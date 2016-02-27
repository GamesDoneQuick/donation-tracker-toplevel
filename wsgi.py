import os
import sys
import logging
import inspect

# I put it ahead so that it will take the local paypal app over the global one
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
os.environ.setdefault("LC_ALL", "en_US.utf8")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

logger = logging.getLogger('')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

