import django_heroku

from gh_repos.settings.common import *

rollbar.report_message('Start production server', level='INFO')

django_heroku.settings(locals())  # noqa: WPS421
