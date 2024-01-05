---
title: Redirecting input and output
author: Franklin Bristow
---

Redirecting input and output
============================

::: outcomes

* [X] Redirect the output from a program to a file.
* [X] Redirect a file to be the input for a program.

:::

We can "redirect" input and output streams:

* Instead of standard input being our keyboard, we can have the input our
  program reads be the contents of a file.
* Instead of standard output and error being our terminal, we can have our
  program's output be written to a file.

We can do this using a little bit of help from our shell :shell:.

Redirecting standard output
---------------------------

Redirecting standard output can be useful when you need to save what a program
prints for output and the program doesn't support options for writing directly
to a file. It's also useful when you've got a program that produces *lots* of
output and you want to be able to search through it later with programs like
`grep`, or review the output with a pager like `less`.

Almost all shells use the same operator for redirecting standard output from a
process to a file: `>`

::: example

You can redirect standard output from a program using the `>` operator:

```bash
# find supports writing to files with `-fprint`, but this is way easier
find . -name "*.md" > all-mds.txt
# pandoc supports writing to files with `-o`, but we can still redirect output
pandoc -f markdown -t man my.md > my.man
```

:::

When you redirect to a file with `>`, if the file previously existed, its
contents will be overwritten with the contents of standard output. Sometimes
this is what you want, but sometimes it's not. Sometimes you want to append to
the existing contents of the file, and you can do that with *two* greater-than
signs: `>>`

::: example

You can redirect standard output from a program and append the output to an
existing file using the `>>` operator:

```bash
# append new output to what's already in all-mds.txt
find . -name "*.md" >> all-mds.txt
```

:::

Redirecting standard error
--------------------------

Redirecting standard error is... uncommon to want to do. The usefulness of
redirecting standard error is similar to redirecting standard output: when you
want to save what was written as errors or if the program produces lots of error
output that you want to filter or review later.

Different shells use different operators to redirect standard error:

* In [Bash], [Dash], [Zsh], [fish], and more, redirecting standard error uses
  the operator `2>`.

  ::: example

  We use the `2>` operator to redirect standard error in some shells:

  ```bash
  ./error-program 2> errors.txt
  ```

  :::
* In [Tcsh] and [csh]... well, you can't *directly* redirect standard error.
  You can, however redirect standard output by itself in a "subshell", then
  redirect what's left (which is only standard error)[^tcsh-stderr]:

  ::: example

  We use "subshells" and the `>&` operator to redirect standard error to a file:

  ```bash
  (./error-program > /dev/tty) >& error.txt
  ```

  ::: aside

  What on earth is going on here?

  The parenthesis `()` creates a "subshell", but we can *sort of* conceptually
  like parenthesis in expressions in a programming language: when we run
  `./error-program` and put the `>` operator in the parenthesis, it's saying
  that the standard input from this program will be redirected to a special file
  named `/dev/tty`. That special file is a file that represents your terminal. 

  (a **file**?! WHAT IS GOING ON?!)

  This is a longhand way of saying "I'd like you to print standard output to my
  terminal, please".

  The `>&` operator in Tcsh and csh represents standard output and standard
  error combined, but since standard output was already redirected to `/dev/tty`
  in the parenthesis, all that's left to redirect to the file is what's getting
  printed on standard error.

  :::

  :::

OK. Now we can do it, but *why*?

"Saving errors for later" and "filtering errors later" are OK motivations for
wanting to do this, but the real reason why we usually want to do this is that
we want to *ignore* errors because we don't care about them. Linux has a special
file named `/dev/null`, and any writes to `/dev/null` are just discarded.

::: example

A common use for redirecting standard error is to redirect that output to a
special file called `/dev/null`:

```bash
./error-program 2> /dev/null

# OR in tcsh or csh

(./error-program > /dev/tty) >& /dev/null
```

:::

[Bash]: https://www.gnu.org/software/bash/
[Dash]: http://gondor.apana.org.au/~herbert/dash/
[Zsh]: https://www.zsh.org/
[fish]: https://fishshell.com
[Tcsh]: https://www.tcsh.org/
[csh]: https://github.com/freebsd/freebsd-src/tree/main/bin/csh
[^tcsh-stderr]:
<https://unix.stackexchange.com/questions/197878/inconsistency-of-stderr-redirection-between-tcsh-and-other-shells>

Redirecting standard input
--------------------------

Both standard output and standard error are places where output is written. We
can also replace where standard input gets its input from. This can be useful
when we want to provide a lot of input to a program, but the program doesn't or
can't read files directly. Or if we're repeatedly re-running a program that's
asking for just a little bit of input, but typing that input in by hand is a
*pain* after the millionth time running the program (we've all done this at some
point, there's no shame in denying it).

Almost all shells use the same operator for redirecting a file to standard
input: `<`

::: example

We can redirect standard input to a process using the `<` operator:

```bash
pandoc -f markdown -o my.pdf < my.md

# redirect both stdin and stdout:
pandoc -f markdown -t html < my.md > my.html
```

:::
