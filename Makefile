.PHONY: all clean run venv distclean install

all: install

run:
	@./venv/bin/pwgen

clean:
	rm -fr */__pycache__
	rm -fr *.egg-info

distclean: clean
	rm -fr venv

install: venv
	./venv/bin/pip install -e .

venv: clean
	virtualenv venv
