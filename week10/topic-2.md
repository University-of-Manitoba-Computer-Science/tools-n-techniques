---
title: Programs requiring dependencies
author: Franklin Bristow
---


Programs requiring dependencies
===============================

::: outcomes

* [X] Download and run a program that requires to you to install dependencies.

:::

When you're working at school you're building almost everything from the ground
up: data structures, abstract data types, working with structured and
unstructured data, implementing algorithms.

When you get into the real world things suddenly change: your boss is probably
going to be annoyed with you if you spend an afternoon building a linked list
in a language that has extensive support for [a variety of different types of
collections]. More often than not in the real world, you're going to be writing
software that depends on other software: other programs, other libraries, or
other frameworks of code.

While you're (probably) most familiar with languages like Java, we're going to
take a diversion and look at downloading and running a program in Python that
requires some external dependencies.

[a variety of different types of collections]:
https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/doc-files/coll-index.html


Downloading the program
-----------------------

The program you're going to be using as an example is actually something that
extends [Pandoc]: a "filter" for Pandoc.

You can find the repository here:

    https://code.cs.umanitoba.ca/cs-lab-course/suppress-notes

You're going to want to get this into your user directory on Aviary (Download a
zip from GitLab and `unzip`, `git clone`, whatever works best for you).

::: challenge

Do this entirely on your own machine *on the command line*. This is easier on
macOS than Windows because `unzip` is already installed. 

If you do this on your own machine, you're on your own, but be forewarned that
you're going to need to install Python ([on Windows] or [on macOS]).

[on Windows]: https://docs.python.org/3/using/windows.html
[on macOS]: https://docs.python.org/3/using/mac.html

:::

[Pandoc]: https://pandoc.org

Dependency management in Python
-------------------------------

Dependency management in Python is... [not exactly a solved problem].

We're going to stick to the basics, though, and use Python's [`pip`]. `pip` is a
command-line tool that you can use to install Python libraries (or packages)
that you can then use (or depend on) in your own Python programs.

Using `pip` is pretty easy (once you know the dependency that you want):

1. Figure out what the name of the dependency is.
2. Install the dependency with `pip install`.

::: example

Assuming you know what the name of your dependency is, installing it is
straightforward with `pip`. Let's assume that you're building a command-line
tool in Python and you want to make it look [*real shiny*]. A Python package you
can use to make your command-line tools look great is [`rich`]. Once you know
the name of the package (`rich` in this case), you can use `pip` to install your
dependency:

```bash
pip install rich
```

:::

`pip` gives us the ability to quickly install dependencies on the command line,
and it installs the most recent version of the library by default.

We can also install specific versions of dependencies, or versions that meet
specific criteria:

```bash
# install exactly this version
pip install rich==12.6.0
# install a version that's compatible with X
pip install rich~=12.6.0
```

In this context, "compatible with" means that the API (the functions you're
calling in the package) are still the same, but there might be releases that are
newer that have important security or other bug fixes.

[not exactly a solved problem]:
https://stackoverflow.com/questions/54475042/python-dependency-hell-a-compromise-between-virtualenv-and-global-dependencies
[`pip`]: https://pypi.org/project/pip/
[*real shiny*]: https://www.youtube.com/watch?v=93lrosBEW-Q
[`rich`]: https://pypi.org/project/rich/

### Listing project dependencies

Installing individual dependencies on the command line is fine, and is a good
way for us to very quickly get to work when we're trying to build something
without having to worry about versions.

When you're ready to actually distribute your code to other people, though,
you're suddenly depending on both specific versions of packages that you had
installed when you were writing your code, and ... well, probably a lot of
different packages.

You *can* just list out instructions for the users of your program or package:

```md
My really cool project
======================

This is my amazing project :tada:!

Installing
----------

You need to install the following dependencies with `pip`:

* `rich` version 12.6.0
* `click` version 8.0.3
* `Pillow` version 9.0.1
```

... but that would be tedious for anyone using your code (*you* know how to use
`pip` now, but this would be tedious; can you imagine your parents doing
this???).

Thankfully, `pip` can read files that contain a listing of the dependencies that
you have for your project: a file named `requirements.txt`.

`requirements.txt` is a file that straight-up lists the dependencies and their
versions, everything that comes after `pip install`.

::: example

Here's a `requirements.txt` that describes the dependencies for the amazing
project above:

```plain
rich==12.6.0
click==8.0.3
Pillow==9.0.1
```

:::

`pip`'s requirements files can also have comments, though it's restricted to
line that *start with* `#`.

::: example

Here's the same `requirements.txt`, but one that has comments:

```plain
# we need rich 12.6.0 for a very important, but arbitrary reason.
rich==12.6.0
# we use click for handling command line arguments
click==8.0.3
# Pillow is a great image processing library
Pillow==9.0.1
```

:::

Once we've got a file that has these dependencies listed, we can use `pip` to
install the dependencies all at once with `pip install -r`.

::: example

If you have a file named `requirements.txt` that has the contents listed above,
you can use `pip` to install the dependencies:

```bash
pip install -r requirements.txt
```

:::

You can write your own `requirements.txt` by hand, but you can also generate one
using the command `pip freeze`. `pip freeze` will list *all* versions of *all*
Python packages currently on your system (even ones you didn't install and ones
that are unrelated to your program), but will give you a comprehensive list of
the state of your system.

::: example

You can use `pip freeze` and some output redirection to generate a
`requirements.txt`:

```bash
pip freeze > requirements.txt
```

:::

::: aside

How important is it that your file is named `requirements.txt`? Not at all! You
could call it "`dependencies.txt`". You could call it "`cats are cool.txt`". You
could call it "`dogs drool.txt`". (Can you sense a theme here? :cat:)

The name `requirements.txt` is a ["de facto" standard]. All that matters is that
what comes after the `-r` option is the name of a file that follows the standard
of "one package and version per line".

["de facto" standard]: https://en.wikipedia.org/wiki/De_facto_standard

::: 

Installing the dependencies
---------------------------

The repository that you downloaded/cloned/whatever has a list of requirements as
`requirements.txt`. You should install those requirements for this project.

Running the program
-------------------

The repository that you downloaded/cloned/whatever has a `README.md` that
describes how to run the software. You should read the `README.md` to see how to
run the software.

After you get the software running, just for the sake of seeing what can happen
when you don't install dependencies for a Python project.

::: example

Let's start by uninstalling dependencies with `pip`:

```bash
[you@bird suppress-notes]> pip uninstall -r requirements.txt
Found existing installation: panflute 1.12.5
Uninstalling panflute-1.12.5:
  Would remove:
    /home/you/.local/bin/panfl
    /home/you/.local/bin/panflute
    /home/you/.local/lib/python3.10/site-packages/panflute-1.12.5.dist-info/*
    /home/you/.local/lib/python3.10/site-packages/panflute/*
Proceed (Y/n)? Y
  Successfully uninstalled panflute-1.12.5
```

Now try running the software using the instructions again (through Pandoc, but
don't pipe to `lynx`); what kind of output do you see now?

Python is helpful enough to tell you the name of the missing package:

```
Traceback (most recent call last):
  File "/home/you/suppress-notes/./suppress-notes", line 3, in <module>
    import panflute as pf
ModuleNotFoundError: No module named 'panflute'
Error running filter suppress-notes:
Filter returned error status 1
```

If you're planning on using this filter again, you should reinstall the
dependencies with `pip`:

```bash
pip install -r requirements.txt
```

:::

Further reading
---------------

Dependency management in Python is... [not exactly a solved problem].

Pip is the best place to start with Python package and dependency management
because it comes for free as part of Python itself (Python's got ["batteries
included"]).

That said, not everyone agrees that Pip alone is the right choice, or even
agrees if Pip is the right tool at all.

You can read a little more about dependency management and packaging in Python
in a couple of places:

* You might be noticing that we're installing specific versions of packages
  "globally"; installing with `pip` means we're installing into a folder in our
  own user directory that any Python program we run will use. Sometimes we'll
  have multiple different Python programs that use the same dependency, but rely
  on different versions that aren't compatible with one another (`panflute` is
  fixed at version 1.12.5 in `suppress-notes`, but the most recent version if
  `panflute` is 2.1.X, these are not compatible with one another).

  Python has something called "[virtual environments]" where you can install
  dependencies for a specific program in a specific directory rather than
  "globally".
* [Poetry] is a more advanced tool than `pip` that is both a dependency manager
  and a build and packaging tool for Python. Poetry doesn't work with `pip`, but
  instead replaces `pip`.

["batteries included"]:
https://www.computer.org/csdl/magazine/cs/2007/03/c3007/13rRUzpQPH7
[virtual environments]: https://docs.python.org/3/tutorial/venv.html
[Poetry]: https://python-poetry.org/
