install:
	pip install -r requirements.txt

lint:
	flake8 . --exclude=env*

start:
	cd ./output && python -m http.server

deploy:
	./scripts/deploy.sh

new:
	./scripts/new.py

develop:
	./scripts/develop.sh
