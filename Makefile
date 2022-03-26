lint:
	poetry run flake8 basic_code

build:
	poetry build

package-install:
	poetry install

test-coverage:
	poetry run pytest --cov=basic_code --cov-report xml

console-start:
	poetry run basic-code

start:
	export FLASK_APP=app.py
	export FLASK_ENV=development
	python -m flask run
