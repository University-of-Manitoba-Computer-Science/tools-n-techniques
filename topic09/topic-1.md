---
title: Introduction
author: Franklin Bristow
---

Introduction
============

Right now building a program doesn't really seem like a hard problem: you hit
the Compile and/or Run buttons (whatever they look like for you), your program
runs and does *stuff* :tada:.

When your program consists of a single file, it can and should be that easy to
build your code. But as the size of your code grows beyond one single file,
building your program can become difficult and tedious. This week we're going to
spend some time looking at tools for building software from source code, and
look at building source code for different programming languages.

As your programs grow in complexity, you're also going to want to rely on source
code and programs that have been developed by *other people*. We'll take a look
at some approaches to downloading and using third-party libraries of code that
aren't included as part of the language itself (I'm looking at you incredibly
huge JDK!).

::: outcomes

By the end of this week you should be able to:

* [ ] Download and run a program that requires you to install dependencies.
* [ ] Create a `Makefile` to accomplish a task (building software, running
  commands).
* [ ] Create a new empty software project that includes a build and dependency
  management tool.
    * [ ] Add and use a new dependency in a software project.

:::

Languages
---------

This isn't a programming course&trade;.

While this isn't a programming course, we're kind of required to look at the
topics we're looking at this week in the context of programming languages:

* Installing dependencies with Python.
* Using `make` with C (but also other stuff).
* Build and dependency management with [Maven] and Java.

While you almost certainly know some dialect of Java, the examples we're going
through are less about knowing the language, and more about knowing how to get a
program already written in that language up and running.

[Maven]: https://maven.apache.org/
