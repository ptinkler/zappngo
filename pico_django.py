"""The tiniest Django project: one file is the settings, the URLs and the view.

Deploy with ``uv run zappa deploy dev``.
"""

import os
import secrets

from django.http import HttpResponse
from django.urls import re_path

DEBUG = False
ROOT_URLCONF = "pico_django"
DATABASES = {"default": {}}

# Behind API Gateway the host name is only known after the first deploy, so the default allows any host.
# Once deployed, narrow it with a comma separated ALLOWED_HOSTS in the stage's `environment_variables`.
ALLOWED_HOSTS = [host.strip() for host in os.environ.get("ALLOWED_HOSTS", "*").split(",") if host.strip()]

# Nothing here signs or stores anything, so there is no secret to keep. Django only insists on a key; a
# random one per Lambda container is fine, and DJANGO_SECRET_KEY overrides it if the app ever grows state.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY") or secrets.token_urlsafe(50)


def index(request, name):
    return HttpResponse(f"Hello, {name or 'World'}!", content_type="text/plain")


urlpatterns = [
    re_path(r"^(?P<name>[\w ]*)$", index),
]
