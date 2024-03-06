---
title: Debugging shell scripts
author: Franklin Bristow
---

Debugging shell scripts
=======================

::: outcomes

* [X] Apply strategies to debug shell scripts.

:::

If you haven't already figured it out, shell scripting isn't... it isn't a great
language for programming. I'm not judging shell scripts, but. No. Yes, I am
judging shell scripts. And my judgment is that they are perfectly fine the way
they are, but they are not a good general purpose programming language.

Shell scripting languages do not come with an IDE and they do not come with a
debugger. You can, however, do *something* to debug shell scripts.

Log-based debugging
-------------------

Re-read (or read) [log-based debugging].

You can print values of variables in shell scripts using the commands `echo` or
`printf`.

::: example

We can print out the current value of a variable in a string with `echo`:

```bash
NAME="Franklin"
echo "Hi, $NAME"
```

You can also print out values with `printf`:

```bash
PI=3 # close enough
printf "%d\n" $PI
```

:::

`echo` is pretty straightforward to use; `printf` can be as complex as
`printf(3)` in the C programming language, but you can refer to the manual pages
to find out more about how to use `printf` by running `man 1 printf`.

[log-based debugging]: https://university-of-manitoba-computer-science.github.io/tools-n-techniques/topic07/topic-3.html#log-based-debugging

Changing Bash Behaviour
-----------------------

Bash is not a good general purpose programming language. For many reasons. But
two reasons that are relevant right now are:

1. By default, Bash does not stop running a script if a variable that's being 
   used does not have a value or has not been initialized.
2. By default, Bash does not stop running a script if a program in the script
   exits with an error.

In other words, if Bash runs into something that could be a possible error, it
just keeps going without stopping.

::: example

If you run the following script, it will just run to completion without telling
you that a variable hasn't been initialized or given any value:

```bash
#!/usr/bin/env bash
echo "Your name is $YOUR_NAME"
echo "Hi $YOUR_NAME!"
```

Try creating this script and running it (don't forget to [make it executable]!).

Go ahead. I'll wait.

...

...

...

Nice.

[make it executable]: https://university-of-manitoba-computer-science.github.io/tools-n-techniques/topic05/topic-4.html

:::

You can change how Bash behaves in these two (obviously!) error situations by
changing Bash's behaviour using [the `set` command].

The two options we're going to change are the ones that correspond to `-e` and
`-x`. The `-e` option says "exit on any error", and the `-x` option says to 
print a "trace" of commands (it prints out the commands that have run, this
helps give you a sense of the flow of the script).

[the `set` command]: https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html

::: example

For ***any*** script that you write, you should start it with:

```bash
#!/usr/bin/env bash
set -e    # exit on any error
set -x    # print out all commands that are run
```

:::

Further reading
---------------

Shell scripting isn't... it isn't a great language for general purpose
programming, but maybe that's because nobody has built up the kind of tooling we
have for debugging like in other programming languages.

Here are some links where you can read a bit more about debugging shell scripts:

* On Julia Evans' "[wizard zines]" there's a comic specifically on "[bash
  debugging]". It's short, visual, but gives some additional tips like using the
  `trap` builtin for even more debugging goodness.
* An actual Bash debugging tool exists as "[BASH Debugger]", but it's not
  usually installed anywhere by default (it's not on Aviary, for example), and
  I'm not entirely sure how it works in the sense that commands have
  side-effects outside of the language. This is something you will have to build
  and install on your own if you want to use it.
* Greg's Wiki entry on [Bash Pitfalls] explains why some of the options that
  we're listing in this book are still not exactly great ways to debug a shell
  script (but it's kinda all we've got).

[wizard zines]: https://wizardzines.com/
[bash debugging]: https://wizardzines.com/comics/bash-debugging/
[BASH Debugger]: https://bashdb.sourceforge.net/
[Bash Pitfalls]: https://mywiki.wooledge.org/BashPitfalls#set_-euo_pipefail
