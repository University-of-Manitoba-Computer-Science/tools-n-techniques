---
title: Arguments
author: Franklin Bristow
---

::: outcomes

* [X] Use command-line arguments in a shell script.

:::

Shell scripts that you write can accept arguments, just like programs you write
in other programming languages. In both C and Java (and Python, technically),
you can access arguments passed on the command line to your program as arrays of
strings.

Shell scripts can access command line arguments using variables, but you can
directly access arguments on the command line as numbered variables like `$1`.

::: example

Here's a small program that will print out the values passed to it as arguments
on the command line:

```bash
#!/usr/bin/env bash

echo "The first argument is $1"
echo "The second argument is $2"
echo "The third argument is $3"
echo "All arguments are $*"
```

Write this script and try running it with different arguments to see how the
output changes. Don't forget to use `chmod` to set execute permissions for your
script!

:::

A common use of arguments on the command line for shell scripts is to pass the
name of a file or directory you want to operate on.

::: example

Let's upgrade our `la` script a little bit.

Remember that `ls` can run with no arguments, and when run with no arguments
it's defaulting to printing out the contents of the directory `.`. But `ls`
*can* accept arguments. Our `la` script doesn't right now.

Change your `la` script to accept an argument and pass it to `ls`:

```bash
#!/usr/bin/env bash

ls -al "$1" # quotes in case of spaces!
```

Now run `la` again, but pass it an argument:

```bash
la .
```

Neat.

::: aside

Why "quotes in case of spaces"? Try this:

1. Remove the quotes around `$1` in your script.
2. Create a directory that has a space in its name (`mkdir "space dir"`).
3. Try running `la "space dir"`.
4. Put back the quotes around `$1` in your script.

When the shell "expands" the variable `$1`, it's replacing the value of that
variable into the command *literally*. If the variable contains spaces, it will
be replaced in the command spaces and all. In other words,

```bash
ls -al $1 # becomes:
ls -al space dir
```

If you remember *way back a long time ago*, we had to put quotes around names
with spaces when using `mkdir` because `mkdir` would turn `space dir` into two
directories. Similarly, `ls` is looking for two separate directories.

Including the quotes around `$1` makes sure that even if the variable contains
spaces, it's going to be quoted when it's passed to the command:

```bash
ls -al "$1" # becomes
ls -al "space dir"
```

:::

:::

While we've improved `la` slightly here, we've also broken it. Try running `la`
by itself with no arguments.

...

Oops. Now we need to test for the special case of no arguments being passed.
We're going to need some more tools for that: conditional statements.
