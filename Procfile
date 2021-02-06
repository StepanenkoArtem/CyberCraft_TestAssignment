release: python3 manage.py makemigrations && python3 manage.py migrate
heroku config:set DISABLE_COLLECTSTATIC=1
web: gunicorn gh_repos.wsgi