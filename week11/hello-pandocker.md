---
author: you
date: now
title: Hello, Pandocker!
toc-own-page: true
toccolor: blue
titlepage: true
pandoc-latex-admonition:
    - color: firebrick
      classes: [admonition, danger]
    - color: gray
      classes: [admonition]
---

Stuff about Pandocker
=====================

Pandocker is pretty cool and comes with support for a lot of different things,
including:

* A filter for PDF output to show important information (admonitions)
* A template (Eisvogel) that makes your PDFs look *great*

[Font Awesome]: https://fontawesome.com/

Using Admonitions
=================

::: {.admonition .danger}

Pandocker requires that you have [Docker] installed on your machine.

[Docker]: https://docker.com

:::

::: {.admonition}

This is a regular admonition, there should be a gray line on the left side to
bring attention to it

:::

Making a PDF from this file
===========================

1. Install Docker.
2. Run a Pandocker container.

On Windows
----------

```bash
docker run --rm -v ${PWD}:/pandoc dalibo/pandocker:stable `
    hello-pandocker.md -o hello-pandocker.pdf `
    --filter pandoc-latex-admonition --template eisvogel `
    --toc --pdf-engine=xelatex --listings
```

On Linux or macOS
-----------------

```bash
docker run --rm -v `pwd`:/pandoc dalibo/pandocker:stable \
    hello-pandocker.md -o hello-pandocker.pdf \
    --filter pandoc-latex-admonition --template eisvogel \
    --toc --pdf-engine=xelatex --listings
```
