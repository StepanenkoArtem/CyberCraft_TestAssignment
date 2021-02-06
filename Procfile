release: pip install poetry
release: poetry export -o requirements.txt
release: python3 manage.py makemigrations && python3 manage.py migrate
web: gunicorn gh_repos.wsgi