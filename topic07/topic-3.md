---
title: Debugging strategies
author: Franklin Bristow
---


Debugging strategies
====================

Pencil-and-paper debugging
--------------------------

Pencil-and-paper debugging is the most primitive form of debugging and uses the
simplest tools: a pencil (or pen) and a piece (or two) of paper.

![I don't advocate for chewing on your pencil even if debugging is stressful. ([Pixabay
License](https://pixabay.com/photos/pencil-notebook-crumpled-paper-1891732/))](pencil.jpg)

Here's the strategy:

1. Find where your program starts executing like the `main` method or function
   or the first line of code in the file.
2. If there are any "global" variables (`static` or file-scope variables), write
   down those variable names and their values on the top of the page or a corner
   of the page that you mark as "global".
3. Write on your piece of paper any variables that are you know about that are
   in scope when the function starts like `String[] args` or `int argc` and
   `char **argv`.
4. "Run" the first line of code in your head. If the value of the variables that
   you have in scope has changed, cross out or erase the old value and write
   down the new value.
    a. If the line of code is a function or method call, draw a line under your
       currently scoped variables, move your finger to the function or method
       and start again at (2).
    b. When the function or method `return`s, cross off or erase all currently
       in-scope variables.
5. Move to the next line of code and repeat (3) until the program is "done" or
   until you uncover the incorrect flow or incorrect state of your program.

Yes, this is tedious. Painfully tedious.

No, this doesn't scale to thousands or millions of lines of code (you're not
writing thousands or millions of lines of code yet). 

No, this doesn't scale to working with even kilobytes of data (you *might* be
working with kilobytes of data, maybe).

Despite the tedium and the lack of ability to scale, this is a good way to debug
your code because it forces you to evaluate and trace the flow of your program.
This strategy makes you [become the computer].

[become the computer]: https://en.wikipedia.org/wiki/Computer#Etymology

Log-based debugging
-------------------

::: outcomes

* [X] Use log-based debugging to identify a problem with code.

:::

Pencil-and-paper debugging is a tedious but effective strategy for finding out
where the flow of your program goes wrong, or what values your variables have
when your program crashes.

But it's tedious. Painfully tedious.

Another strategy for debugging your code that's primitive and *usually*
effective is log- or print-based debugging. This strategy uses tools that are
entirely digital: The functions or methods you call to print output
(`System.out.println()`, `print()`, `console.log`, `printf()`).

The strategy is simple, but where you start depends on the kinds of error
messages your programming language produces:

* Some programming languages like Java or Python produce meaningful error
  messages that tell you specifically which line of code the program crashed on
  and what the error was when the crash happened.
* Some programming language do not produce meaningful errors. Like C, I'm
  specifically looking at you, C. We're not bitter about C at all.

### Languages with meaningful error messages

If your language produces meaningful error messages that include the file and
line number that your program crashed on, then that's the best place to start
adding print or log statements.

Find the line of code reported in the error message and print out the values of
variables that are in scope *just before* the crash happened, then run your
program again and hope it still crashes. Sometimes seeing that a variable you
expected to never be `null` having a value of `null` is enough to help you move
forward.

The flow of our program was partially revealed by the error message, but the
error message doesn't tell us what happened before that, just the state of the
[call stack], so we still may need to figure out how we got here. In this case,
the strategy for adding more print or log statements is to work backwards from
the site of the crash:

* If your code crashes inside a conditional statement, print out the values just
  before entering the conditional statement.
* If your code crashes inside a loop, print out the values of the variables that
  are in scope and relevant inside to loop to see how they change each
  iteration.
* If your code crashes inside a function, look back at the error message and see
  which line of code caused your program to enter that function, and add print
  messages *just before* calling the function in the first place.

Repeat this until you're able to identify where your program's flow has gone an
unexpected way or until you're able to identify when and how your variables have
their values changed to something unexpected.

[call stack]: https://en.wikipedia.org/wiki/Call_stack

### Languages without meaningful error messages

If your language does not produce meaningful error messages, then we need to
follow a strategy that resembles pencil-and-paper debugging: Start printing out
the values of variables in the place where our code starts (like the `main`
function).

If there's a line of code that contains a call to a function, you don't
necessarily have to trace the flow through that function, you may only care
that the value you get back from the function is what you expect, so adding
print statements before and after the call is enough:

```c
printf("The value right now is [%s]\n", my_string);
my_function(my_string);
printf("Now the value is [%s]\n", my_string);
```

If you can see that the value *was not* what you expected, then move your editor
to that function call and start adding similar print messages until you find a
single statement that you wrote that causes your program to flow incorrectly, or
that changes the value of a variable in a way you weren't expecting.

### General advice for log-based debugging

Here are some very general tips for log-based debugging:

* Print the **name** of the variable that you're trying to inspect. Modern
  Python has a shortcut for this:
  
  ```python
  message = "Hello"
  print(f"{hello=}")
  ```

  In other languages it's just including the name of the variable in your print
  statement:

  ```java
  int variable = 42;
  System.out.printf("variable = %d\n", variable);
  ```
* Print the **line number** that the print statement is on. You can print the
  line number in C with a magic variable:

  ```c
  printf("The current line number is %d\n", __LINE__);
  ```
* When working with strings, **wrap the value** with symbols you know won't or
  shouldn't be in the string so that you can see (for example) leading or
  trailing space characters:

  ```java
  final String message = "   spaces\t!!!\r\n";
  System.out.println("message is [" + message + "]");
  ```

  This is particularly helpful in C when you're working with strings.
