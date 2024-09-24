---
title: "Introduction"
author: Franklin Bristow
---

We're getting comfortable with using the command line, managing folders and
files, and writing structured text, but all you've been doing in your CS courses
(if you're taking CS courses!) up to this point has been programming, and the
things we've been doing in this course haven't exactly been related to
programming.

We're going to switch things up a bit: we're not going to do any programming,
but we are going to look at how to compile and run code on Linux systems (we'll
do Java, Python, and C). Even if you don't know how to program, knowing how to
compile and run code can help with work or research you might be doing that has
nothing to do with Computer Science.

... and while it's cool :sunglasses: to be able to compile and run code on
remote systems and you're definitely going to have to do this lots in the
future, it's, uh, not exactly a significant amount of course material.

Our bigger topic is going to be an introduction to [version control]. Version
control can help you in a couple of different ways, whether you're taking CS
courses or not:

* Sometimes when working on code, I (me, Franklin) will find myself in a
  situation where some of my code doesn't work, but it *sorta* works. So: I copy
  and paste the chunk of code, comment one of the chunks and edit the other
  because I was worried about losing my working code. Even worse, I've had
  working code that I edited and then **it didn't work anymore** and I couldn't
  remember what I changed.
* Sometimes when I am writing (and I am usually writing in [Markdown and
  $\LaTeX$!), I re-read what I wrote and realize that I should probably make
  some changes (e.g., I've changed this paragraph at least 3 times). Sometimes I
  will cut and paste paragraphs from one place to another only to realize that
  the way that I had it originally flows a lot more nicely than ... whatever
  this is right now, but the undo feature in my text editor doesn't go back far
  enough to get back to the better flowing state and I just can't reproduce it.

  ("You can [track changes in Word]!" I can hear you saying through my screen,
  and, yes, I definitely can track changes in Word, but then I would have to
  *use Word*.)
* Sometimes I am working on an experiment (or something that requires me to keep
  track of values that I'm observing), and I accidentally and unintentionally
  change a value, but I don't notice until it's too late (or I never notice
  :frowning_face:).

We're going to use version control software to help us keep track of changes
that we've made to plain text files over time (plain text includes both
documents we're writing in Markdown and $\LaTex$ **and** source code).  While
many different version control software exist, we're going to be specifically
looking at `git`, and we're going to be using some web-based software called
GitLab to help us.

::: outcomes

By the end of this week you should be able to:

* [ ] Download a file from the internet on the command-line.
* [ ] Compile and run programs of various programming languages on the command-line.
* [ ] Use version control software on your own code to keep track of changes that
  you make over time (initializing and adding changes to a repository).
* [ ] Use version control software on your own code to make changes and quickly be
  able to revert to a working state.
* [ ] Identify files that should not be version controlled and make sure they aren't
  included in a repository's history (`.gitignore`).

:::

[version control]: https://en.wikipedia.org/wiki/Version_control
[Markdown and $\LaTeX$]: ../topic01/topic-3.html
[track changes in Word]: https://support.microsoft.com/en-us/office/track-changes-in-word-197ba630-0f5f-4a8e-9a77-3712475e806a
