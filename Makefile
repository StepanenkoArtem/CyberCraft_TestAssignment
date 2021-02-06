test:
	poetry run pytest */tests -vv

lint:
	poetry run flake8

devserver:
	poetry run ./manage.py runserver

prepare-migrate:
	poetry run ./manage.py makemigrations

migrate:
	poetry run ./manage.py migrate

.PHONY:
	test lint devserver migrate prepare-migrate