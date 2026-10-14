name := cspc118_final_project
entry := src/main.py

.DELETE_ON_ERROR:
build: pyinstaller

pyinstaller:
	uv run --with pyinstaller pyinstaller build.spec

.PHONY: clean
clean:
	rm -r dist build
