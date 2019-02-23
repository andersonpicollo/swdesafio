GIT_CURRENT_BRANCH := @git symbolic-ref --short HEAD

.PHONY: help clean test run

.DEFAULT: help

help:
	@echo "make clean:"
	@echo "       Removes all pyc, pyo and __pycache__"
	@echo ""
	@echo "make test:"
	@echo "       Run tests with and clean commands"
	@echo ""
	@echo "make dev:"
	@echo "       Run the dev web application, with tests"
	@echo ""
	@echo "make run:"
	@echo "       Run the web application without tests"
	@echo ""
	@echo ""

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . | grep -E "__pycache__|.pytest_cache|.pyc|.DS_Store$$" | xargs rm -rf
test: clean
	@pytest --verbose  --color=yes tests/

dev: clean test
	python application.py

run:
	python application.py
