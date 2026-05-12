all: book

book: styles.css
	pandoc index.md **/*.md -t chunkedhtml -f markdown+emoji -o toolsntechniques \
		--resource-path=topic01:topic02:topic03:topic04:topic05:topic06:topic07:topic08:topic09:topic10:topic11:topic12:. \
		--katex --toc-depth=2 --split-level=2 --toc  --embed-resources --standalone --css=./styles.css
	cp styles.css toolsntechniques/

styles.css:
	cat styles/*.css > styles.css

.PHONY: clean

clean: 
	rm -rf toolsntechniques
