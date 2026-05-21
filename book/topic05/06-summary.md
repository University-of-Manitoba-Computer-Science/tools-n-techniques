## Summary

OK, so we've actually really only looked at 3 or 4 tools and called that
"advanced shell usage"; what gives?

It turns out that there are a few different *implicit* learning outcomes that
you met by going through this exercise of learning these tools:

* You had a sense that command-line programs had "options" (like `ls -a`), but
  now you're beginning to see that almost all command-line programs have options.
* You've learned a little bit about "patterns". We got a taste of patterns when
  we looked at `.gitignore`: "I don't want files that end with `.class` to be in
  my repository, so I add the 'pattern' `*.class`".

  Patterns are something that you'll see treated formally if you take a course
  introducing automata and state machines where you'll learn about "regular
  expressions" and their corresponding abstract representation as automata (sort
  of like graphs).
* You've learned that some commands can launch *other commands* on your behalf.
  This is something that you'll actually see in two other courses implicitly and
  explicitly: implicitly a software engineering course as a "design pattern" and
  explicitly in an operating systems course as... well, the mechanical API for
  how programs launch other programs (your shell :shell: *is* a program, it's
  job is to start *other* programs).
* You've learned a little bit more about how Git works in terms of how to
  compare different text files to one another (Git uses something like `diff`
  internally).

You should now be able to:

::: outcomes

* [X] Find files on the command line by name using patterns.
    * [X] Execute commands on the files that match the pattern.
* [X] Filter lines from large text files using patterns.
* [X] Read and change permissions on files.
* [X] Compare plain text files.

:::

