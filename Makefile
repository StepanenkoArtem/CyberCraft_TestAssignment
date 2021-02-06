lint:
	poetry run flake8 gh_repos

devserver:
	poetry run ./manage.py runserver

prepare-migrate:
	poetry run ./manage.py makemigrations

migrate:
	poetry run ./manage.py migrate

test:
        poetry run python -m pytest -vv --ff

test-cov:
        poetry run python -m pytest -q --cov=yelpme tests/

coverage.xml:
        poetry run python -m pytest --cov=yelpme tests/ --cov-report=xml

.PHONY:
	test lint devserver migrate prepare-migrate test-cov