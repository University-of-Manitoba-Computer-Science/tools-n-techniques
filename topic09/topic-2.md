---
title: Shell scripts
author: Franklin Bristow
---

Shell scripts
=============

::: outcomes

* [X] Write and run shell scripts to repeat complex tasks.

:::

::: {style='float: left;width: 300px'}

![A script.](script.png)

:::

At this point you're pretty familiar with using the command line; you should be
able to do a variety of things:

* Navigate and create folder structures.
* Edit text files.
* Convert files between various formats.
* Filter lines from text files.
* Read and change permissions on files.
* Use version control software.
* Find files by name or properties.
* Redirect standard input, output, and error.
* Construct pipelines of commands.

While there's a whole world of things you can still learn about using the
command line, and more command line tools than you can imagine to learn about
(which sometimes themselves contain entire programming languages!), you've
learned and demonstrated a lot! :tada:

As you're getting more used to using the command line, you may find yourself
repeating similar, complex commands over and over again. Or maybe you find
yourself doing the same kinds of things over and over again, maybe running
multiple commands repeatedly. Or maybe you've built a complex pipeline that
you want to keep for use later because you'll need to use it again.

In their very simplest form, shell scripts are plain text files that contain a
sequence of commands or statements, separated by newlines or semi-colons. As you
grow shell scripts, they can contain things like conditional statements, loops,
functions, and... uh, hey, [wait a minute]. That, uh, that sounds an awful lot
like programming.

Most of the time we spend interacting with shells is interactive: the shell is
waiting for us to enter a command, and when we press <kbd>Enter</kbd>, the shell
runs the command, waits for it to finish (it actually `wait(2)`s, it's a C
function), then patiently waits for us to enter another command.

Most shells can also run non-interactively: you give the shell the name of a
file that contains a sequence of commands and the shell will just interpret,
then run the sequence of commands like it's a program.

[wait a minute]: https://youtu.be/g3YiPC91QUk?t=58

Shells and languages
--------------------

Similar to different programming languages, different shells use different
syntax to express similar ideas. Deciding which shell program to use defines
what syntax you're going to use and the kinds of keywords you should be using
when you're looking for help (in the manual page for the shell, on the shell's
website, or generally online).

While your default shell on Aviary is `tcsh`, we're going to be using `bash` as
a shell interpreter for scripting. This is an opinionated choice, just as
using `vim` instead of `emacs` is an opinionated choice. As you get more
comfortable using the command line, you may want to choose a different shell
(like `fish`) and thus a different shell language, but `bash` and its syntax are
common enough that we'll treat it like a "[lingua franca]".

[lingua franca]: https://en.wikipedia.org/wiki/Lingua_franca

Basic scripting
---------------

Let's start with the basics: the general structure of a shell script and some
very simple shell scripts.

### General structure

Shell scripts all start with a "[shebang]" line --- a line that starts with the
symbols `#!`. The first line indicates which program is going to be run to
interpret the rest of the file.

```bash
#!/usr/bin/env bash # this is a bash script
```

Everything after the first line is the actual contents of the script, the
sequence of commands to be executed.

[shebang]: https://en.wikipedia.org/wiki/Shebang_(Unix)

### Simple scripts

Here's an example of a very simple script:

```bash
#!/usr/bin/env bash

ls -la
```

Copy and paste this into a new plain text file on Aviary; give it a file name
that represents what this does (I recommend `la`, "list all").

::: aside

Copying and pasting into `vim` is tedious, having to enter and exit paste mode
is a real bother. Another way to quickly copy and paste into your terminal to
create a new file is using the program `cat`. As above, `cat` is a program that
will read standard input and write to standard output. But we can redirect
standard output to a file!

```bash
cat > la
```

Once you enter that, press <kbd>Enter</kbd>, then paste, then press
<kbd>Control</kbd>+<kbd>D</kbd>.

That's it!

:::

Once you've written the file, exit your editor. Before we can run a shell
script, we need to mark it as executable using `chmod`:

```bash
chmod a+x la
```

Then we can run the script:

```bash
./la
```

:tada:, your first shell script!

Shell scripts consist of one or more lines of commands to run. Add another line
to your script:

```bash
find . -name "*.md"
```

Then run it again (you don't need to `chmod` again). Now *two* commands worth of
output appear.

One command that you might find helpful when you're scripting is the `echo`
command, this is a "print" command for shells:

```bash
echo "Hello, world!"
```

You can also write comments using the `#` symbol, anything following is a
comment:

```bash
echo "Hello, world" # a friendly message
find . -name "*.docx" -delete # clean up Word files
```

::: example

Here's a more complete (and completely contrived) example of a script:

```bash
#!/usr/bin/env bash

echo "Here's what's in the current directory:"
# list all with long listings
ls -al

echo "Here are all the Markdown files:"
# find all files with the `.md` extension
find . -name "*.md"
```

:::

Environment variables and the `$PATH`
------------------------------------

Shell languages, like other programming languages, support variables.

Almost all shells follow the same convention for naming variables:

* Variable names start with a `$`,
* Variable names are all `UPPERCASE`,
* Variable names are [`SNAKE_CASE`] (they use underscores to separate words).

[`SNAKE_CASE`]: https://en.wikipedia.org/wiki/Snake_case

All shells have special variables, and those special variables help your shell
make decisions, or help define the behaviour that your shell has. These special
variables are called "environment variables".

::: example

Try running this in your shell to find out what shell you're using:

```bash
echo $SHELL
```

`$SHELL` is an environment variable that contains the name of the running shell.

:::

When you enter the names of programs on the command line, your shell has to
figure out where that program actually is in a folder structure.

::: aside

This is might seem obvious when you think about it, but think about it: the
programs that you're running on the command line are just files with bits in
them. They were written in a programming language (often C), then compiled and
put in a folder somewhere.

A lot of programs on Linux and UNIX systems live in the folders `/bin` and
`/usr/bin`. You can learn a bit more about where files live on a Linux system by
reading a manual page:


```bash
man hier 

### OR

man 7 hier # hier is in section 7 for miscellaneous
```

:::

Your shell uses a special environment variable called `$PATH` (often called
*the* `$PATH`) to find where the command you just entered exists as a file. The
`$PATH` contains a list of directories that your shell will look in to find the
file representing the command you asked it to run. Different shells use
different separators for directory entries in the path. Both `tcsh` and `bash`
use a colon `:` to separate directories.

::: example

As above, use the `echo` command to print out what the `$PATH` is right now in
your shell:

```bash
echo $PATH
```

:::

Your `$PATH` will contain many folders on Aviary, but it importantly includes
two directories:

1. `.`: the current directory, and this is why you don't have to type `./` in
   front of programs you've written and compiled yourself.
2. `~/bin`: a directory named `bin` relative to your home directory. When you
   `echo $PATH`, the `~` will be listed as an absolute path (e.g.,
   `/home/student/you/bin`).

What this means is that we can put scripts we write into the directory `~/bin`,
then we can run them *anywhere*.

::: example

The directory `~/bin` *may not* exist in your user directory on Aviary. Create
the directory, then move the `la` script you wrote above into this directory.

This applies **only** to `tcsh`: `tcsh` [caches] the names of commands that are
in folders on the `$PATH`. After you add something to `~/bin` (which is on your
`$PATH`), you've got to get `tcsh` to regenerate this cache. You can regenerate
the cache in `tcsh` by running the command:

```bash
rehash
```

You must do this any time you add programs or commands to folders on the `$PATH`
that you want to work in other places, but this only applies to `tcsh`. If
you're using a different shell like `bash` or `fish`, then your shell will
almost certainly do this for you.

Now change back to your user directory:

```bash
cd ~

### Or just `cd` with no arguments

cd
```

And run `la`. :tada:, now you can run `la` in *any* directory.

:::

You can find out which environment variables are currently set and what their
values are using the `env` command.

[caches]: https://en.wikipedia.org/wiki/Cache_(computing)