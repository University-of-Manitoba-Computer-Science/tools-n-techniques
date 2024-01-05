---
title: Debuggers
author: Franklin Bristow
---

Debuggers
=========

Pencil and paper debugging is tedious and painful, but effective. Log-based
debugging is less tedious (maybe) and less painful (no risk of poking yourself
with a pencil when you're not using a pencil), and while easy, don't always work
(for example, a `printf` in a C program that's before a line that crashes won't
always print before the program crashes). 

Despite being tedious, painful, and not always working, these strategies for
debugging are approachable because they use tools that you have to know about to
do programming in the first place, and they are *universal*: you can use
log-based debugging in any language where you can print or produce output, and
you can use pencil-and-paper debugging anywhere you've got a pencil, and paper.

Nevertheless, they are painful. Painful and tedious.

A debugger is a program that you can use to help you debug a program. Debuggers
are usually very tightly coupled to the programming language or environment that
you're using (you use a Java debugger to debug Java programs, you use a Python
debugger to debug Python programs, and you use a C debugger to debug C
programs).

All debuggers give you generally the same tools for working with your program,
and we generally use them in the same way. A debugger will let us run one line
of code at a time and inspect the values that variables have when the line of
code has completed running.

Almost all debuggers will use the same general terminology to describe actions
or ideas:

* A **break point** is a way for you to tell the debugger where and when it
  should pause running your program. We can say things like "Start running from
  the beginning, then pause when you get to line 158."
* We can **step into** a function or method call when the line we're about to
  run is a function or method call. Stepping into the function or method call
  means that our debugger will "move" to the code for the function, then let us
  run lines inside that function.
* We can **step over** a line, running whatever the line was and then pausing on
  the next line of code.
* We can **inspect** values, either by printing them out, or by seeing their
  values in a window or pane.
