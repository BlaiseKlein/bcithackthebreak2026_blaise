.PHONY: build venv run clean

venv:
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install -r requirements.txt

build: venv
	# Optional: Build with pyinstaller if needed
	@echo "Build complete. Virtual environment is ready."

run: venv
	. venv/bin/activate && python GUI/app.py

clean:
	rm -rf venv
	rm -rf dist
	rm -rf build
	rm -rf *.spec

# Default target when just running 'make'
all: venv
	@echo "Virtual environment is ready. Run 'make run' to start the app."