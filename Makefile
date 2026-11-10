name        := playfetch
specs_dir   := ./specs
out_dir     := ./out
rust_pkg    := playfetchlib

dist_out    := $(out_dir)/dist
dist_work   := $(out_dir)/build/dist
dev_out     := $(out_dir)/dev
dev_work    := $(out_dir)/build/dev

pyinstaller := uv run pyinstaller --clean --noconfirm

.DELETE_ON_ERROR:
.PHONY: default build dev rust rust-force clean clean_dev

default: clean build

build: rust
	$(pyinstaller) --distpath $(dist_out) --workpath $(dist_work) $(specs_dir)/dist.spec

dev: clean_dev rust
	$(pyinstaller) --distpath $(dev_out) --workpath $(dev_work) $(specs_dir)/dev.spec

rust:
	uv sync

rust-force:
	uv sync --reinstall-package $(rust_pkg)

clean:
	rm -rf $(out_dir)

clean_dev:
	rm -rf $(dev_out) $(dev_work)
