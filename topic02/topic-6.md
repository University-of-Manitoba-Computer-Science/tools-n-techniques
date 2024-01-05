---
title: "`handin`"
author: Franklin Bristow
---

`handin`
========

::: outcomes

* [X] Use the `handin` command in the U of M CS UNIX environment.

:::

Many courses require you to submit your work to assignment folders on [UM
Learn].

Some computer science courses will require you to submit your work using a tool
called `handin` that can be run on any computer managed by the Department of
Computer Science at the U of M, for example, all computers in Aviary. You're
only required to use `handin` if your course instructor tells you to use
`handin`.

::: checklist

Handing in work with `handin` is straightforward and you need to know a few
things:

1. [ ] The **course number** that you're turning in the work for.
2. [ ] The **name of the assignment or work** that you're turning in.
3. [ ] The **folder containing the work you want to hand in**. 

:::

The course number is always the numeric part of the course name in `COMP`
courses (e.g., COMP 1010 is `1010`).

The name of the assignment or work you're turning in is something that your
instructor sets up and will tell you, but is commonly `aX` for assignments,
where $X$ is the assignment number (e.g., `a1`).

The folder containing your work is something you made with `mkdir` or by copying
your work to the remote computer.

To start, open your terminal, then connect to Aviary. Once you're connected to a
bird machine in Aviary, find the directory that you want to submit and use the
`handin` command to turn in your work.

::: example

I want to turn in my COMP 2150 assignment. My instructor has told me that the
name of the assignment for `handin` is `assignment1`. I have put my work into a
folder named `comp2150-a1`. To hand in my work, I would run `handin`:

```bash
handin 2150 assignment1 comp2150-a1
```

When I run this, `handin` provides me with a report telling me when the work was
submitted:

```
handin: Time Stamp: Thu Jul  7 15:16:44 2022
Submitter: fbristow@cormorant.cs.umanitoba.ca
Total bytes copied to handin file was: 121
Handin was successful.
```

:::

[UM Learn]: https://umlearn.ca
