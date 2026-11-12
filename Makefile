name        := playfetch
specs_dir   := ./specs
out_dir     := ./out

dist_out    := $(out_dir)/dist
dist_work   := $(out_dir)/build/dist
dev_out     := $(out_dir)/dev
dev_work    := $(out_dir)/build/dev

out_binary  := $(dist_out)/$(name)
out_hash1   := $(dist_out)/SHA1SUMS
out_hash256 := $(dist_out)/SHA256SUMS

pyinstaller := uv run pyinstaller --clean --noconfirm

.DELETE_ON_ERROR:
.PHONY: dev clean clean_dev hash

_ := $(shell mkdir -p $(dist_out))
_ := $(shell mkdir -p $(dist_work))

$(out_binary): $(specs_dir) $(dist_work) $(dist_out) clean
	$(pyinstaller) --distpath $(dist_out) --workpath $(dist_work) $(specs_dir)/dist.spec

hash: $(out_hash1) $(out_hash256)

$(out_hash1): $(dist_out) $(out_binary)
	cd $(dist_out) && sha1sum $(notdir $(out_binary)) > $(notdir $@) && sha1sum -c $(notdir $@)

$(out_hash256): $(dist_out) $(out_binary)
	cd $(dist_out) && sha256sum $(notdir $(out_binary)) > $(notdir $@) && sha256sum -c $(notdir $@)

dev: clean_dev
	$(pyinstaller) --distpath $(dev_out) --workpath $(dev_work) $(specs_dir)/dev.spec

clean:
	rm -rf $(out_dir)

clean_dev:
	rm -rf $(dev_out) $(dev_work)
