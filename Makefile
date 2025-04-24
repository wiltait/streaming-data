export PYTHONPATH := $(shell pwd)

.PHONY: install test run clean

install:
	@echo "Setting up virtual environment..."
	python -m venv venv
	./venv/bin/pip install -r requirements.txt

test:
	@echo "Running unit tests..."
	./venv/bin/python -m unittest discover -s tests -p "test_*.py"

test-all:
	@echo "Running all tests (including integration)..."
	./venv/bin/python -m unittest discover tests

run:
	@echo "Running with default parameters..."
	./venv/bin/python src/main.py "technology"

clean:
	@echo "Cleaning up..."
	rm -rf venv
	find . -type d -name "__pycache__" -exec rm -rf {} +