.PHONY: install verify lint clean

PYTHON ?= python3

install:
	$(PYTHON) -m pip install -r requirements.txt

verify:
	$(PYTHON) code/quick_start.py

lint:
	ruff check code/ --ignore=E501,E402,F401,F841

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
