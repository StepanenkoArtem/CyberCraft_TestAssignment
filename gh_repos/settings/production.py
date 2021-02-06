import django_heroku

from gh_repos.settings.common import *

django_heroku.settings(locals())  # noqa: WPS421
