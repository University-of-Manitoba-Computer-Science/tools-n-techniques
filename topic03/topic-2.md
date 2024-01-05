---
title: "Compiling and running code"
author: Franklin Bristow
---


Compiling and running code
==========================

::: outcomes

* [X] Download a file from the internet on the command-line.
* [X] Compile and run programs of various programming languages on the
  command-line.

:::

Starting your terminal and connecting
-------------------------------------

You spent a lot of time in your terminal in "Remote connections and command-line
file management", and we're going to continue to spend a lot of time in our
terminal in this module. So: open your terminal and connect to Aviary. If you forget
how to connect to a remote computer (and it's totally OK if you do!), refer back
to the notes on connecting to a remote computer.


Downloading files from the internet
-----------------------------------

Sometimes you need to download files from the internet so that you can work with
them on the command line:

* Your course instructor has given you a template you can use to start your
  assignment.
* You're doing work on analyzing genetic data from bacteria and you need the
  data to work with.
* Your current project uses a program that reads a configuration file, but the
  configuration file is very long or hard to type out.

In all of these cases it's possible for you to open your web browser (e.g.,
Microsoft Edge, Google Chrome, Mozilla Firefox), go to the page with the URL,
click the URL, download the file to your Downloads folder, then transfer the
file to the remote computer with something like `scp`, but doing that is tedious
and time consuming (you have to download the file to your computer, then
transfer it *again* to another computer).

Thankfully it's straightforward to download files from the internet directly to
the remote computer using a command-line programs `wget`.

::: example

You can use a program like `wget` to download a file from the internet using its
address. Addresses of files on the internet look like
`https://example.com/file.txt`.

Here's a link to a `.zip` file that contains many versions of a "hello world"
program:

    https://university-of-manitoba-computer-science.github.io/tools-n-techniques/topic03/hello.zip

Here's how you would download this file to a remote computer directly on the
command line:

```bash
[you@bird ~]> wget "https://university-of-manitoba-computer-science.github.io/tools-n-techniques/topic03/hello.zip"
```

:::

Congratulations :tada:! You just downloaded a file directly to a remote
computer without downloading it to your computer first!

::: aside

You were given the address directly in this example, but how do you get
addresses from web sites in general?

* Sometimes you get told the address directly, just like in this example.
* You may find a link to the file that you want on a web page. You can copy a
  link from a web page by right clicking on the link, then selecting (something
  similar to) "Copy link".

You unfortunately can't download **all** files this way. One example of a file
that you can't trivially download directly to a remote computer would be files
that are stored on a course web page on UM Learn. More generally: files that are
on web sites that require you to log in before you can see the files.

:::

Unzipping that zip file
-----------------------

You might have noticed that the file you just downloaded to the remote computer
is a `.zip` file.

Your operating system will automatically unzip a zip file when you download it,
but we're going to need to manually unzip this file. You can use a command-line
program called `unzip` to unzip a zip file.

::: example

Find the file that you just downloaded (you put it into an appropriate location
in your folder structure, right? If not: `mv` the file you downloaded into the
right place!).

In the same directory as the zip file, you can use `unzip` and tell `unzip` the
name of the file it should unzip:

```bash
[you@bird ~]> unzip hello.zip
```

:::

Compile and run programs
------------------------

We're not going to be doing any programming in this course, but we do want to be
able to compile and run code on the command line. The file that you just
downloaded and unzipped contains implementations of "Hello, world!" in a variety
of programming languages. You're not expected to write in any of these
languages, and you're not necessarily expected to read any of these programming
languages. All we want to do is compile them (when necessary) and run them on
the command line. You will (maybe) learn these programming languages in future
courses, learn them in the workplace, or learn them on your own time.

We're going to be looking at three main types of languages:

1. Languages that require you to compile the code, then run the resulting
   program like a normal program (compiled languages).
2. Languages that require you to compile the code, then run the resulting
   program using a *different* program (compiled, but "virtual machine"-based or
   VM-based languages)
3. Languages that you give to a program to execute ("interpreted" or "scripting"
   languages).

We're going to be looking at only one or two examples of each of these
languages, but there are many more kinds of each type of language.

::: aside

We're actually going to revisit building programs later in the course when we 
look at the [command-line environment], when we actually go through the process
of building more complex applications with build systems and dependency 
management, but for now we're just going to get programs compiled and run them.

[command-line environment]: ../topic08/topic-1.html

:::

All the examples are in the folder that you unzipped called `hello`. Change into
that directory now with `cd hello`.

### Compiled languages

Change into the `compiled` directory and list its contents. This directory
contains a hello world program that's written in the [C programming language].

C programs require you to compile the code using a compiler before you can run
them. There are two C compilers that are available on Aviary: `gcc` and `clang`.
Which one you pick isn't actually that important for the purposes of this
course, they are effectively interchangeable.

::: example

You can compile a C program with `clang` (or `gcc`) by running a command:

```bash
clang hello.c -o hello # or replace `clang` with `gcc`
```

The `hello` after the `-o` is the name of the program that you just compiled.
You can run the program by saying "run the program from *this* directory":

```bash
./hello # ./ means "from this directory"
```

Hooray :tada:! You just compiled and ran your first C program.

:::

[C programming language]: https://en.wikipedia.org/wiki/C_(programming_language)

### Compiled Virtual Machine-based (VM-based) languages

Change back to the main `hello` directory, then change into the `compiled-vm`
directory.

::: aside

Remember how you can use special directory names like `..` to go back or up a
directory? You can combine this special directory name with others, and can go
back and then to a different directory in a single command.

```bash
### Doing this with 2 commands
cd ..
cd compiled-vm

### Doing this with 1 command
cd ../compiled-vm # go back, then to the `compiled-vm` directory
```

Remember to use tab completion to auto-complete these folder names!

:::

You may have already written, compiled, and run Java programs (or Processing
programs), but you probably did this entirely within an integrated development
environment (IDE) like the Processing IDE, DrJava, Eclipse, IntelliJ, ...

You can also compile and run Java programs on the command line using the `javac`
and `java` commands.

::: example

You first have to compile (with `javac`), then separately run your Java program
(with `java`) on the command line.

```bash
javac Hello.java
java Hello # the same name as the class in the .java file.
```

Hello, Java :coffee:!

:::

### Interpreted or scripting languages

The last kind of language we're going to look at are languages that are run *by*
a program. An example of this kind of language is [Python].

Change back to the main `hello`, then change into the `interpreted` directory.

You can run the Python "interpreter" (a program that will read your Python
program and then *do* the statements) on the command line using the `python`
command.

::: example

Once you're in a directory with a `.py` file, you can tell the Python
interpreter to run that program:

```bash
python hello.py
```

Hello, Python :snake:!

:::

[Python]: https://en.wikipedia.org/wiki/Python_(programming_language)
