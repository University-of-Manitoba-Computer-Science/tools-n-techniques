---
title: "Finding files"
author: Franklin Bristow
---

::: outcomes

* [X] Find files on the command line by name using patterns.

:::

You might be saying to yourself "[wat]". "Why would I ever need to find files on
the command line?"

I'd say to you: "You're right :+1:! we just spent time figuring out an
appropriate folder structure for your courses! It should be pretty easy to find
a file in that nice folder structure!"

But then I'd also say: "You're not always going to be working with folder
structures that you made. You're not always going to be working with files
that you've created. Sometimes you'll know what the name of a file is (or
something like what the file name should look like), but not where it is within
a deeply nested or complex folder structure."

So here I am saying it: You're not always going to be working with folder
structures that you made. You're not always going to be working with files
that you've created. Sometimes you'll know what the name of a file is (or
something like what the file name should look like), but not where it is within
a deeply nested or complex folder structure.

We're going to be using a program that has an amazingly appropriate name:
`find`.

::: aside

If you're using macOS, *some* of these examples will work on your local
computer. If you're using Windows, **none** of these examples will work on your
local computer. If you're using a Linux distribution, ***all*** of these
examples will work on your local computer.

Somewhat annoyingly, some of the examples that we'll look at will work
*differently* between macOS and Linux. We will try to use examples that work on
both the same way, but...

Please connect to Aviary before you try to run any of these examples.

:::

::: example

The simplest way to run `find` is to run it with a single argument: the
directory that you want to find files in:


::: input

```bash
find .

# this is the word `find` with a space, then a period after it.
```

:::

`find` will proceed to list all of the files that it can find starting in the
current directory, and that's probably a lot more than you expected.

:::

[wat]:
https://i.kym-cdn.com/photos/images/original/000/000/151/n725075089_288918_2774.jpg

Finding files by name
=====================

Normally this isn't how you would use `find`. This is certainly *a* way you can
run `find`, but it's not the typical usage.

One fairly common way to use `find` is to search for files by their name. We're
going to look at this in several ways:

* Finding files by an exact file name that we know in advance.
* Finding files by a file name that we know matches a pattern.
* Finding files by a file name that we know matches a pattern, but we don't know
  the *case* of the file's name (UPPER CASE or lower case).

You're going to be working with a directory structure that you don't know
anything about and is too deep and complex for you to manually search through.
(I really hope the directories you see in your job or your academic life don't
look anything like this!)

Start by [downloading this file] (on the command line; either use `wget` or
download to your local computer then transfer with `scp`), but make sure that
you **do not** download it into your repository:

<https://toolsntechniques.ca/topic05/crazy-directories.tar>

[downloading this file]: ../topic03/topic-2.html#downloading-files-from-the-internet

::: warning

**Note**: There are over 7000 directories in this folder structure.  It's not
worth your time trying to find anything trying to use `cd` and `ls`.

:::

This is a `.tar` file (a "[Tape ARchive]"). Similar to a `.zip` file, this is
a kind of "compressed" file --- there are many files *within* this single file,
and you need to use a program to "expand" the archive. For `.tar` files, the
program's name is `tar`:

::: input

```bash
tar -xf crazy-directories.tar 
# The options xf are for e**X**tract from **F**ile
```

:::

::: warning

<mark>**Note**</mark>: **There are over 7000 directories in this folder
structure**. Extracting the entire directory structure on Aviary will probably
take 5 or more minutes to complete.

:::

[Tape ARchive]: https://en.wikipedia.org/wiki/Tar_(computing)

::: aside

A **single command** was used to create this directory structure:

```bash
mkdir -p {a..z}/{0..9}/{a..z}
```

This uses a feature that's present in *some* shells called brace expansion.

This **will not** work on Aviary when you first connect. Aviary, by default,
uses a shell program called [tcsh]. tcsh does not support brace expansion.
[Bash] supports brace expansion, and that's the shell that was used to create
this directory structure. You can run `bash` on the command line to start the
Bash shell.

::: aside

An aside *within an aside*? Is that even legal?

`bash` and `tcsh` are not the only shell programs. There are [many shell
programs].  We're unfortunately not going to spend time talking about shells.
Most people don't even think about shells and just use the one that starts
automatically when the terminal opens or when they connect to a remote computer.

When you take the time to try out different shells, though, it's a similar
choice to choosing a text editor.

[many shell programs]:
https://en.wikipedia.org/wiki/List_of_command-line_interpreters

:::

[tcsh]: https://en.wikipedia.org/wiki/Tcsh
[Bash]: https://en.wikipedia.org/wiki/Bash_(Unix_shell)


:::

Finding an exact file name
--------------------------

Let's imagine that we know the exact name of a file. I'm going to tell it to
you. The file name that you want to find is "`bananas.md`".

::: example

Change into the `crazy-directories` directory (`cd`).

We can use the `-name` option on `find` to look for a file by name when we know
the exact name of the file:

::: input

```bash
find . -name "bananas.md"
```

:::

:::

Finding a file name matching a pattern
--------------------------------------

Finding a file using a name that we know is straightforward.

Sometimes (maybe more frequently), we only know what the file name *looks like*.
Examples of situations like this might be:

* We want to find all files that have a name ending in "`.java`".
* We want to find all files that have a name containing "`List`".
* We want to find all files that have a name starting with "`Hello`".

Thankfully, we can use "patterns" to help us find files with names where we
don't know the *exact* name of the file.

Patterns require using characters that have special meanings:

* `*` means "anything": any number of characters (0 or more) and any character.
* `?` means "one character": exactly one character, but it can be any character.
* `[` and `]` is a "character class"; `[abc]` means "any of `a`, `b`, or `c`".

::: example

Starting from the `crazy-directories` directory, we're going to be looking for
files that match some specific patterns.

You can find the same file that we saw before (`bananas.md`) using patterns:

::: input

```bash
find . -name "*nanas.md"  # anything ending with "nanas.md"
find . -name "*.md"       # anything ending with ".md"
find . -name "?ananas.md" # anything that has exactly one character, then
                          # ananas.md
find . -name "*bananas*"  # anything that contains "bananas"
find . -name "banana*"    # anything that starts with "banana"
find . -name "[AbC]ananas.md" 
                          # files named "bananas.md", "Aananas.md", or
                          # "Cananas.md"
```

::: 

:::

Finding a file names with unknown case
--------------------------------------

You may have encountered this before while working on the command line,
especially if you're moving between Windows on your personal computer and
Aviary: file names on Unix or Unix-like systems (Linux or macOS) are case
sensitive. That means that "`BANANAS.md`" and "`bananas.md`" and "`bAnAnAs.md`"
are three different file names that could be completely unique on Linux or
macOS.

We *could* use the character class pattern to find files that have any case, but
typing this out would be extraordinarily tedious:

::: input

```bash
find . -name "[Bb][Aa][Nn][Aa][Nn][Aa][Ss].md"
```

:::

Thankfully, there's another option for `find`: `-iname`.

::: example

When you know the general pattern that your file has for its name, but you don't
know what case the file name uses, you can use the `-iname` option; the `i` in
`-iname` stands for "ignore case".

::: input

```bash
find . -iname "bananas.md"
```

:::

You can use any of the special characters (`*`, `?`, or `[]`) with the `-iname`
option.

:::

Running programs on the files you find (with `find`)
====================================================

::: outcomes

* [X] Execute commands on the files that match the pattern.

:::

Sometimes finding the files is enough (i.e., "Great! Now I can open the file
with `vi` or `vim` or `emacs` or ..."). Sometimes you actually want to *do
something* with the files that you find. Let's first explore some of the things
that we might want to *do* to files, and then look at the way we would use
`find` to do those things on our behalf.

What would we want to do?
-------------------------

What kinds of things might you want to do with the files that you find on the
command line using `find`?

* Converting between file formats (e.g., you like to download music using the
  [FLAC] format and need to convert to [MP3]).
    * Or... you have many "`.md`" files that you want to convert to "`.docx`".
* Changing files (e.g., you have many very large photos that you want to also
  have smaller versions of, or "thumbnails").
* Deleting files (e.g., you have many `.class` files, and you want to delete
  them all).

[FLAC]: https://en.wikipedia.org/wiki/FLAC
[MP3]: https://en.wikipedia.org/wiki/MP3

Using `find` to accomplish our goal
-----------------------------------

We're going to use two options on `find` to accomplish our goal: `-exec` and
`-delete`.

### `-delete`

Deleting files is pretty straightforward using the `-delete` option.

::: warning

Remember: **There is no "Recycle Bin" or "Trash Can" on the command line**. When
you delete something using either with `rm` or with the option we're about to see,
it's **gone**.

:::

::: example

Let's delete the file with the exact file name `bananas.md`:

::: input

```bash
find . -name "bananas.md" -delete
```

:::

The `-delete` option on `find` deletes any file that has a name matching the
pattern that you've described to `find`. That means that if multiple files
match the pattern, then all of those files would be deleted with the `-delete`
option.

:::

### `-exec`

More often than deleting stuff, you're going to want to run a program on the
things that you find.

Similar to the way that the `-delete` option works (it deletes all files that
have a name matching the pattern), the `-exec` option will run a program for
each file that has a name matching the pattern.

The `-exec` option is *slightly* differently from `-delete` in that you need to
include how to run the command, but the best way to describe this is by example.

::: example

Let's start by finding all Markdown files in the `crazy-directories` directory:

::: input

```bash
find . -name "*.md" # find all files with the extension .md
```

:::

There are a few more than expected!

We want to convert all of these Markdown files to Word files (`.docx`). Doing
this manually is possible, but tedious, so we'll let `find` to the work for us:

::: input

```bash
find . -name "*.md" -exec pandoc '{}' -f markdown+emoji -o '{}'.docx \;
```

:::

There's some weird looking stuff in there, so let's break it down:

* ```bash
  find . -name "*.md" # find all files with the extension .md
  ```

  This is the same as what we've seen before: find all files with names that
  match the pattern.
* ```bash
  -exec
  ```

  Here's the start of our new option for `find`. Everything that follows the
  `-exec` option is another complete command.
* ```bash
  pandoc '{}' -f markdown+emoji -o '{}'.docx \; 
         # run pandoc on the name of the file
         # quote it in case there are spaces;
         # The output file is the same file name
         # with a .docx extension (Word), and the
         # command is terminated with \;
  ```

  * We've seen `pandoc` before lots of times. 
  * One new thing here is the `'{}'` (twice).
    * When `pandoc` is run by `find`, the `{}` is replaced with the name of the
      file that `find` found. The quotes are around `{}` in case the name of the
      file that `find` found contains spaces. In our example, one of the files
      `find` finds is `bAnAnAs.md`, and this would make the command look like:

      ```bash
      pandoc 'b/5/s/bAnAnAs.md' -f markdown+emoji -o 'b/5/s/bAnAnAs.md'.docx \;
      ```
  * The `-f markdown+emoji` is an option to `pandoc` to say that we want it to
    actually render emoji using shortcodes.
  * The `\;` is the "end of command" marker that the `-exec` option looks for so
    it knows where the command ends.

If everything works out, we shouldn't see any output (`pandoc` is pretty quiet).

Now check out the new files you have in your directory:

::: input

```bash
find . -name "*.docx"
```

:::

:::

The `-exec` option sure looks *weird*, but it's a pretty powerful option: we can
find files that have a name matching a pattern, and then run commands on those
files with a single command.
