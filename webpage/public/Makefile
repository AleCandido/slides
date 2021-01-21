IMAGES=$(wildcard *.svg)

all: png favicon

.PHONY: all png pdf favicon

png: $(patsubst %.svg,%.png,$(IMAGES))

pdf: $(patsubst %.svg,%.pdf,$(IMAGES))

favicon: favicon.ico

%.png: %.svg
	inkscape $< --export-png $@ -w 1200

%.pdf: %.svg
	inkscape --file=$< --export-area-drawing --without-gui --export-pdf=$@

favicon.ico: favicon.svg
	inkscape $< --export-filename=x.png -w 32
	convert x.png $@
	@rm -f x.png
