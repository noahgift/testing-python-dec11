setup:
	#### You may want to use this convention
	#python -m venv ~/.testing-python-dec11
	#### To use this do this:
	# source ~/.testing-python-dec11/bin/activate
	### To deactivate do this
	# deactivate

install:
	# This upgrades pip to the latest version and run requirements.txt
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C mylib

flakeit:
	flake8 mylib

reformat:
	black cli.py mylib/lib.py

test:
	python -m pytest -vv --cov=mylib --cov=cli tests/*.py

all: install flakeit lint test