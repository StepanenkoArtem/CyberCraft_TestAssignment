release: heroku config:set DISABLE_COLLECTSTATIC=1
release: python3 manage.py makemigrations && python3 manage.py migrate
web: gunicorn gh_repos.wsgi