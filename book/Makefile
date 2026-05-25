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
		--toc --lua-filter=filters/diagram.lua

styles.css:
	cat styles/*.css > styles.css

.PHONY: clean

clean: 
	rm -rf toolsntechniques styles.css
