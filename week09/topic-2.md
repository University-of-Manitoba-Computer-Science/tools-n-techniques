---
title: Input and output on the command line
author: Franklin Bristow
---

Input and output on the command line
====================================

I think that we can all agree: programs generally read information from
somewhere (like a file) and print out information to somewhere (like your
terminal or a different file).

When we were first getting to know our terminals at the beginning of this course
we ran `pandoc` and we just started typing stuff in:

```bash
[you@bird ~]> pandoc
Hello, pandoc! ^D
<p>Hello, pandoc!</p>
```

We only did that once, then we quickly switched to passing file names as
arguments to `pandoc`:

```bash
pandoc my.md -o my.docx
```

But... what was going on with Pandoc when we just typed stuff in? This is
actually something you already know about (!), even if it doesn't quite look
like it: `pandoc` was reading from a "data stream" called "standard input".
That data stream, standard input, is where you (the user) type information using
your keyboard. `pandoc` was writing to a data stream called "standard output".
Standard output is where you see information printed in your terminal.

You've almost certainly used this in programs you've written before:

```java
// maybe you didn't call this "keyboard", but...
final Scanner keyboard = new Scanner(System.in);
```

In Java, `System.in` is:

* The `System` part is the [`System` class]. Really broadly, the `System` class
  has a bunch of properties, attributes, and methods that let your program
  interact with your operating system.
* The `in` part is the [`static` class member `in`], this is an instance of
  `InputStream`, and, very specifically, this instance refers to **standard
  input**.

We use code like this to get input from our keyboard, and, as far as we are
concerned right now, standard input *is* our keyboard.

You've **definitely** seen this code before:

```java
System.out.println("Hello, world!");
```

In Java, `System.out` is:

* `System` is the same `System` as above, and
* The `out` part is the [`static` class member `out`], this is an instance of an
  `OutputStream`, and, very specifically, this instance refers to **standard
  output**.

When we don't pass `pandoc` the name of a file to read from or a file name to
write to, `pandoc` defaults to reading from standard input (your keyboard) and
writing to standard output (the terminal).

This is actually pretty normal behaviour for programs: `grep`, for example,
writes to standard output by default, but it can also read from standard input
by default. Go ahead, try it:

```bash
[you@bird ~]> grep 'hello' # now type stuff in, some lines with hello, some
                           # without, what's printed?
```

You can quit `grep` by pressing <kbd>Control</kbd>+<kbd>C</kbd> or
<kbd>Control</kbd>+<kbd>D</kbd>.

So we've got two data streams: 

* Standard input (our keyboard), and
* Standard output (our terminal).

There's actually a *third* data stream called standard error. You probably
haven't written this in Java before, but:

```java
try {
    // dangerous stuff
} catch (final Exception e) {
    System.err.println("Oh no, something terrible happened!");
}
```

Standard error (`System.err`) is another output stream, and the main purpose of
standard error is for printing out errors to your terminal.

[`System` class]:
https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/System.html
[`static` class member `in`]:
https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/System.html#in
[`static` class member `out`]: 
https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/System.html#out

::: aside

We've seen standard input, standard output, and standard error in Java, but what
about some other languages we've seen or used?

This is not a programming course, and you won't be assessed on this at all, but
it's interesting to see how different programming languages all interact with
the same data streams!

Standard input, output, and error in C
--------------------------------------

Most of what you're doing with input and output in C comes from `stdio.h`:
functions like `fgets`, `printf`, `getline`, `getchar`, `scanf`, etc. Some of
these functions read and write standard input and standard output by default
(`scanf`/`getchar` and `printf` respectively). Others require you to pass a "file
pointer" that you get from `fopen` (`fgets`, `fprintf`).

`stdio.h` defines some constant file pointers that you can use to to read and
write standard input, output, and error: `stdin`, `stdout`, and `stderr`:

(Wait a minute, file pointers??? They're *files*???)

```c
#include <stdio.h>
#include <stdlib.h> // for EXIT_SUCCESS

int main(void)
{
    char h;
#define MAX_LEN 100
    char message[MAX_LEN];

    printf("Hello, world!\n"); // standard output
    fprintf(stdout, "Hello, world!\n"); // standard output

    fgets(message, MAX_LEN, stdin); // standard input
    h = getchar(); // standard input

    fprintf(stderr, "Oh no! Errors!\n"); // standard error

    return EXIT_SUCCESS;
}
```

Standard input, output, and error in Python
-------------------------------------------

There are a few different ways to get input or produce output in Python:

* The `input()` function reads standard input by default.
* The `print()` function prints to standard output by default.

Similar to C, Python's `sys` module provides three file objects that refer to
standard input, output, and error.

(***FILES????***)

```python
import sys
message = input("Please enter a message: ") # standard input

print("Hello, world!") # standard output
print("Hello, world!", file=sys.stdout) # standard output

print("Oh no! Errors!", file=sys.stderr) # standard error

data = sys.stdin.read() # standard input
sys.stdout.write(data)  # standard output
sys.stderr.write(data)  # standard error
```

Files (????!!!!?!??!?!?!)
-------------------------

OK, so yeah. They are file-like-things&trade; in various languages and
environments. Unfortunately we can't get much more into it than that in this
course. Be patient! You will learn a little bit more about this later in your
academic career when you're looking at how operating systems are implemented.

:::

Further reading
---------------

You can read a more about the concepts and history of standard input, output,
and error on [the Wikipedia article about Standard Streams].

[the Wikipedia article about Standard Streams]:
https://en.wikipedia.org/wiki/Standard_streams
