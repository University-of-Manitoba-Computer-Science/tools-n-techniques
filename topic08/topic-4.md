---
title: Piping
author: Franklin Bristow
---

Piping
======

::: outcomes

* [X] Send data between programs using a pipe.

:::

!["The Treachery of Images" by Rene Magritte; &copy; [C. Herscovici/Artists
Rights Society (ARS), New York](https://collections.lacma.org/node/239578)](pipes.jpg)

Sometimes we're redirecting output from one program to a file, then redirecting
the input of another program using that same file.

::: example

```bash
./program1 > outputfrom1.txt # stdout goes to the file
./program2 < outputfrom1.txt # stdin comes from the file
```

:::

This is... fine, but there are two reasons why we want something better:

1. We do this frequently, so having to type fewer characters is helpful.
2. We don't want to waste space by creating all of these temporary files.

We do this *so* frequently (sending the output from one program to be the input
to another program) that there's an operator for that: the "pipe".

::: example

We can send the output of one program to be the input of another program using
pipes (`|`):

```bash
./program1 | ./program2 # stdout from 1 is sent directly to stdin of 2
```

:::

When you can use pipes, pipes are almost always better:

* You don't create extra files that you need to worry about deleting later.
* You only enter one line in your terminal instead of many lines.
* Pipes *can* be faster :rabbit:, the programs on either side of the pipe run at
  the same time, unlike with simple redirection where you run one program, then
  the other.

A frequent use of pipes is to send the output of one command to a *pager*
(not like [:pager:], but more like :book:) like `less`.

[:pager:]: https://en.wikipedia.org/wiki/Pager

::: aside

Pagers (or "[Terminal pagers]") are programs that will show you one "page" of
text from a text file at a time. They allow you to scroll through a text file,
either line by line or by page.

An early pager is called [`more`]. `more` was originally released in 1978, and
has limited paging functionality, you could only move forward one page at a time
(modern versions of `more` let you go backwards and moving one line at a time,
see the manual page for `more` to find out what else it can do).

A newer pager (barely) is called [`less`]. `less` was originally released in
1984 and has extensive improvements over `more`. `less` implements everything
you can do in `more`, but adds *more* functionality like going backwards.

As always, explained jokes are the funniest, and the joke here is that `less`
*is* `more`.

[Terminal pagers]: https://en.wikipedia.org/wiki/Terminal_pager
[`more`]: https://en.wikipedia.org/wiki/More_(command)
[`less`]: https://en.wikipedia.org/wiki/Less_(Unix)

:::

You've used `less` before already: `less` is the default pager when you're
reading manual pages.

`less` and all pagers can be used to read the contents of a file:

```bash
less my.md # page through my.md
```

As a pager, `less` is read only, but if you do need to make changes to the file,
you can ask `less` to start your editor by pressing <kbd>v</kbd> on your
keyboard.

Another common use of `less` and other pages is to page through output from
another program.

::: example

You can send the output of one program to the input of `less` and other pagers
using pipes:

```bash
sort -R /usr/share/dict/words | less
```

This will sort (using the appropriately named `sort` command) randomly (`-R`)
the list of words in `/usr/share/dict/words`. `sort` will write it's output to
standard output. `less` is on the other side of the pipe and will read from
standard input. The pipe here will send the standard output from `sort` to be
the standard input for `less`.

Just like with manual pages, you can quit less by pressing <kbd>q</kbd> on your
keyboard.

:::

A single command in your shell is not limited to just one pipe. With
redirections, you could only redirect one program's standard output or standard
input. We can actually chain more than two programs together using pipes to
build complex "pipelines" of data.

::: example

Here's a still contrived, but slightly more complex pipeline consisting of four
separate commands:

```bash
sort -R /usr/share/dict/words | head -5 | less
```

Here's what this does:

* `sort` reads the file `/usr/share/dict/words`, sorts the lines randomly (`-R`)
  and writes to standard output. Standard output is the pipe and the data is
  sent to `head`.
* `head` reads standard input (which is the piped data from `sort`) and prints
  out the first 5 lines (`-5`) to standard output. `head`'s standard output is
  the second pipe and the data is sent to `less`.
* `less` reads standard input (which is the piped data from `head`) and prints
  out (yes, prints out) to standard output (yes, to standard output) the
  interface you see when interacting with `less`.

:::

Some commands you may frequently see in pipelines include:

* `head`: Reads standard input (or a file) and prints the first $n$ lines it
  reads to standard output.
* `tail`: Reads standard input (or a file) and prints the last $n$ lines it
  reads at the end of the "file" to standard output.
* `cat`: Reads standard input (or a file) and prints out the file in its
  entirety.
* `yes`: Just constantly prints `y` (or a different string you give to it) to
  standard output.
* `sort`: Reads standard input (or a file) and prints the output in the sorted
  order you specify to standard output.
* `grep`: Reads standard input (or a file, like you've seen) and prints out
  lines from the file that match a pattern to standard output
* `uniq`: Reads standard input (or a file), and prints out only non-repeated
  adjacent lines to standard output.
* `less`: A pager!
* `wc`: "Word count"; Reads standard input (or a file), and prints out the
  number of lines, words, or bytes (characters) read to standard output.
* `tee`: Reads standard input (and **not** a file), and prints output to both
  standard output and the file you specify by name.

Any program you write that reads standard input and writes to standard output
can be used in a pipeline, too!
