---
title: Getting help
author: Franklin Bristow
---

::: outcomes

* [X] Get help about a command by running the command.
* [X] Get help about a command by reading manual pages.
* [X] Find and assess the quality of help online.

:::

We've all been here: I need to do something (something for an assignment,
something for work, something for myself) and I just don't know how. Even worse,
sometimes we don't even know what words to use to ask for help --- how would I
even know to ask for help with a tool called `grep` let alone figure out what
the name of the program is?!.

We're going to be primarily looking at getting help with command line tools, but
we're also going to take a look at how we can find and assess the quality of
help online.

Getting help by running the command
===================================

So far in this course you've been told the names of commands that you should
run, you've been told how you should run those commands, and you've been told
about some new options on the commands you knew that change how they behave.

Getting told how to do those things when we're getting started is important,
especially when we're working in an environment like the command line that isn't
inherently *discoverable*.

::: aside

Try putting yourself back in your shoes the very first time you opened your
terminal. If you hadn't been told what to do, what would you even do? Type in
"`help`", press <kbd>Enter</kbd> and hope for the best?

Well... try that.

Depending on the shell you're using, it *might* tell you some stuff, but it's,
uh, pretty cryptic or entirely not helpful:

* Your shell on Aviary (The [TENEX C shell], or `tcsh`) very unhelpfully tells
  you "You should have someone show you some things". *Thanks*.
* [Bash] (another shell) immediately tells you 

  > `These shell commands are defined internally.`

  What does that mean???
* [Fish] (yet another shell) somewhat helpfully opens your web browser (when it
  can) with readable documentation.

Condescending, cryptic, or otherwise, asking your shell for help gives you a
place to start by telling you about a bunch of commands you *could* run, even
with some examples. Some of the commands have good names with an obvious
meaning, others have names you recognize but don't do what you think (I'm
looking at you, `kill`), and others have inexplicable names like `compopt` or
`stty`.

[TENEX C shell]: https://en.wikipedia.org/wiki/Tcsh
[Bash]: https://en.wikipedia.org/wiki/Bash_(Unix_shell)
[Fish]: https://fishshell.com/

:::

One way we can ask commands to help us out a little bit is by just running them.
Let's take a look at a command we've been working with for a little while now:
`git`.

::: example

Enter the `git` command in your terminal and press <kbd>Enter</kbd>:

::: output

```
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]


These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone             Clone a repository into a new directory
   init              Create an empty Git repository or reinitialize an existing one
```
:::

When you run `git` without any arguments or options, it doesn't know what you
want it to do, and the most helpful response when a command can't do anything
without options or arguments is to print out a list of the things that you
*can* do with that command.

Try this on your own: pick one of the commands that are printed out when you run
`help` and see what it does when you don't pass it any arguments or options.

::: aside

You might pick a command that just doesn't seem to do anything (like `cat`).
When you're in a state where a command doesn't seem to be doing anything, you
can stop that program from running by pressing <kbd>Control</kbd>+<kbd>C</kbd>
on your keyboard.

:::

:::

Some commands just do what they're supposed to do what we run them, like `ls`:

::: example

Enter the `ls` command in your terminal and press <kbd>Enter</kbd>:

::: output

```
bin Mail hello comp-1002
```

:::

We knew about that!

::: aside

Why is `ls` different from `git`? Why does it do something without any
arguments?

`ls` *can* take arguments (not just options, but *arguments*).  `ls` can take a
file or directory name as an argument, and when you run `ls` without an
argument, the file or directory name is implicitly `.` (the current directory):

```bash
ls . # is the same as just ls
```

We use `ls` **so often in our current directory** that not typing in the extra
<kbd>Space</kbd> then <kbd>.</kbd> will actually save us a real amount of time
over our lifetimes (literally entire minutes!), so the current working directory
is the "default" argument to `ls`.

:::

Now add the options `-a` for "all" and `-l` for "long":

::: input

```bash
ls -al
```

:::

We knew about that, too!

Well... what else can `ls` do?

Let's try running `ls` with a new option: `--help`:

::: input

```bash
ls --help
```
:::

::: output

```
Usage: ls [OPTION]... [FILE]...                                            
List information about the FILEs (the current directory by default).       
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.  
                                                                           
Mandatory arguments to long options are mandatory for short options too.   
  -a, --all                  do not ignore entries starting with .         
  -A, --almost-all           do not list implied . and ..                  
      --author               with -l, print the author of each file        
```

:::

OK, cool! Overwhelming! But *cool*!

We can see some of the options that we've been told about with an explanation of
what they do, so:

```
-a --all            do not ignore entries starting with .
```

Remember: files with names starting with a period `.` are hidden when we just
used `ls` by itself.

Look through the options that are listed in the output from `ls --help` and find
some options that could be helpful. One I'll suggest you look at is the
`--human-readable` option: when `ls` prints out file sizes by default in `ls
-l`, it's printing out the file size in *bytes*. The `--human-readable` option
tells `ls` to print out file sizes using a more appropriate unit (like using MB
instead of printing out millions of bytes).

:::

We've seen several commands that run without requiring us to pass any options or
arguments (file names) like `ls` and `find`, and some that require us to pass
either options or "subcommands" like `git`.

One program we saw previously is `find`. Try running `find` with a `--help`
option right now, I'll wait.

...

The output here isn't *not* helpful. But it's... not exactly super helpful,
either. Let's move on to finding a little bit better help for `find`.

Getting help by reading manual pages
====================================

Getting help from the command itself is useful, but a very common place to find
additional help for programs on the command line are the "manual pages". This is
very often shortened to the "man pages" because the command that you run to get
this information is `man`.

::: aside

Documentation. API docs. Comments. What's the difference between all of these
things? It's all information ([it's information all the way down]).

Comments
: What you write to other people (including future you) that describe what your
  code does, explaining or justifying choices you're making in design, or
  apologizing for the terrible state of your code.
: Comments are embedded within source code, but aren't source code (you don't
  run comments).

API documentation
: What you write to other people (including future you) that describe how to use
  your *interface* in code; how someone should call your function or method,
  what your function or method expects as input, and what it will provide as
  output.
: Usually initially written within source code as specially formatted comments
  in special places (above functions or methods, using special syntax like
  `@param`).
: Can be turned into web pages (or other documents) using special tools (like
  `javadoc`). This is usually how you read API documentation.

Documentation
: What you write to other people (including future you) the describe how to use
  your program; how someone should run your program, the options they can pass
  to it to change behaviour, the arguments they should pass as file names.
: Usually written *separately* from source code, in a file like `README.md`,
  with no required format.
: *Can* be formatted to live in special system places like manual pages.

Comments, API documentation, and more broadly "documentation" are all related to
each other, telling people about code and programs.

[it's information all the way down]:
https://en.wikipedia.org/wiki/Turtles_all_the_way_down

:::

The `--help` option on `find` was... fine. Let's take a look at the manual page
for `find`.

::: example

Open the manual page for `find`:

```bash
man find
```

This opens documentation for `find` that is **comprehensive**.

The manual page opens in something called a "pager". You can use your regular
navigation keys (<kbd>&larr;</kbd>, <kbd>&uarr;</kbd>, <kbd>&darr;</kbd>, or
<kbd>&rarr;</kbd>), you can press the <kbd>Space</kbd> key to move forward
one page at a time, or you can use the <kbd>Pg Up</kbd> or <kbd>Pg Dn</kbd> keys
if your keyboard has them. You can quit the pager by pressing <kbd>q</kbd> on
your keyboard.

:::

Almost every command you can run on the command line has a comprehensive manual
page that describes all the options and arguments you can pass to the program.
Some of the manual pages also give examples about how to run the program.

Let's step through the manual page for `find` and take a look at the general
structure of a manual page.

::: example

If you quit the pager, open up the manual page for `find` again.

Here's the first line of the manual page:

```
FIND(1)                  General Commands Manual                 FIND(1)
```

This tells us the name of the command that we're looking at (`FIND`) and that
it's in section 1 of the manual pages.

::: aside

The manual pages have several sections:

1. Command line programs that you will use.
2. An API for asking the operating system to do stuff (in C; e.g., you can do
   something like `man 2 read` to learn about how to read files at a low level).
3. An API for "standard library" calls (in C, like Java JDK API; e.g., you can
   do something like `man 3 fgets` to learn about how to read files line-by-line).
4. Descriptions of special files in Linux (that represent *hardware*! e.g., you
   can do something like `man 4 random` to learn about how random numbers are
   generated on Linux).
5. Descriptions and formats for system configuration files (e.g., you can
   do something like `man 5 fstab` to learn about how hard drives are
   represented as folders/"mounted").
6. Games.
7. Meta descriptions, usually things like concepts or HOWTOs that don't fit into
   other sections (like `man 7 signal`, telling you about how running programs
   can communicate with each other).
8. System administration commands (usually only for administrative users)
9. An API for asking the Linux kernel to do stuff (in C).

You can learn more about this (and other stuff!) by looking at the manual page
for `man`, run

```bash
man man # ha ha
```

:::

Next is the `NAME` section:

```
NAME
       find - search for files in a directory hierarchy
```

This repeats the name of the command that we're asking about (`find`) and gives
us a human-readable description of what the command does.

Next is the `SYNOPSIS` section:

```
SYNOPSIS
       find  [-H] [-L] [-P] [-D debugopts] [-Olevel] [starting-point...]
       [expression]
```

This describes to us how we can run the command. Anything that's between square
brackets (`[]`) means that this thing is *optional*. Remember that we could run
`find` without any arguments, so everything is optional.

For `find` specifically, the `[starting-point...]` argument is a list of
directories (hence the `...`), we've always specified `.`, but you can put any
directory in here for `find` to start searching from. The `[expression]` part is
the place where we've been putting our name pattern (`-name "*ananas.md"`), but
can contain a number of other specifiers and tools for filtering files, not
just by name!

After the `SYNOPSIS` is the `DESRIPTION`. This is similar to the brief
description in the `NAME` section, but is more detailed:

```
DESCRIPTION
       This manual page documents the GNU version  of  find.   GNU  find
       searches  the  directory tree rooted at each given starting-point
       by evaluating the given expression from left to right,  according
       to  the  rules  of  precedence (see section OPERATORS), until the
       outcome is known (the left hand side is false for and operations,
       true for or), at which point find moves on to the next file name.
       If no starting-point is specified, `.' is assumed.
```

Next is the `OPTIONS` section. This is a comprehensive listing of all options
that the program accepts, and a description of what all of those options mean
and do to the behaviour of the program. Most of these won't make any sense
(what's a "symbolic link" and why does it seem to be so important???), and
that's OK.

The part of this manual page that I consider to be the most important is the
`EXPRESSION` section:

```
EXPRESSION
       The part of the command line after the list of starting points is
       the expression.  This is a kind of query specification describing
       how we match files and what  we  do  with  the  files  that  were
       matched.
```

The `EXPRESSION` section is ***comprehensive*** (we keep using that word, but its
meaning keeps changing to be stuff that's even bigger). This section makes up
about half the contents of this manual page!

This section is also the most important because it describes how you filter
files and folders. We're not just limited to names (we can filter files that
have specific permissions with `-perm`), and we're not just limited to files (we
can specify if we're looking for directories with `-type d`).

This section is so long that it's almost hard to find the next section, so we're
going to do a little trick and we're going to search through the manual page!

Press <kbd>/</kbd> on your keyboard, then type "`EXAMPLES`" and press
<kbd>Enter</kbd>. This will search for the next appearance of the word
"`EXAMPLES`". The next appearance is *probably not* the one you're looking for,
so you can press <kbd>n</kbd> on your keyboard to get to the next one. Similar
to the other sections (`SYNOPSIS`, `DESCRIPTION`, `EXPRESSION`), the `EXAMPLES`
section starts when the word `EXAMPLES` is by itself on a line. If you go too
far, you can press <kbd>Shift</kbd>+<kbd>n</kbd> on your keyboard to go to the
previous appearance of the word you're looking for.

Not all manual pages have an `EXAMPLES` section, but the one in the `find`
manual page is great because it shows you how you can use `find` to do specific
tasks. They aren't necessarily exactly what you want to do, but they're detailed
enough that you can adapt them to what you need.

:::

The manual page for `find` is exceptionally good. I almost never need to
search for how to do something with `find` online because of how good the manual
page for `find` is.

Try looking at the manual pages for some of the other commands that you've used
(`ls`, `grep`). How do these manual pages compare to `find`?

What if I don't know the name?
------------------------------

Running the command with no arguments, with `--help`, or using the manual pages
is great when you know the name of the command that you're trying to get help
with, but what if you don't know the name of the command? Maybe you want to do
something and you don't know what command you can use to help you accomplish
that. We can actually still use the manual pages to help us with this!

::: example

The manual page command `man` has an option `-k` that we can pass to ask it to
find manual pages for us that contain keywords. This can sometimes help us find
commands.

```bash
man -k search # I'm looking for something
```

The `-k` option searches through all sections of the manual pages, and you can
see which section the match is from in the parenthesis `()` immediately after
the name of the command:

```
apropos (1)          - search the manual page names and descriptions
apt-patterns (7)     - Syntax and semantics of apt search patterns
badblocks (8)        - search a device for bad blocks
bsearch (3)          - binary search of a sorted array
bsearch (3avr)       - (unknown subject)
bzegrep (1)          - search possibly bzip2 compressed files for a regular expression
bzfgrep (1)          - search possibly bzip2 compressed files for a regular expression
bzgrep (1)           - search possibly bzip2 compressed files for a regular expression
find (1)             - search for files in a directory hierarchy
```

`apropos` is in section 1, `apt-patterns` is in section 7, ... `find` is in
section 1.

:::

Find and assess the quality of help online
==========================================

While we can find help using manual pages, not all manual pages are created
equally. Not all commands even have manual pages. When the manual page isn't
great or doesn't exist, we sometimes have to resort to finding help online.

::: warning

Unless you're given permission from your instructor, you should almost never
just copy and paste something from online without taking the time to understand
what it does.

Not only would copying and pasting something from online without previous
permission be a form of academic misconduct, depending on what you're copying
and pasting, it could also be [potentially dangerous] --- what you see in your
web browser might not actually be the same as what gets copied, then pasted.

[potentially dangerous]:
http://www.h-online.com/security/news/item/Old-tricks-are-new-again-Dangerous-copy-paste-1842898.html

:::

How to ask the question
-----------------------

The first part of finding help online is knowing what question to ask, and
sometimes that's one of the hardest parts of getting help.

Asking the right question depends heavily on context, but we're going to focus
on asking questions to get help with tasks on the command line.

Here are some suggestions that you can use for coming up with or phrasing your
question:

* State the end result of what you're trying to accomplish (I want to undo the
  last commit in my Git repository; I want to be able to change into a
  directory; "I want to" or "I want to be able to" isn't necessary).
* Add the context where you're trying to accomplish that (on the command line;
  in Linux; on Ubuntu).

Places to look
--------------

Your main starting point is a search engine ([Google], [Bing], [DuckDuckGo]).

Sometimes specific websites have search features ([GitHub], [StackOverflow]).

Sometimes the websites that you want to search through don't have very good
search features, but do have good resources ([Reddit]). When you're in this
situation, you can use regular search engines and use filters to limit your
results to a specific website.

::: example

Open your favourite search engine, and search for some resources on how to
change permissions on StackOverflow:

> remove the execute permission Linux command line site:stackoverflow.com

:::

Sometimes the combination of keywords you're using give you too many results,
but the results aren't the specific combination of words that you want. In
situations like that, you can use quotes around words or phrases that must be
included in the search results:

::: example

Again, open your favourite search engine, and search for some resources on how
to find directories based on when they were modified with `find`:

> find directory by name "modified time" linux

:::

[Reddit]: https://reddit.com
[StackOverflow]: https://stackoverflow.com
[GitHub]: https://github.com
[Google]: https://google.com
[Bing]: https://bing.com
[DuckDuckGo]: https://duckduckgo.com

Assessing what you find
-----------------------

Once you've got your question asked, you're gonna find a bunch of stuff.
Sometimes the resources you find are high quality (blog posts by real people who
know their stuff), sometimes it's good (user-generated content on websites like
StackOverflow), sometimes it's bad (user-generated content on websites like
StackOverflow). Sometimes it's all of the above. Sometimes you're going to find
things like the entire contents of manual pages copied and pasted onto a random
"blog" that does little more than show ads.

### General approach

We of course can't give comprehensive advice for every specific situation, but
we can give some general advice.

1. **Read it!**

   You've found a resource that has an obvious code fragment or snippet in it,
   and it looks like it *could* solve the problem that you have right now. It's
   really tempting to copy and paste that fragment right now, but there's
   probably also some text around that fragment. Read it!
2. **Can you understand it? Can you explain it in your own words?**

   Now that you've read it, were you able to understand both what the code
   contains, but also everything else around it? One way to show yourself that
   you understand what it's saying or what the fragment or snippet does is by
   explaining it to yourself in your own words.
3. **Does it work?**

   You've read it. You understand it (or at least you think you do), now let's
   see if it actually works.

   One thing to keep in mind here is that you want to make sure it works in the
   specific context that you're trying to use it in.
4. **Where else can you get help?**

   OK, so it didn't work. Or maybe it does work, but you can't explain it to
   yourself, and can't realistically write it yourself. Where else can you go to
   get help?

   Depending on the situation, you can go to a few different places:

   * If you're working on an assignment, you can go to your instructor or TA,
     either by visiting during their office hours or sending an e-mail, or
     communicating with them using the ways described in your course syllabus.
   * If you're working on your own project, ask in places like StackOverflow,
     student groups like [CSSA], [.devClub] or [WICS], or, if you have specific
     questions about a specific project or library that you're using, ask the
     developer in places like GitHub.
   * If you're working in a workplace, ask your peers or your supervisor.

[CSSA]: https://umanitobacssa.ca/
[.devClub]: https://devclub.ca/
[WICS]: https://umwics.vercel.app/
