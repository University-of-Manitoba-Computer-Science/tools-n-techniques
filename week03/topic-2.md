---
title: "Command line file management"
author: Franklin Bristow
---

Creating folders and finding your way around
============================================

::: outcomes

* [X] Create, rename, delete, and inspect folder structures on the command-line.
* [X] Navigate folder structures on the command-line.

:::

Being connected to a remote computer is nice, but we really want to be able to
actually *do* stuff on that remote computer. The very first thing we're going to
do is to re-do something that we did last week --- we're going to navigate
around folder structures and create new folders, ultimately to re-create the
folder structure you created last week.

:eyes: Looking around
---------------------

When you connect to a remote computer you're interacting with a program called a
"shell". When you see something that looks like

```bash
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

```bash
[you@bird ~]> ls
bin  Mail
[you@bird ~]>
```

The folders that you see here were created for you when your account on the
remote computer was created. What you see may not be *exactly* the same as what
is shown here.

:::

:hammer_and_wrench: Making a directory
--------------------------------------

While `bin` and `Mail` are good directories to have, they don't represent what
we want to actually keep on our remote computer, so let's start making some of
our own folders.

We're going to start small, let's make a new folder. When we made folders with
our visual file explorers we mostly used our mice, though you may have used a
keyboard shortcut.. While you can literally click on your terminal window,
clicking on the terminal window isn't actually going to do anything. Instead,
we're going to need to use a new command to create a folder: `mkdir`.

::: example

The `mkdir` command will create a new folder that has the name that you pass to
it on the command line.

Type `mkdir hello` into your terminal, press <kbd>Enter</kbd>, then re-run `ls`:

```bash
[you@bird ~]> mkdir hello
[you@bird ~]> ls
bin  hello  Mail
[you@bird ~]>
```

:::

You just made a new folder :tada:!

::: aside

One (minor) problem with making folders in our terminal is that we can't use
spaces `' '` in the same way that we could when making folders in our visual
file explorers:

```bash
[you@bird ~]> mkdir hello world
[you@bird ~]> ls
hello  world
[you@bird ~]>
```

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

The issue with spaces is common to **all** commands on the command line, so my
advice is to try avoiding their use.

:::

:compass: Navigating directories
--------------------------------

Now that we've made a directory, we need to be able to "open" the directory.
When we used visual file explorers, we "opened" the directory (either in a new
window or in the same window) by double-clicking on the icon.

Again, while we can click on our terminal window, clicking isn't doing anything.
To "open" a directory that we created, we need to "change" to that directory
using a new command: `cd`

::: example

If the name of the folder that you created with `mkdir` is `hello`, then you
should be able to change into `hello` with `cd`:

```bash
[you@bird ~]> ls
bin  hello  Mail
[you@bird ~]> cd hello
[you@bird hello]> ls
[you@bird hello]>
```

Notice that when you changed into `hello`, your **prompt** changed from `~` to
`hello`!

:::

Now that you've changed *into* a directory, you also need to be able to change
*out of* a directory. When you changed into your directory `hello`, you moved
"down" a folder. You can move "up" a folder by changing to the "parent"
directory using a special directory name `..` (two periods). You can also go
back to your "home" directory (your user folder on this remote computer) by
using a special directory name `~` (tilde).

::: example

You can change to the parent directory of the current directory (the directory
this directory is in) using `..`.

```bash
[you@bird hello]> cd ..
[you@bird ~]> 
```

You can change back to your user directory at any time from anywhere using `~`.

```bash
[you@bird hello]> cd ~
[you@bird ~]>
```

:::

The last part of being able to move around in a directory structure on a remote
computer is knowing where you are. Our shell has a concept of a "working
directory". Thinking about visual file explorers, this is the folder that we're
currently looking at. We can ask our shell to tell us what directory we're
currently in using the `pwd` command, `pwd` stands for **p**rint **w**orking
**d**irectory.

::: example

Type `pwd` into your terminal, then press <kbd>Enter</kbd>. The directory that
you're currently "in" will be printed out.

```bash
[you@bird ~]> pwd
/home/student/you
[you@bird ~]>
```

Now try changing into `hello` and re-run `pwd` to see that the directory you're
"in" has changed:

```bash
[you@bird ~]> cd hello
[you@bird hello]> pwd
/home/student/you/hello
[you@bird hello]>
```

:::


:pencil2: Moving and renaming directories
-----------------------------------------

Sometimes when making a directory you realize that you made the directory in the
wrong place, or you gave it the wrong name (or misspelled the name). 

You can rename or move a directory from one place to another (or both at the
same time!) with the `mv` command.

::: example

You can rename a directory with `mv`.

```bash
[you@bird ~]> ls
bin  hello  Mail
[you@bird ~]> mv hello not-hello
[you@bird ~]> ls
bin  Mail  not-hello
```

You can *move* a directory into another directory with `mv`, too.

```bash
[you@bird ~]> mkdir hello world # intentionally making two directories
[you@bird ~]> mv hello world/
[you@bird ~]> cd world
[you@bird world]> ls
hello
[you@bird world]>
```

:::

Just like with `cd`, you can use the special directories `..` and `~` to move a
file into the parent directory or into your user directory. You can also use
another special directory name `.` (one period) to move something to or from the
**current** directory.

::: example

You can move a directory to or from your home directory with `~` and use the `.`
directory to move things into or from the current directory.

```bash
[you@bird ~]> cd world
[you@bird world]> mv hello ~ # move hello to your user directory
[you@bird world]> ls
[you@bird world]> mv ~/hello . # move hello back into *this* directory
```

:::

:wastebasket: Removing directories
----------------------------------

Sometimes you don't need a directory anymore and you want to remove it. You can
remove directories using two different commands: `rm` and `rmdir`.

::: example

You can remove *empty* directories using the `rmdir` command, and this is
*usually* the command you want to use to try removing a directory.

```bash
[you@bird ~]> rmdir hello
```

If you try to remove a directory that has other stuff in it (files or folders),
`rmdir` will warn you and refuse to remove the directory:

```bash
[you@bird ~]> mkdir hello
[you@bird ~]> mkdir hello/world # makes a directory in hello named world
[you@bird ~]> rmdir hello
rmdir: failed to remove directory 'hello': Directory not empty
```

You can remove files and directories using the `rm` command, and you can remove
directories that have things in them by asking `rm` to remove *recursively*.

```bash
[you@bird ~]> rm -r hello # remove hello and all of its contents
```

The `rm` command itself will refuse to remove directories unless you tell it to
remove them recursively.

```bash
[you@bird ~]> rm hello
rm: cannot remove 'hello': Is a directory
```

:::

::: aside

The command line doesn't have a concept of a "temporary trash location" like
Windows (the recycle bin) or macOS (the trash can). When you put something into
the recycle bin or trash can, you can always open the recycle bin or trash can
and get the file back.

When you remove a file or folder on the command line, the file or folder is
removed and you can't get it back (easily or at all).

:::
