lint:
	poetry run flake8 gh_repos

devserver:
	poetry run ./manage.py runserver

prepare-migrate:
	poetry run ./manage.py makemigrations

migrate:
	poetry run ./manage.py migrate

test:
	poetry run python -m pytest tests -vv --ff -s

test-cov:
	poetry run python -m pytest -q --cov=tests

coverage.xml:
	poetry run python -m pytest --cov=tests --cov-report=xml

.PHONY:
	test lint devserver migrate prepare-migrate test-cov
