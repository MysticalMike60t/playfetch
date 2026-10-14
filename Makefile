name := cspc118_final_project
entry := src/main.py

.PHONY: default build pyinstaller clean

.DELETE_ON_ERROR:
default: clean build

.DELETE_ON_ERROR:
build: pyinstaller

pyinstaller:
	uv run --with pyinstaller pyinstaller --clean build.spec

clean:
	rm -r dist build
