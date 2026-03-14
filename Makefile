.PHONY: build venv

venv:
	python3 -m venv venv
	. venv/bin/activate && pip install pyinstaller

build: venv
	. venv/bin/activate && pyinstaller --onefile dist/test_cli.py
