---
title: Summary
author: Franklin Bristow
---

Summary
=======

This has been a bit of a whirlwind through some topics related to running
programs on Linux or UNIX-like systems, with us learning a little bit about
things that apply to *all* programs (how and where they get input, and how and
where they send output).

Depending on the path you take through CS, you may eventually learn about the
underlying mechanisms of how this all works (maybe) in an operating systems
course, specifically about how an operating system (OS) represents "processes"
(running programs) as a data structure, and how the OS keeps track of files that
a process has open (`STDIN`, `STDOUT`, and `STDERR` are all special
file-like-things&trade;; neat :camera:).

But let's be honest: backing up stuff is boring. Well, it's boring right up until
you actually need the back up. And sometimes we don't *think* about backups
right up until we need them. This week is an opportunity to consider what you're
doing for back ups, and to give you an opportunity to *back up your stuff*.

Backing up isn't just making sure that you've got a copy of your files, it's
copying your files across devices and locations. It's also a choice of how you
do back ups in the first place: file-based or image-based.

Regardless of how you do back ups, restoring and verifying your back ups is an
essential part of confirming that you *actually have a back up* and not just a
bunch of [random bits and bytes].

[random bits and bytes]: https://en.wikipedia.org/wiki/Garbage

You should now be able to:

::: outcomes

* [X] Redirect the output from a program to a file.
* [X] Redirect a file to be the input for a program.
* [X] Send data between programs using a pipe.
* [X] Choose an appropriate back up strategy for protecting your files.
* [X] Install and configure software to back up your files to a remote server.
* [X] Restore and verify your back up from the remote server.

:::

Now you should be ready to start working on the assignment this week!
