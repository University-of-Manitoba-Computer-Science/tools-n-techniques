---
title: Summary
author: Franklin Bristow
---

At this point you should be able to create shell scripts to help you when you
run into repetitive tasks on the command line.

Even though shell scripting languages are complete programming languages, you 
should also take the time to evaluate whether or not making a shell script is 
the right tool :hammer_and_wrench: for the job:

* Shell scripts can help quickly apply a sequence of operations to files.
* Shell scripts *can* operate on strings, but it's pretty painful!
* Shell scripts *usually **can't*** do basic math (you have to use a separate
  calculator program, like `bc`).
* Shell scripting languages don't usually or trivially allow you to build
  complex composite data structures and objects (no classes), so building up
  abstractions can be tricky (if possible at all).
* Shell scripting languages don't usually (or ever) have the kind of supporting
  tools that other programming languages have (no debuggers, no libraries, no
  specific IDEs, no ...).

Shell scripts are great for quickly finding files and running programs on those
files, other programming languages are *usually* going to be better for
actually doing stuff *to* the files.

Further reading
===============

Just like programming (and anything, really), shell scripting goes way beyond 
what you've been introduced to here. You've got a good start, but as you keep
working with shell scripting, you'll find yourself running into situations where
you need to get some more help.

* You can read the manual page for your shell to learn more about its scripting
  language (e.g., `man bash` or `man tcsh`).
    * Sections of interest in the manual page for `bash` include the
      `CONDITIONAL EXPRESSIONS` section and the `Compound Commands` subsection.
* Joshua Levy's "[The Art of Command Line]" is a very good resource that's been
  translated into many languages. It's a good reference to keep in your
  bookmarks.
* [ShellCheck] is a tool for identifying and then helping you fix possible bugs
  in your shell scripts.
* The [Advanced Bash-Scripting Guide] is a comprehensive guide for shell
  scripting with Bash.

[The Art of Command Line]: https://github.com/jlevy/the-art-of-command-line
[ShellCheck]: https://www.shellcheck.net/
[Advanced Bash-Scripting Guide]: https://tldp.org/LDP/abs/html/
