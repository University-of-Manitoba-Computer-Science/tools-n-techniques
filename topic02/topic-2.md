---
title: "Command line file management"
author: Franklin Bristow
---

<iframe width="560" height="315"
src="https://www.youtube.com/embed/gkZa1S5eJ6U?si=iJreZyfZ8a5AIFH6"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

::: outcomes

* [X] Create, rename, delete, and inspect folder structures on the command-line.
* [X] Navigate folder structures on the command-line.

:::

Being connected to a remote computer is nice, but we really want to be able to
actually *do* stuff on that remote computer. The very first thing we're going to
do is to re-do something that we did in the [last unit] --- we're going to
navigate around folder structures and create new folders, ultimately to
re-create the folder structure you created in the last unit.

[last unit]: ../topic01/topic-5.html

:eyes: Looking around
=====================

When you connect to a remote computer you're interacting with a program called a
"shell". When you see something that looks like

```
[you@bird ~]>
```

the shell is patiently waiting for you to type some commands into it to tell it
what to do.

Let's start by running a command that will ask the shell to print out the
contents of the **current working directory**. Note: the words "directory" and
"folder" are synonyms for each other, so any time someone is talking about a
directory, they mean folder.

::: example

The `ls` command asks the shell to print out the files and folders that are in
the current directory.

Type `ls` into your terminal, then press <kbd>Enter</kbd>:

:::::: columns
::: {.column .input width=50%}

```bash
ls
```
:::
::: {.column .output width=50%}

```
bin  Mail
```

:::
::::::

The folders that you see here were created for you when your account on the
remote computer was created. What you see may not be *exactly* the same as what
is shown here.

:::

:hammer_and_wrench: Making a directory
======================================

While `bin` and `Mail` are good directories to have, they don't represent what
we want to actually keep on our remote computer, so let's start making some of
our own folders.

We're going to start small, let's make a new folder. When we made folders with
our visual file explorers we mostly used our mice, though you may have used a
keyboard shortcut. While you can literally click on your terminal window,
clicking on the terminal window isn't actually going to do anything other than
making a fun clicking sound from your mouse (if you're literally using a mouse)
or a faint tapping sound as you tap your touchpad. Instead, we're going to need
to use a new command to create a folder: `mkdir`.

::: example

The `mkdir` command will create a new folder that has the name that you pass to
it on the command line.

Type `mkdir hello` into your terminal, press <kbd>Enter</kbd>, then re-run `ls`:

:::::: columns
::: {.column .input width=50%}

```bash
mkdir hello
ls
```

:::
::: {.column .output width=50%}
```
bin  hello  Mail
```

:::
::::::

:::

You just made a new folder :tada:!

::: aside

One (minor) problem with making folders in our terminal is that we can't use
spaces `' '` in the same way that we could when making folders in our visual
file explorers:

:::::: columns
::: {.column .input width=50%}
```bash
mkdir hello world
ls
```
:::
::: {.column .output width=50%}
```
hello  world
```
:::
::::::

This didn't make one folder named `hello world`, it made *two folders*, one
named `hello` and one named `world`. You've got a few options:

1. Don't use spaces at all and instead use dashes `-` or underscores `_` to
   represent spaces, or just don't have spaces (similar to naming variables).

   ```bash
   mkdir hello-world
   mkdir hello_world
   mkdir helloworld
   ```
2. Put quotes around the name that includes spaces.

   ```bash
   mkdir "hello world"
   mkdir 'hello world'
   ```
3. Escape the spaces with a backslash character `\`.

   ```bash
   mkdir hello\ world
   ```

The issue with spaces is common to **all** commands on the command line. This is
a good opportunity to choose a new personal preference: When you're working on
the command line, do you want to always use dashes, underscores, or no spaces at
all?

:::

:compass: Navigating directories
================================

Now that we've made a directory, we need to be able to "open" the directory.
When we used visual file explorers, we "opened" the directory (either in a new
window or in the same window) by double-clicking on the icon.

Again, we *can* double-click on our terminal window, but that double-clicking
isn't doing anything other than making fun clicking or tapping sounds. To "open"
a directory that we created, we need to "change" to that directory using a new
command: `cd`

::: example

If the name of the folder that you created with `mkdir` is `hello`, then you
should be able to change into `hello` with `cd`:

:::::: columns
::: {.column .input width=50%}

```bash
ls
```
:::
::: {.column .output width=50%}
```
bin  hello  Mail
```
:::
::::::
:::::: columns
::: {.column .input width=50%}

```bash
cd hello
ls
```
:::
::: {.column .output width=50%}
There should be no output (the directory is empty, you just made it!), but your
**prompt** will change to look something like:

```
[you@bird hello]>
```
:::
::::::

:::

Now that you've changed *into* a directory, you also need to be able to change
*out of* a directory. When you changed into your directory `hello`, you moved
"down" a folder. You can move "up" a folder by changing to the "parent"
directory using a special directory name `..` (two periods). You can also go
back to your "home" directory (your user folder on this remote computer) by
using a special directory name `~` ([tilde]; I say this as 'till-duh', but I've
also heard 'till-dee').

::: example

You can change to the parent directory of the current directory (the directory
this directory is in) using `..`.

```bash
cd ..
```

You can change back to your user directory at any time from anywhere using `~`.

```bash
cd ~
```

:::

The last part of being able to move around in a directory structure on a remote
computer is knowing where you are. Our shell has a concept of a "working
directory". Thinking about visual file explorers, this is the window in our file
explorer that we're currently looking at. We can ask our shell to tell us what
directory we're currently in using the `pwd` command, `pwd` stands for **p**rint
**w**orking **d**irectory.

::: example

Type `pwd` into your terminal, then press <kbd>Enter</kbd>. The directory that
you're currently "in" will be printed out.

:::::: columns
::: {.column .input width=50%}

```bash
pwd
```

:::
::: {.column .output width=50%}
```
/home/student/you
```
:::
::::::

Now try changing into `hello` and re-run `pwd` to see that the directory you're
"in" has changed:

:::::: columns
::: {.column .input width=50%}

```bash
cd hello
pwd
```
:::
::: {.column .output width=50%}
```
/home/student/you/hello
```
:::
::::::

:::

[tilde]: https://en.wikipedia.org/wiki/Tilde

:pencil2: Moving and renaming directories
=========================================

Sometimes when making a directory you realize that you made the directory in the
wrong place, or you gave it the wrong name (or misspelled the name). 

You can rename or move a directory from one place to another (or both at the
same time!) with the `mv` command.

::: example

You can rename a directory with `mv`.

:::::: columns
::: {.column .input width=50%}

```bash
ls
```
:::
::: {.column .output width=50%}
```
bin  hello  Mail
```

We should see a directory named `hello` because of the `mkdir` we ran before.
:::
::::::
:::::: columns
::: {.column .input width=50%}
```bash
mv hello not-hello
ls
```
:::
::: {.column .output width=50%}
```
bin  Mail  not-hello
```
:::
::::::

You can *move* a directory into another directory with `mv`, too.

:::::: columns
::: {.column .input width=50%}
```bash
# intentionally making two directories
mkdir hello world 
ls
```
:::
::: {.column .output width=50%}

```
bin Mail hello world
```
:::
::::::
:::::: columns
::: {.column .input width=50%}
```bash
mv hello world/   # move hello *into* world/
cd world          # change into world
ls                # now hello is *in* world/
```
:::
::: {.column .output width=50%}
```
hello
```
:::
::::::
:::::: columns
::: {.column .input width=50%}
```bash
ls ..         # hello is *not* in ~
```
:::
::: {.column .output width=50%}
```
bin Mail world
```
:::
::::::

:::

Just like with `cd`, you can use the special directories `..` and `~` to move
(`mv`) a file into the parent directory, list (`ls`) files in the parent
directory, or move (`mv`) files into your user directory (or list your user
directory with `ls ~`). You can also use another special directory name `.` (one
period) to move something to or from the **current** directory.

::: example

You can move a directory to or from your home directory with `~` and use the `.`
directory to move things into or from the current directory.

:::::: columns
::: {.column .input width=50%}
```bash
cd world
mv hello ~   # move hello to your user directory
ls
```
:::
::: {.column .output width=50%}

There should be no output, we just moved `hello` out of the directory.

:::
::::::
:::::: columns
::: {.column .input width=50%}
```bash
# move hello back into *this* directory
mv ~/hello . 
ls
```
:::
::: {.column .output width=50%}

```
hello
```

:::
::::::

:::

:wastebasket: Removing directories
==================================

Sometimes you don't need a directory anymore and you want to remove it. You can
remove directories using two different commands: `rm` and `rmdir`.

::: example

You can remove *empty* directories using the `rmdir` command, and this is
*usually* the command you want to use to try removing a directory.

```bash
rmdir hello
```

If you try to remove a directory that has other stuff in it (files or folders),
`rmdir` will warn you and refuse to remove the directory:

:::::: columns
::: {.column .input width=50%}
```bash
mkdir hello
# makes a directory in hello named world
mkdir hello/world 
rmdir hello
```
:::
::: {.column .output width=50%}

```
rmdir: failed to remove directory 'hello': Directory not empty
```
:::
::::::

You can remove files and directories using the `rm` command, and you can remove
directories that have things in them by asking `rm` to remove *recursively*.

```bash
rm -r hello # remove hello and all of its contents
```

The `rm` command itself will refuse to remove directories unless you tell it to
remove them recursively.

:::::: columns
::: {.column .input width=50%}

```bash
rm hello
```
:::
::: {.column .output width=50%}
```
rm: cannot remove 'hello': Is a directory
```
:::
::::::

:::

::: aside

The command line doesn't have a concept of a "temporary trash location" like
Windows (the recycle bin) or macOS (the trash can). When you put something into
the recycle bin or trash can, you can always open the recycle bin or trash can
and get the file back, restoring it to its original location.

When you remove a file or folder on the command line (using `rm` or `rmdir`),
the file or folder is removed and you **can't** get it back, unless you've
[backed it up somewhere].

[backed it up somewhere]: ../topic11/topic-1.html

:::
