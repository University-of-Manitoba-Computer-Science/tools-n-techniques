---
title: "Structures: conditional statements and loops"
author: Franklin Bristow
---

::: outcomes

* [X] Use loops, conditional statements, and variables in a shell script.
    * [X] Use "globs" in a shell script to apply operations to files.

:::


Shell scripting languages are fully featured programming languages and include
structures like conditional statements and loops. They contain other structures,
too, but let's stick to the basics.

Conditional statements
======================

Conditional statements in `bash` use the familiar `if` keyword and *resemble*
the expressions you've seen in other languages.

One of the major differences in `bash` are expressions themselves: most of the
questions you're going to be asking about a variable use unary operators.

Here's what a `bash` conditional statement looks like:

```bash
if [[ -a hello.c ]]; then
    echo "hello.c exists"
else
    echo "hello.c does not exist"
fi
```

The `-a` is a unary operator on file names. `-a` returns true if the file
exists, and returns false if the file does not exist.

Spacing is important here! `bash` is not a very smart language. You might be
tempted to leave out spaces between `[[` and `-a` or between `hello.c` and `]]`,
but you **must** have spaces between these symbols.

::: aside

WHY?!

`bash` is, uh, weird. `[[` is technically a command that takes arguments. The
arguments the `[[` command is getting in the above example are `-a`, `hello.c`,
and `]]`. The `;` is a line separator (like in Python it's optional, but can be
used).

Yeah, weird.

:::

`bash` has many unary operators that you can use to test files or variables. The
one we care about right now is the `-n` operator, asking if a string is non-zero
in length.

::: example

Let's add a conditional statement to `la` to test for the presence of arguments:

```bash
#!/usr/bin/env bash

if [[ -n "$1" ]] ; then
    ls -al "$1"
else
    ls -al
fi
```

:::

You can find more unary operators in `bash` by reading the `CONDITIONAL
EXPRESSIONS` section of its manual page, but here are some examples:

+----------------------+----------------------------------------------------+
| Operator             | Meaning                                            |
+======================+====================================================+
| `-a file`            | True if file exists.                               |
+----------------------+----------------------------------------------------+
| `-d file`            | True if file exists and is a directory.            |
+----------------------+----------------------------------------------------+
| `-r file`            | True if file exists and is readable.               |
+----------------------+----------------------------------------------------+
| `-s file`            | True if file exists and has a size greater than 0. |
+----------------------+----------------------------------------------------+
| `string1 == string2` | True if the strings are equal.                     |
+----------------------+----------------------------------------------------+

Loops
=====

We can't talk about conditional statements without at least saying something
about loops!

Similar to conditional statements, loops use the familiar `for` keyword. Bash
also supports `while` and `until` loops, but most of the time you're using a
loop in Bash, you're operating on some sequence of file names rather than until
some event happens.

The structure of a `for` loop is frustratingly different from conditional
statements in a way it's not in other programming languages --- the conditional
statements you saw above use the `[[` and `]]` brackets for wrapping the
expression, but `for` loops generally do not use brackets or parenthesis in
Bash.

Here's what a `for` loop looks like in Bash:

```bash
for f in * ; do
    echo $f
done
```

* The `for` is ... `for`, it's the start of the loop.
* The `f` is the name of the variable you want to use as the name for the value
  in the current iteration of the loop over the sequence.
* The `in` is a separator between the variable name and the sequence.
* In this case `*` *is* the sequence. This is a "glob" or a pattern, and this
  glob in the shell means "all files in the current directory" (more on this 
  soon!).
* The semi-colon `;`, like in conditional statements above, ends the current
  statement.
* `do`, then is the beginning of the body of the loop.
    * `echo $f` is one command you want run on the variable. This will print out
      the variable's name.
* `done` ends the body of the loop.

::: aside

Maybe this looks sort of familiar. Maybe this looks like what we were doing with
`find` and `-exec`. They do accomplish similar results!

Both work, and both are effective. One way to think about this matching of ideas
is that `find` and `-exec` are more of a functional programming paradigm (this
is a `map` operation), `for` loops are more of a procedural paradigm.

Some people may find that a loop is more readable than `find` and `-exec`, 
though, especially if you're going to do *several* operations on a file or item
in a loop.

:::

When you're writing `for` loops, the sequence can either use the patterns you've
seen before (like `*.md`), or can be the result of a *command*. 

In fact, we can rewrite the `for` loop from above using `find`!

```bash
for f in $(find . -maxdepth 1) ; do
    echo $f
done
```

The output looks a little bit different, but the result is the same.

Another common kind of loop you may want to write is one that iterates over a
sequence of numbers (like the traditional `for` loop you've seen in languages
like Java). To do that you can use the `seq` command:

```bash
for num in $(seq 1 10) ; do
    echo $num
done
```

