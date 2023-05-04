---
title: Write plain text documents
author: Franklin Bristow
---


Write plain text documents
==========================

::: outcomes

* [X] Write plain text documents (including code and formulas) using structured
  markup formats (Markdown and $\LaTeX$).

:::

[A lot] of the stuff that we create in computer science is formatted as [plain
text] --- all the source code that we write in Java, Python, Processing, and C
(for example) are plain text documents.

Plain text documents (`.txt` files!) don't really seem that useful at first
glance, but really are very useful:

* Writing plain text files to describe how to build and use software is common
  in industry (`README` files).
* Plain text files can be opened and read in almost all environments, including
  ones that don't have a graphical user interface (like your terminal).
* Plain text is a format that's long-lived (you can still open and read plain
  text files written in the 90s in modern computing environments today; you
  can't open many word processor formats from the same time today).
* Plain text plays a lot more nicely with version control (we'll get there!).
* Writing in plain text lets you focus on more on writing and less on
  formatting.

All that said, plain text documents are, well, plain.

* You can't add *emphasis* to certain words. 
* You can't easily
  1. Make
  2. Numbered
  3. Lists
  4. Of
  5. Things.
* You can't embed

  ```c
  #include <stdio.h>
  int main(void)
  {
    printf(" source code.\n");
    return EXIT_SUCCESS;
  }
  ```
* You certainly can't include ![A picture of the word
  "images".](images.png){style='height: 1em'}.
* You **definitely** can't include fancy formulas:

  $$
  x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2ac}
  $$

We're going to be writing in this course, and you will be doing all of your
writing in this course in **plain text**. When you write in plain text, you're
going to be doing *everything* that we listed above. In fact, this document was
originally written as [a plain text document]!

Plain text in and of itself won't let us do those things very easily, so we need
to write plain text, but write the plain text such that we're following
structured text standards: Markdown and $\LaTeX$.

[plain text]: https://en.wikipedia.org/wiki/Plain_text
[a plain text document]: topic-3.md

Writing in Markdown
-------------------

Writing [Markdown]-formatted plain text documents is pretty straightforward:
Open up VS Code, create a new file, and start writing words.

::: example

Here, write this into VS Code:

```
Hi! It's me! I'm writing Markdown-formatted plain text! Yay!
```

:::

Congratulations :tada:! You just wrote some Markdown!

OK, so it's not really that exciting. And hey! We didn't even do any of those
things that I said we would do above, what gives?

Adding some flair to your writing in Markdown isn't really much more than doing
what we just did:

* [Titles]
* [Emphasis]
* [Lists]
* [Code]
* [Images and links]

[Markdown]: https://en.wikipedia.org/wiki/Markdown

### Titles

Most documents have a title, or headings and subheadings (and subsubheadings).

You've got two options for making headings in Markdown:

1. Use underlines (`===` or `---`).
2. Use number signs or hashes (`#`, `##`, `###`).

::: example

Here are some examples:

:::::: columns
::: {.column .input width=50%}

```markdown
Top level heading
=================

Here's some text under the top level
heading.

Second level heading
--------------------

Here's some text under the second 
level heading.

### Third level heading

There's only so many levels of 
underlines, so you have to switch 
to using number signs if you want 
3+-level headings.

# Top

More text under a top level heading.

## Second

Some text under a different kind 
of second level heading.

### Third

More text under a third level 
heading.
```

:::
::: {.column .output width=50%}
Top level heading
=================

Here's some text under the top level
heading.

Second level heading
--------------------

Here's some text under the second 
level heading.

### Third level heading

There's only so many levels of 
underlines, so you have to switch 
to using number signs if you want 
3+-level headings.

# Top

More text under a top level heading.

## Second

Some text under a different kind 
of second level heading.

### Third

More text under a third level 
heading.

:::
::::::

Pick whichever style you want and stick with it. I prefer to use underlines
because I think it's more obvious, but has the downside of being limited to
two levels of heading and subheading.

:::

### Emphasis

If you want to add emphasis (*italic*) to text in Markdown, you put asterisks `*`
around the text:

::: example

:::::: columns
::: {.column .input width=50%}

```markdown
The word emphasis has *emphasis*.
```

:::
::: {.column .output width=50%}
The word emphasis has *emphasis*.
:::

::::::

:::

If you want to add emphasis (**bold**) to text in Markdown, you put *two* asterisks
`**` around the text:

::: example

:::::: columns
::: {.column .input width=50%}

```markdown
Some text doesn't need emphasis,
**some text needs to be bold**.
```

:::
::: {.column .output width=50%}
Some text doesn't need emphasis,
**some text needs to be bold**.
:::
::::::

:::

### Lists

There are two kinds of lists you can format in Markdown: Bullets and numbered
lists. Bulleted lists use the asterisk symbol at the beginning of a line,
numbered lists are a number followed by a period:

::: example

:::::: columns
::: {.column .input width=50%}

```markdown
* This is
* A bulleted list
* In Markdown.

1. This is
2. A numbered list
3. In Markdown.
```

:::
::: {.column .output width=50%}
* This is
* A bulleted list
* In Markdown.

1. This is
2. A numbered list
3. In Markdown.

:::
::::::

:::

### Code

You can put code (or any content that shouldn't be formatted) in "fences". A
fence is a section in your plain text that's surrounded by two lines that have
just three backticks (`\``). If what you're putting into the fence is source
code for a specific programming language, you can indicate which language it is
by writing the language name in lower case letters just after the first fence:

::: example

:::::: columns
::: {.column .input width=50%}
<pre><code>
Plain text:

```
Here's some plain-text that's not formatted.
```

Some Java:

```java
public static void main(String... args)
{
  System.out.println("Hello, world!");
}
```

Some Python:

```python
# it's embarrassing (for Java)
# how much shorter this is
print("Hi")
```
</code></pre>
:::
::: {.column .output width=50%}
Plain text:

```
Here's some plain-text that's not formatted.
```

Some Java:

```java
public static void main(String... args)
{
  System.out.println("Hello, world!");
}
```

Some Python:

```python
# it's embarrassing (for Java)
# how much shorter this is
print("Hi")
```

:::
::::::

:::

### Images and links

You unfortunately can't copy and paste a picture into your Markdown document in
the same way you can with something like Word, but you can still *refer* to an
image and have that image appear when [converting documents to different
formats] like PDF or `docx`.

Referring to an image in Markdown uses a "link": some text that will appear as
the caption or description of the image and the file name for the image (e.g.,
`jpg`, `gif`, `png`):

::: example

:::::: columns
::: {.column .input width=50%}

```markdown
Here's a cool picture:

![The word "images".](images.png)
```

:::
::: {.column .output width=50%}

Here's a cool picture:

![The word "images".](images.png)

:::
::::::

The file `images.png` has to be in the same folder as the Markdown-formatted
text file.

:::


You can also make links to web pages using the same syntax, but without the
leading `!`:

::: example

:::::: columns
::: {.column .input width=50%}

```markdown
You can get to UM Learn by clicking this
[link to UM Learn](https://umlearn.ca),
and it will open in your web browser.
```

:::
::: {.column .output width=50%}
You can get to UM Learn by clicking this [link to UM Learn](https://umlearn.ca),
and it will open in your web browser.

:::
::::::

:::

Another format for writing links to web pages is to separate the address from
the text you want displayed:

::: example

:::::: columns
::: {.column .input width=50%}

```markdown
You can get to UM Learn by clicking this
[link to UM Learn], and it will open in
your web browser.

[link to UM Learn]: https://umlearn.ca
```

:::
::: {.column .output width=50%}
You can get to UM Learn by clicking this [link to UM Learn], and it will open in
your web browser.

[link to UM Learn]: https://umlearn.ca

:::
::::::

:::

Writing in $\LaTeX$
-------------------

Finally, we want to be able to write fancy formulas in our plain text document.
Unfortunately, Markdown doesn't have syntax to support writing fancy formulas in
and of itself. Fortunately, we can embed a *different* text format in our plain
text documents that *does* have syntax for writing fancy formulas, and that text
format is called $\LaTeX$.

::: aside

$\LaTeX$ is pronounced "Lah-tek", the $X$ in $\LaTeX$ is not [the latin letter
X], but is instead [the Greek letter Chi]).

:::

We can embed $\LaTeX$ in Markdown using some simple syntax:

::: example

Single dollar signs around an expression will put that expression on the same
line as the text you're writing:

:::::: columns
::: {.column .input width=50%}

```markdown
For example, $x + 2$ is right on the
same line as everything else.
```

:::
::: {.column .output width=50%}

For example, $x + 2$ is right on the same line as everything else.

:::
::::::

Double dollar signs around an expression will put it on its own line and
centered:

:::::: columns
::: {.column .input width=50%}
```markdown
For example, this is a fancy expression:

$$
x + 2
$$
```

:::
::: {.column .output width=50%}
For example, this is a fancy expression:

$$
x + 2
$$
:::
::::::

:::

We want to be able to accomplish a few things with $\LaTeX$:

* Write simple expressions with variables, superscripts, and subscripts.
* Write expressions that include fractions.
* Write expressions that include sequences (e.g., sums and products).
* Write expressions that include common CS symbols (e.g., the $\mathcal{O}$ in "big O").

[the latin letter X]: https://en.wikipedia.org/wiki/X
[the Greek letter Chi]: https://en.wikipedia.org/wiki/Chi_(letter)

### Simple expressions

Writing simple expressions with variables is straightforward, just wrap the
expression with the appropriate number of dollar signs (\$) and write it out:

::: example

:::::: columns
::: {.column .input width=50%}

```latex
$$
x + y + 10
$$
```

:::
::: {.column .output width=50%}


$$
x + y + 10
$$

:::
::::::

:::

To make a value a superscript (like an exponent), you need to use the caret
symbol (^). To make a value subscript (like an index), you need to use the
underscore (\_) symbol. Then wrap the value you want to be superscripted or
subscripted in curly braces ({}):

::: example

:::::: columns
::: {.column .input width=50%}

```latex
$$
x_{1}^{2} + y^{n+4} + z_{0} + 10
$$
```

:::
::: {.column .output width=50%}


$$
x_{1}^{2} + y^{n+4} + z_{0} + 10
$$

:::
::::::

:::

### Fractions

Writing expressions that include fractions takes a little bit more than simple
expressions, but it's not much. Writing a fraction requires the use of a
*command* in $\LaTeX$: `\frac`. Commands in $\LaTeX$ generally also accept
arguments, the things that you want the command to display. The `\frac` command
takes two arguments: a numerator and a denominator. You can pass arguments to a
command in separate sets of curly braces per argument, just after the command:

::: example

:::::: columns
::: {.column .input width=50%}

```latex
$$
\frac{1}{2}
$$
```

:::
::: {.column .output width=50%}

$$
\frac{1}{2}
$$

:::
::::::

:::

That's a pretty simple fraction, but the arguments that you pass to `\frac` can
be any expression in $\LaTeX$, *including* other fractions!

::: example

:::::: columns
::: {.column .input width=50%}

```latex
$$
\frac{ x_1^{2} + y^{n+4} + 10 }
     { \frac{1}{2} }
$$
```

:::
::: {.column .output width=50%}

$$
\frac{ x_1^{2} + y^{n+4} + 10 }
     { \frac{1}{2} }
$$

:::
::::::

:::

### Sequences

Sometimes you need to show an expression that includes sums of sequences
($\sum$) or products of sequences ($\prod$). Writing these expressions is
similar to fractions in that you'll use some commands (`\sum` and `\prod`), but
you'll also use superscripts (^) and subscripts (\_) to place symbols above and
below the sum or product symbols:

::: example

Use the `\sum` command to display a summation:

:::::: columns
::: {.column .input width=50%}

```latex
\sum_{n=0}^{\infty} x_n = \infty
```

:::
::: {.column .output width=50%}

$$
\sum_{n=0}^{\infty} x_n = \infty
$$

:::
::::::

Similarly, use the `\prod` command to display a product:

:::::: columns
::: {.column .input width=50%}
```latex
\prod_{n=0}^{\infty} x_n = \infty
```
:::
::: {.column .output width=50%}

$$
\prod_{n=0}^{\infty} x_n = \infty
$$
:::
::::::

:::

### Common CS symbols

Some other symbols that you'll need to use when writing for CS are to describe
things like complexity of algorithms, so "big O", "big omega", "theta",
logarithms and natural logarithms, etc.

::: example

* Big O: `\mathcal{O}` &rarr; $\mathcal{O}$
* Big omega: `\Omega` &rarr; $\Omega$
* Big theta: `\Theta` &rarr; $\Theta$
* Logarithm: `\log` &rarr; $\log$
* Natural logarithm: `\ln` &rarr; $\ln$

A more complete example would look like:

:::::: columns
::: {.column .input width=50%}

```latex
\mathcal{O}(\log(n))
```

:::
::: {.column .output width=50%}

$$
\mathcal{O}(\log(n))
$$

:::
::::::

:::

You may also want to put subscripts on things like `\log` to indicate which
number system you're using, so for something like base 2:

::: example

:::::: columns
::: {.column .input width=50%}

```latex
\Theta(\log_{2}(n))
```

:::
::: {.column .output width=50%}

$$
\Theta(\log_{2}(n))
$$

:::
::::::

:::

Further reading
---------------

This document gets you started with Markdown and $\LaTeX$, but you're definitely
going to run into situations where you want to do things that are a little bit
more complex than what you've seen here (i.e., tables).

You can find plenty of information online about both Markdown and $\LaTeX$, but
here are some resources that are particularly good or helpful:

* GitHub's "[Basic formatting syntax]" describes most of this document and a
  little bit more.
* GitHub's "[Working with advanced formatting]" shows things that are in this
  document (math and code blocks) and shows things like tables, and features
  that are specific to GitHub's Markdown like "collapsed sections".
* Pandoc's "[Pandoc's Markdown]" has similar content to the above, but focusing
  specifically on Pandoc.
* [Overleaf's documentation] is a comprehensive overview of $\LaTeX$, well
  beyond anything you would need for this course.

  ::: aside

   We're embedding $\LaTeX$ within Markdown-formatted documents, but $\LaTeX$
   is, in and of itself, a complete plain text document format. I (me, Franklin)
   personally find writing in $\LaTeX$ to be painful. Being able to embed bits
   of $\LaTeX$ in Markdown gives me the best of both worlds.

  :::

[Basic formatting syntax]:
https://guides.github.com/features/mastering-markdown/
[Working with advanced formatting]:
https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting
[Overleaf's documentation]: https://www.overleaf.com/learn
[Pandoc's Markdown]: https://pandoc.org/MANUAL.html#pandocs-markdown
