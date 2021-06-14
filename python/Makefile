# Makefile
.PHONY = help

help:
	@echo "---------------HELP-----------------"
	@echo "Linting and formating:"
	@echo "To lint the codebase run: make lint"
	@echo "To format the code run: make format"
	@echo ""
	@echo "Utils:"
	@echo "To compile the requirements run: make compile"
	@echo "------------------------------------"

lint:
	flake8 .
	pydocstyle pipeline
	isort --check-only .
	black --check .
	mypy gilded_rose

format:
	isort .
	black .

compile:
	pip-compile dev-requirements.in
	pip-compile requirements.in
