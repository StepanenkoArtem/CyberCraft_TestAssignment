import django_heroku

from gh_repos.settings.common import *

rollbar.report_message('Start production server', level='INFO')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')

django_heroku.settings(locals())  # noqa: WPS421
