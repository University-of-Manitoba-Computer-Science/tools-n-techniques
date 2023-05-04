---
title: Command-line Debuggers
author: Franklin Bristow
---


Command-line debuggers
======================

::: outcomes

* [X] Use a command-line debugger to set breakpoints, inspect values, step
  through a running program, and make observations about a program when it
  crashes.

:::

Visual debugging tools are comfortable --- it's easy to see where we are, and
telling the debugger what to do is straightforward because we can point our
mouse and click on the places where we want to set breakpoints.

Unfortunately, though, using a visual debugger is not always possible. One
specific situation where you can't (easily) use a visual debugger is when you're
working with remote computers --- in your case (maybe) running C programs on
Aviary.

Thankfully, we can use command-line debuggers to help us debug programs on
remote computers.

We're going to be looking specifically at debugging a C program using the
`clang` compiler and the `lldb` debugger.

You may or may not know C, but we're not concerned with the program itself, more
about how we interact with a command-line debugger.

Getting started
---------------

Connect to Aviary with SSH, download and extract this package:

    https://university-of-manitoba-computer-science.github.io/tools-n-techniques/week08/hello.tar.gz

This program has a `Makefile`, so you can compile it using the `make` command.

```bash
[you@bird hello]> make
```

::: aside

Open the `Makefile` with your text editor. There's a lot going on in there, but
one important addition or difference from the way that we have compiled C
programs previously is that we've added an extra option to our compiler `-g`.
The `-g` option tells the compiler (approximately) to include the source code
for the C program *in* the compiled file so that we can see the source code when
we're debugging the program.

If you're planning to debug a C program, you must add this option to your
compile command:

```bash
clang -Wall -g myprogram.c -o myprogram
```

:::

Once you've compiled the code, run the program:

```bash
./hello
```

This C program works in exactly the same way as the Java program we looked at.

Launching the debugger
----------------------

The debugger we're going to use is `lldb`. `lldb` is a program that you run on
the command line, and the argument that you pass to it is the program that you
want to debug:

```bash
lldb ./hello
```

There's not much going on when you launch `lldb`:

```
(lldb) target create "./hello"
Current executable set to '/yourdir/hello' (x86_64).
(lldb)
```

Similar to your shell, `lldb` is patiently waiting for you to give it some
commands.

Setting breakpoints and running
-------------------------------

You can set a breakpoint in `lldb` using the `b` command. Break points can
either be set by line number or by function name. Let's set a break point to
pause running when we enter the `main` function:

```
(lldb) b main
```

This sets a break point on the first line of the `main` function in the program.

Let's start our program by running the `r` command:

```
(lldb) r
Process 4425 launched: '/yourdir/hello' (x86_64)
Process 4425 stopped
* thread #1, name = 'hello', stop reason = breakpoint 1.1
    frame #0: 0x000000000040114f hello`main at hello.c:10:5
   7    {
   8        int left, right, sum;
   9   
-> 10       printf("Let's add x+y!\n");
   11       printf("Enter the left side (x): ");
   12       scanf("%d", &left);
   13  
(lldb)
```

::: aside

You may want to run your process by passing arguments or by passing a file that
your program is supposed to read on "standard input" (more on this next week,
but if you normally run your program with something like `./prog < file.txt`,
then you're replacing standard input)).

You can pass the name of a file that should be read as standard input using an
`lldb` command `process launch -i` instead of using `r`:

```bash
process launch -i file.txt
```

If your program takes arguments on the command line (you need to pass things
like `-o output.txt` or `-i input.txt`), you can pass arguments to
the process using `process launch --`:

```bash
process launch -- -o output.txt -i input.txt
```

:::

Let's set another breakpoint on line 17, just before we call the `add` function,
then we'll "continue" to the next break point by using the `c` command again:

```
(lldb) b 17
Breakpoint 2: where = hello`main + 120 at hello.c:17:5, address = 0x00000000004011b8
(lldb) c
```

At this point, the program should be asking you to enter values for the left
side and right side, so enter some numeric values and press <kbd>Enter</kbd>.
Just after you press <kbd>Enter</kbd>, the debugger takes over again, telling
you where you are:

```
Let's add x+y!
Enter the left side (x): 12
Enter the right side (y): 20
Process 9196 stopped
* thread #1, name = 'hello', stop reason = breakpoint 2.1
    frame #0: 0x00000000004011b8 hello`main at hello.c:17:5
   14       printf("Enter the right side (y): ");
   15       scanf("%d", &right);
   16  
-> 17       printf("Thanks! Calculating...\n");
   18       sum = add( left, right );
   19       printf("The sum is %d\n", sum);
   20       printf("Thanks for letting me calculate for you!");
(lldb)
```

We don't have a variables pane, but we can see which variables are currently in
scope, their values, and their type by using the `var` command:

```
(lldb) var
(int) left = 12
(int) right = 20
(int) sum = -7664
(lldb)
```

The value you see for `sum` will almost certainly be different.

You can also inspect the value for specific variables using the `p` command for
print:

```
(lldb) p left
(int) $0 = 12
```

Stepping over
-------------

We just stepped over several lines of code using the `c` command for continue.
Continuing will let the program run until the next break point is encountered,
the program crashes, or the program ends.

We can step over one line at a time using the `n` command for next:

```
(lldb) n
Thanks! Calculating...
Process 9196 stopped
* thread #1, name = 'hello', stop reason = step over
    frame #0: 0x00000000004011cc hello`main at hello.c:18:16
   15       scanf("%d", &right);
   16  
   17       printf("Thanks! Calculating...\n");
-> 18       sum = add( left, right );
   19       printf("The sum is %d\n", sum);
   20       printf("Thanks for letting me calculate for you!");
   21  
(lldb)
```

Now line of code we were on (line 17) has been executed and the arrow is
pointing at the next line where we call `sum`.

Stepping into
-------------

Let's step into this function using the `s` command for step.

```
(lldb) s
Process 9196 stopped
* thread #1, name = 'hello', stop reason = step in
    frame #0: 0x000000000040122e hello`add(left=12, right=20) at hello.c:29:5
   26   {
   27       int sum;
   28  
-> 29       printf("\tAbout to add left to right.\n");
   30       sum = left + right;
   31       printf("\tHeading back to the caller.\n");
   32  
(lldb)
```

The variables currently in scope have changed, and you can see which variables
are currently in scope using the `var` command again.

Since we're in a function, our call stack has also changed. We can see the call
stack using the `bt` command for backtrace:

```
(lldb) bt
* thread #1, name = 'hello', stop reason = step in
  * frame #0: 0x000000000040122e hello`add(left=12, right=20) at hello.c:29:5
    frame #1: 0x00000000004011da hello`main at hello.c:18:11
    frame #2: 0x00007ffff7e09d0a libc.so.6`__libc_start_main + 234
    frame #3: 0x000000000040107a hello`_start + 42
(lldb)
```

"`frame #0`" is the stack frame that we're in right now in the `sum` function.
"`frame #1`" is the stack frame for the `main` function.

We can move around stack frames using the `up` and `down` commands:

```
(lldb) up
frame #1: 0x00000000004011da hello`main at hello.c:18:11
   15       scanf("%d", &right);
   16  
   17       printf("Thanks! Calculating...\n");
-> 18       sum = add( left, right );
   19       printf("The sum is %d\n", sum);
   20       printf("Thanks for letting me calculate for you!");
   21  
(lldb) var
(int) left = 12
(int) right = 20
(int) sum = -7664
(lldb) down
frame #0: 0x000000000040122e hello`add(left=12, right=20) at hello.c:29:5
   26   {
   27       int sum;
   28  
-> 29       printf("\tAbout to add left to right.\n");
   30       sum = left + right;
   31       printf("\tHeading back to the caller.\n");
   32  
(lldb) var
(const int) left = 12
(const int) right = 20
(int) sum = 0
(lldb)
```

Stepping out
------------

Get back to stack frame #0 using your `up` or `down` commands, your arrow should
be pointing at line 29 right now.

Step over the next two lines, enter the command `n` and press <kbd>Enter</kbd>.
You can repeat the last command you entered in `lldb` by pressing the
<kbd>Enter</kbd> key again.

Once you've stepped twice, your arrow should be pointing at line 31. Let's step
out of the function by using the `finish` command (for finish):

```
(lldb) finish
        Heading back to the caller.
Process 12236 stopped
* thread #1, name = 'hello', stop reason = step out
Return value: (int) $0 = 50

    frame #0: 0x00000000004011da hello`main at hello.c:18:9
   15       scanf("%d", &right);
   16  
   17       printf("Thanks! Calculating...\n");
-> 18       sum = add( left, right );
   19       printf("The sum is %d\n", sum);
   20       printf("Thanks for letting me calculate for you!");
   21  
(lldb)
```

Finishing
---------

At this point you can use the `c` command for continue to allow the program to
finish running then the `q` command to quit `lldb`, or you can immediately use
the `q` command to end the program without finishing.

Catching crashes
----------------

`lldb` will, by default, catch all crashes. That's not entirely true. C
programs, by default, will end when they crash, and they don't print out
friendly(-ish) error messages about why they crashed, they just crash and maybe
print out `Segmentation fault` or `Bus error`.

There's another program in the package you downloaded call `ccrash.c`.

Run `lldb` and pass it `ccrash`:

```bash
lldb ccrash
```

Now run the program with the `r` command, and enter some text when prompted:

```
(lldb) r
Process 12657 launched: '/yourdir/ccrash' (x86_64)
Please enter some input: hello, world!
Process 12657 stopped
* thread #1, name = 'ccrash', stop reason = signal SIGSEGV: invalid address (fault address: 0x0)
    frame #0: 0x0000000000401164 ccrash`main at ccrash.c:12:49
   9   
   10       get_input(my_input);
   11  
-> 12       printf("Here's the input: %d on line %d\n", *my_input, __LINE__);
   13  
   14       return EXIT_SUCCESS;
   15   }
(lldb)
```

Now you can use the same commands we've been using to inspect state: `var`, `p`,
`bt`, `up`, and `down`. You can also use the `q` command to quit. Since the
program is still technically running, `lldb` will ask if it's OK to quit, and
you can confirm by entering `Y` and pressing <kbd>Enter</kbd>.

::: aside

Why aren't we doing the same example in crashing with C as we did with Java and
`Scanner` crashing on non-number input?

Well... try it. What happens when you enter a string into `hello.c` instead of a
number?

:::

Further reading
---------------

These are the basics for using `lldb` as a command-line debugger for a C
program, and there's lots more we didn't get into. You can read more on the
[LLDB Tutorial] page.

LLDB is a good debugger for languages that have an [LLVM]-backed compiler;
languages like C and C++ are examples of that.

There are other command-line debuggers, and while they won't at all share the
same commands, they do share very similar concepts to what we've looked at with
`lldb`. Here's a short list of command-line debuggers for other languages:

* [JDB] is a command-line debugger for Java programs.
* [PDB] is a command-line debugger for Python programs.
* [`MDbg.exe`] is a command-line debugger for .NET languages like C#.

[LLVM]: https://llvm.org/
[LLDB Tutorial]: https://lldb.llvm.org/use/tutorial.html
[JDB]: https://docs.oracle.com/en/java/javase/17/docs/specs/man/jdb.html
[PDB]: https://docs.python.org/3/library/pdb.html
[`MDbg.exe`]: https://learn.microsoft.com/en-us/dotnet/framework/tools/mdbg-exe
