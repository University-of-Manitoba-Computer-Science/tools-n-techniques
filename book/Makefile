all: book-html 

book-html: clean styles.css
	pandoc index.md **/*.md -t chunkedhtml -f markdown+emoji -o toolsntechniques \
		--resource-path=topic01:topic02:topic03:topic04:topic05:topic06:topic07:topic08:topic09:topic10:topic11:topic12:. \
		--katex --toc-depth=2 --split-level=2 -V toc  --embed-resources --standalone --css=./styles.css \
		--lua-filter=filters/diagram.lua --template=templates/template.html -V abstract-title= --section-divs=true \
		--lua-filter=filters/toc.lua
	cp styles.css toolsntechniques/
	cp templates/github.svg toolsntechniques/

book-typst: 
	pandoc index.md **/*.md -t pdf --pdf-engine=typst -f markdown+emoji -o book.pdf \
		--resource-path=topic01:topic02:topic03:topic04:topic05:topic06:topic07:topic08:topic09:topic10:topic11:topic12:. \
		--toc --lua-filter=filters/diagram.lua --lua-filter=filters/toc.lua --lua-filter=filters/typst-latex-logo.lua \
		-V header-includes='#import "@preview/metalogo:1.2.0": TeX, LaTeX' -V linkcolor='0000ff' \
		-H templates/headers.typst --toc-depth 2

book-typst-src: 
	pandoc index.md **/*.md -t typst --standalone -f markdown+emoji -o book.typ \
		--resource-path=topic01:topic02:topic03:topic04:topic05:topic06:topic07:topic08:topic09:topic10:topic11:topic12:. \
		--toc --lua-filter=filters/diagram.lua --lua-filter=filters/toc.lua --lua-filter=filters/typst-latex-logo.lua \
		-V header-includes='#import "@preview/metalogo:1.2.0": TeX, LaTeX' -V linkcolor='0000ff' \
		-H templates/headers.typst

styles.css:
	cat styles/*.css > styles.css

.PHONY: clean

clean: 
	rm -rf toolsntechniques styles.css
