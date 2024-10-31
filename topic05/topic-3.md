---
title: "Filter lines from large text files"
author: Franklin Bristow
---

::: outcomes

* [X] Filter lines from large text files using patterns.

:::

We're going to switch away from `find`, but we're going to stick with the
general theme of using patterns. Another relatively common task is to find lines
*within* a plain text file that match a certain pattern.

Depending on which courses you're taking or have taken, this might be a task
where you would consider using a loop, but we're going to take advantage of a
tool that's available on the command line: `grep`.

::: aside

What on earth does `grep` mean?!

Computer Scientists and programmers are bad at naming things (maybe because it's
a "[hard thing]"). Maybe it is hard, but we're still bad at naming things, and
[we should feel bad].

I'm digressing. The name `grep` [comes from a command in the `ed` editor] that
would "**g**lobally search for a **r**egular **e**pression and **p**rint
matching lines".

An unfortunate theme among useful programs in Unix and Unix-like operating
systems (like macOS and Linux) is that their names aren't *discoverable* (it's
really hard to figure out a command to do something you want when it's called
something like `grep`).

[hard thing]: https://www.martinfowler.com/bliki/TwoHardThings.html
[we should feel bad]: https://youtu.be/4mcD5jd-RAU?t=34
[comes from a command in the `ed` editor]: https://en.wikipedia.org/wiki/Grep#History

:::

Just finding the lines that match a pattern in a file can be useful, but we're
going to look at a few options for `grep` that can help give some additional
information or context about what we're looking for:

* Basic use: printing out matching lines.
* An option to count the number of matching lines.
* An option to show lines around the line we're looking for.
* An option to search files recursively.
* An option to print the line number that matches the pattern.

Getting some data
=================

Let's start with a large text file.

::: aside

The example we're going to be using here is genetic sequence data. Similar to
how Computer Scientists and programmers are bad at naming things, biologists and
microbiologists are bad at storing things and they use plain text formats to
store genetic sequence data. That's actually really convenient for us because it
gives a realistic data set to work with.

Don't worry: you don't need to be a biologist or microbiologist to follow along.

:::

Download this file from [NCBI] to your user directory on Aviary (use `wget` or
`curl`):

<https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/030/370/485/GCA_030370485.1_ASM3037048v1/GCA_030370485.1_ASM3037048v1_genomic.fna.gz>

This file type is a `gz` or "g-zipped" file (where the g means [gnu]).
Once you've downloaded the file, you will have to decompress it!

:::::: columns
::: {.column .input width=50%}

```bash
gunzip GCA_030370485.1_ASM3037048v1_genomic.fna.gz
```

:::
::: {.column .output width=50%}

`gunzip` does not print any output, but you should now see
`GCA_030370485.1_ASM3037048v1_genomic.fna`, noting that the `.gz` is not at the
end of the file name any more.

:::
::::::

Now that the file is decompressed, feel free to take a look at it using your
preferred text editor on Aviary (e.g., `vim`, `nano`, `emacs`). This is a
[FASTA-formatted file]. A FASTA-formatted file contains 1 or more "records",
where a record will have a unique identifier that's meaningful to a biologist or
microbiologist, and then the sequence data that corresponds to that identifier.
Records look like this:

```
>OR160415.1 Monkeypox virus isolate hMpxV/USA/IL-RIPHL-MPXV-050-0057/2023, complete genome
TTACAGATCATTTATATTCCAAAAATATTAACTATATACGTTTATTATATGATGTTAACGTGTAAATTATAAACATTATT
```

The file you just downloaded is about 200KB in size (there are about 200 thousand
characters in this file), so doing things like counting records is not something
we want to do by hand.

[NCBI]: https://www.ncbi.nlm.nih.gov/
[FASTA-formatted file]: https://en.wikipedia.org/wiki/FASTA_format
[gnu]: https://www.gnu.org/philosophy/free-sw.html

Basic use
=========

::: aside

You could do these exercises with any text file. Consider trying them
with some of the markdown files you've created in the past, too!

:::

Let's start using `grep` to filter and print out lines that match a certain
pattern.

::: example

From our crash course on FASTA-formatted files, we know that records have unique
identifiers, and the lines with unique identifiers contain or start with the `>`
character. Let's use that as our filter:

::: input

```bash
grep '>' GCA_030370485.1_ASM3037048v1_genomic.fna # print all lines in the file that
                                                  # contain the > character
```

:::

This will print out a bunch of lines (we'll find out how many real soon!), and
all the lines contain the pattern `>`.

We can actually be more precise with what we want by using an "anchor" for our
pattern. Records start with lines where the **first character** on the line is
`>`. In most FASTA-formatted files, the only place where the `>` character
appears is on the unique identifier line, but it's possible for it to appear in
other places, too.

::: input

```bash
grep '^>' GCA_030370485.1_ASM3037048v1_genomic.fna # print all lines in the file that
                                                   # **start with** the > character
```

:::

The `^` (caret, I prefer "hat") is an "anchor": "From the start of the line".

:::

Counting lines
==============

Seeing the lines that match the pattern is useful, but we may also want to know
other stuff, like how many lines matched the pattern. Thankfully, `grep` has an
option to help us with that: `-c`.

::: example 

::: input

```bash
grep -c '^>' GCA_030370485.1_ASM3037048v1_genomic.fna # count the lines in the file that
                                                      # start with the > character
```

:::

This prints out *only a number*, and the number represents how many lines
matched the pattern.

For `GCA_030370485.1_ASM3037048v1_genomic.fna`, this tells us how many records
are in this file.

:::

Showing lines around the matching lines
=======================================

We can ask `grep` to find lines that match patterns, and we can also ask `grep`
to show us the lines that are around (before and after) the line that matches
the pattern. `grep` calls this "context".

::: example

We can print the lines that match the pattern, plus the lines immediately after
those using the `-A` option (after):

::: input

```bash
grep -A 2 '^>' GCA_030370485.1_ASM3037048v1_genomic.fna # print out the record identifier and
                                                        # 2 lines of sequence data after it.
```

:::

Similarly, we can print the lines that match the pattern, plus the lines
immediately *before* those using the `-B` option (before):

::: input

```bash
grep -B 2 '^>' GCA_030370485.1_ASM3037048v1_genomic.fna # print out the record identifier and
                                                        # 2 lines of sequence data before it.
```
:::

We can do both at the same time with the `-C` option (this is upper-case C, for
"context"):

::: input
```bash
grep -C 2 '^>' GCA_030370485.1_ASM3037048v1_genomic.fna # print out the record identifier and both
                                                        # 2 lines before and after it.
```
:::

:::

Filtering recursively
=====================

Sometimes you want to search many files in the same directory for a pattern,
either because you don't know which file contains the lines you're looking for,
or because your data is spread across many files.

We've seen a "recursive" command before: 

::: input

```bash
rm -r hello # recursively remove hello and everything within it
```
:::

The `grep` command also has a recursive option, and it's also `-r`!

::: example

Switch back to `crazy-directories`. We were able to use `find` to help us find
files that have names matching a pattern. Now we want to use `grep` to find
files that contain a specific pattern.

Emoji short codes all follow the same pattern: A colon, followed by some
characters, followed by another colon. Here are some emoji and their [short
codes]:

* `:banana:` :banana:
* `:robot:` :robot:
* `:sparkles:` :sparkles:

[short codes]: https://www.unicode.org/emoji/charts/full-emoji-list.html

We can use `grep` recursively to find all files that contain one or more lines
matching the pattern `:*:` (a colon, followed by any number of characters,
followed by another colon).

::: input

```bash
grep -r ":*:" # note no filename!
```

:::

Depending on the state you're in, this is probably going to print out a few more
files than you expected, including `.docx` files.

::: aside

Let's talk about what `.docx` files are: they're secretly a `.zip` file.
Remember how to `unzip` `.zip` files? That's right! `unzip`!

Go ahead, change into a directory containing one of the `.docx` files you
created in `crazy-directories` and `unzip` it:

::: input

```bash
unzip robot.md.docx
```

:::

There are going to be a bunch of new files in the directory that are mostly
`.xml` files. XML is a "markup" language, sort of like Markdown.

Try running `grep` again recursively on this again and you'll see that we're not
just matching emoji short codes anymore, but a bunch of weird looking XML. Neat
:camera:.

:::

:::

Printing matching line numbers
==============================

Knowing the name of the file containing the line that matches your pattern is
often enough, but `grep` can help you out a little more by telling you exactly
the line number that matched the pattern. You can ask `grep` to tell you this
using the `-n` option.

::: example

If you left the root of `crazy-directories`, change back to it.

Let's find all files that contain the pattern `:*:` again, but we'll ask for
`grep` to print out the line numbers:

::: input

```bash
grep -rn ":*:"

# OR

grep -r -n ":*:"
```

:::

*Some* command line tools will allow you to combine options after a single `-`
(so `-r -n` turns into `-rn`).

:::
