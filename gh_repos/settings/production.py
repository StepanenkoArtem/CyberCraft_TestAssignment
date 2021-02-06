from gh_repos.settings.common import *

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': os.getenv('GH_REPOS_DB_PORT'),
        'USER': os.getenv('GH_REPOS_DB_USER'),
        'PASSWORD': os.getenv('GH_REPOS_DB_PASS'),
    },
}
