name := cspc118_final_project
entry := src/main.py
specs_folder := ./specs
output_dir := ./out
dist_dir := dist
dev_dir := dev
pyinstaller_build_cmd := uv run --with pyinstaller pyinstaller --clean --distpath ${output_dir}/${dist_dir} --workpath ${output_dir}/${build_dir}

.PHONY: default build dev clean clean_dev

.DELETE_ON_ERROR:
default: clean build_dist

.DELETE_ON_ERROR:
build: build_dist

build_dist:
	${pyinstaller_build_cmd} ${specs_folder}/dist.spec

dev: clean_dev build_dev

build_dev:
	${pyinstaller_build_cmd} ${specs_folder}/dev.spec

clean:
	rm -rf ${output_dir}/${build_dir} ${output_dir}/${dist_dir}

clean_dev:
	dir="${output_dir}/${build_dir}/dev"
	rm -rf "$${dir}"
