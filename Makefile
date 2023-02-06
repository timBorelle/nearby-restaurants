.ONESHELL:

SHELL := /bin/bash
BIN=venv/bin/
ACTIVATE_LINUX:=. venv/bin/activate

venv:
	: # Create venv if it doesn't exist
	test -d venv || python3 -m venv venv

install: venv
	chmod +x venv/bin/activate
	@$(ACTIVATE_LINUX)

deps: install
	$(BIN)pip3 install -r requirements.txt

test:
	pytest

clean:
	deactivate
	rm -rf venv
