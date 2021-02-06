release: python3 manage.py makemigrations && python3 manage.py migrate
release: python3 manage.py collectstatic
web: gunicorn gh_repos.wsgi