---
title: What even is debugging?
author: Franklin Bristow
---

What even is debugging?
=======================

::: outcomes

* [X] Describe what debugging allows you to observe about a running program.

:::

Everyone's code doesn't work sometimes. Sometimes your code crashes with
messages that are sort of helpful like Java stack traces:

```
Exception in thread "main" java.lang.NullPointerException: Cannot invoke "String.length()" because "<local1>" is null
        at JCrash.main(JCrash.java:7)
```

Sometimes your code crashes with messages that aren't helpful at all:

```
Segmentation fault
```

Regardless of the message that's printed out, our job is now to figure out *why*
that error message is being printed out and then *change the code* so that that
message isn't printed anymore. Also hopefully to get the program we're writing
to accomplish it's task.

Debugging is the process of systematically trying to figure out what's wrong
with our code; maybe we've made a mistake in:

* The literal sequence of statements or order of operations in our code,
* The assumptions we've made about the kinds of values that we're getting as
  input, or about the kinds of values our variables can have while our code is
  running,
* Maybe our internal mental model of our code doesn't match what our code
  actually does.

Two different things can help us better understand our program and our problem:

1. **The flow of our program**: The way that our program runs; how it gets from
   one line of code to another line of code. 
2. **The state of our program**: The values that our variables have as the
   program run and how those values change, and

The flow of our program
-----------------------

In debugging, one goal is to figure out how our program got to the place in the
code where it crashed in the first place.

One thing we know about our programs regardless of the programming language
we're using is where our program starts:

* In languages like Java and C, the name of the method or function that our
  program starts in is `main`.
* In languages like Python or JavaScript, our program literally starts running
  from the first line in the file.

Figuring out how our program gets to the line where the code crashes or stops
working correctly was straightforward when our programs were very simple
programs that were entirely within `main` and had no conditional statements or
loops: we could just read our program one line at a time and pretty quickly
figure out what happened.

With conditional statements, loops, methods, and data structures like arrays or
lists, we still want to be able to figure out how we got into a particular state
by making observations about how our program proceeds through our program:

* Does our program run the line(s) of code within the conditional statement, or
  does it skip over them?
* How many times does our program run the body of the loop, if it any at all?
* How did our program even get *into* this specific method?
* How many times does our method or function recurse on itself?

The state of our program
------------------------

Another goal in debugging is to figure out what values our variables have, and
how their values change as the program flows through execution.

We (almost) always know the values our variables have when they're first
declared:

* In languages like Java, you're not allowed to use a variable in an expression
  or statement before it's been assigned a value (even `null`).

  ```java
  String message;
  System.out.println("The message is " + message); // compile time error
  ```
* In languages like Python, you can't declare a variable without giving it a
  value in the first place (declaration and initialization are a single
  statement in Python).

  ```python
  my_variable # this isn't a statement in Python!
  print(f"The message is {message}") # this is a run time error
  ```
* In languages like C, ... well, in languages like C you can declare a variable
  and use it without giving it a value. C can be bad and it should feel bad.

  ```c
  int value;
  printf("The value is %d\n", value); 
  // we can't predict what this will print
  // your compiler will warn you, though (probably)
  ```

We can figure out what values our code assigns to variables using a pencil and
paper, similar to stepping through our code mentally, and that very quickly
becomes tedious.

Tedium aside, we still want to figure out what values our variables have as the
program is running:

* What value does a variable have that's being used in a Boolean expression for
  a conditional statement?
* What value does a variable have as we're entering a loop? Repeating a loop
  for the first time? Repeating a loop for the $n^\text{th}$ time?
* What value does a variable have that's being passed to a method or function as
  an argument? What value does it have when we `return`?
* What value does a variable have as we're recursing into a function or method?
  How does that value change?
