
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")

SECRET_KEY = os.environ.get("SECRET_KEY")
STRIPE_PUBLISHABLE = os.environ.get("STRIPE_PUBLISHABLE")
STRIPE_SECRET = os.environ.get("STRIPE_SECRET")
EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")

application = get_wsgi_application()
