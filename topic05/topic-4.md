---
title: "Reading and changing permissions"
author: Franklin Bristow
---

::: outcomes

* [X] Read and change permissions on files.

:::

Finding files by name and filtering lines in files is useful (I promise!).

We're going to switch gears a little bit and spend some time looking at files
and permissions.

You probably haven't spent a lot of time thinking about permissions. Permissions
on files are metadata (there's that word again; data about the data) that your
operating system (Windows, macOS, Linux) uses to decide whether or not you or
other users are allowed to read, write, or execute (run) a file.

You probably haven't spent a lot of time thinking about permissions partly
because you're probably the only person using your computer; why would you care
about permissions when nobody else is going to use your computer?

That's true, but now you are using computers that have other people using them:
Aviary.

::: aside

Who else uses Aviary? There are currently more than 1000 active user accounts on
the CS Linux systems, mostly undergraduate students, but also faculty and other
staff.

You can find out who else is currently logged in to the bird machine that you're
connected to (remember: Aviary has about 25 computers in it) using the `w`
command:

:::::: columns
::: {.column .input width=20%}

```bash
w 
```
:::
::: {.column .output width=80%}
```
 19:44:05 up  3:03,  2 users,  load average: 0.08, 0.07, 0.09
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
you      pts/2    tmux(7408).%0    Mon14    1.00s  6:29   0.03s w
you      pts/3    tmux(7408).%2    Tue19    5.00s 13.95s 13.54s vi notebook.md
```

(I guess it's just you).

The output you see from `w` will differ depending on who else is currently
connected to that specific machine in Aviary!
:::
::::::

:::

Permissions are important in multi-user systems like this.

Reading permissions
===================

Let's start by checking the permissions on our files. We'll use a command that
we've used frequently: `ls`

::: example

Let's print out the "long" listing of all the files in our current directory
using the `-l` option (that's a lower case L):

:::::: columns
::: {.column .input width=20%}

```bash
ls -l
```

:::
::: {.column .output width=80%}

```
total 17100
drwxr-xr-x 1 you csunderg       52 Oct  3 14:39 crazy-directories/
-rw-r--r-- 1 you csunderg  1239277 Oct  2 16:24 crazy-directories.zip
-rw-r--r-- 1 you csunderg 16012093 Jun 16 12:49 MonkeyPox.fn
```

:::
::::::

Your output will look a little different than this (you've probably got
different files and directories), but it should look similar to this.

:::

Files and directories have a concept of ownership (a user account and a "group"
own a file), and permissions for three distinct sets of people (the user account
that owns it, the group that owns it, and everyone else "other" or "world").

You can see which user account owns a file in the second column of output from
`ls -l`. All files that are in your user directory should be owned by your user
account.

You can see which group owns a file in the third column of output from `ls -l`.
Your user accounts are in the `csunderg` group, so that's the group that "owns"
these files.

We can see which permissions each set of people has in the first column. Let's
take apart the first column in pieces:

```
drwxr-xr-x
|||||||||| 
|uuugggooo # u = user, g = group, o = other
-> type
```

The directory `crazy-directories` has the following metadata for permissions:

* It is a directory, so the first letter is `d`. Files have a first letter of
  `-`.
* Your user account (the `u` part) has all permissions on it: Read, Write, and
  eXecute.
* The group (the `g` part) has only the ability to Read and eXecute this
  directory.
* Similarly, other users (the `o` part) have the ability to Read and eXecute
  this directory.

::: aside

When I think of the word "execute" in the context of the command line, I think
about running a program. Why do directories have execute permissions and other
regular files don't?

This is an unfortunate case of something being [overloaded] and having multiple
meanings in different contexts.

[overloaded]: https://en.wikipedia.org/wiki/Function_overloading

When a regular file has the eXecute permission, that means that you can run it
like a program. When a directory has the eXecute permission, that means that you
can change into that directory with `cd`. :shrug:

:::

User, group, and other have different uses in different places, and we'll see an
example of this later in an assignment.

Changing permissions
====================

Seeing permissions is an important part of knowing what we need to change, when
we need to change it.

We can change permissions on files using a program called `chmod`.

::: example

We can change the permissions for user, group, and world on files or directories
using `chmod`. `chmod` will let us specify permissions for each of user, group,
and other. Let's change then inspect some permissions on `crazy-directories`.
Try running each of these one at a time, then running `ls -l` to see how the
permissions have changed each time.

```bash
chmod u-x crazy-directories # remove (-) the eXecute permission for user
chmod a+x crazy-directories # add (+) the eXecute permission for everyone
chmod ug-r crazy-directories # remove read permissions for user and group
chmod ug+r crazy-directories # add back read permissions for user and group
```

:::
