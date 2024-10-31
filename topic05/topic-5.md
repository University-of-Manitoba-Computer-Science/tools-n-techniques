---
title: "Comparing plain text files"
author: Franklin Bristow
---

::: outcomes

* [X] Compare plain text files.

:::

The last thing we'll do in this topic is look at comparing plain text files to
one another. You've actually been introduced to this topic already when we
looked at the output from `git diff`: when you run `git diff` you're comparing
the files as they were in the last commit to the current state that the files
are in now!

We also sometimes want to be able to compare files directly to one another when,
for example, they aren't under version control (we don't have the files in our
repository).

For this, we're going to use a program called `diff`.

::: example

Let's get back one more time to the root of `crazy-directories`. Once you're
there, let's compare the differences between `b/5/s/bananas.md` and
`b/5/s/bAnAnAs.md`:

:::::: columns
::: {.column .input width=30%}

```bash
diff -u b/5/s/bananas.md \
        b/5/s/bAnAnAs.md
```

:::
::: {.column .output width=70%}

You should see output that looks something like this:

```
--- b/5/s/bananas.md    2022-10-04 19:34:34.327980126 -0500
+++ b/5/s/bAnAnAs.md    2022-10-04 19:34:03.496980478 -0500
@@ -1,4 +1,4 @@
-bananas
+bAnAnAs
 =======
 
-You found me! That's bananas :banana:!
+You found me! That's ... wait, what?
```
:::
::::::

`diff` is reporting to us the differences between the first file we passed and
the second file. It indicates which file lines belong to using the `-` and `+`
characters, and it's showing us how we can change the file on the left to turn
into the file on the right. The `@@ -1,4 +1,4 @@` line is cryptically telling us
that it's showing us 4 lines from the file on the left (`-`) starting at line 1,
and 4 lines from the file on the right (`+`) starting at line 1.

:::

For full clarity: the learning outcome here is "Compare plain text files", not
"interpret the output from `diff`". Being able to run `diff` on the command line
to see the differences between files is all we're looking for.
