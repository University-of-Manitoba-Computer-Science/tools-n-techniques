---
title: Practice Questions
author: Alex Kitt
---
%%  %%
Practice Questions
==================

Question 1
----------
Match the symbols with what they do:

- 1. `>`
- 2. `<`
- 3. `>>`
- 4. `|`
- 5. `2>`

- a. Pipe standard output from one program to another program's standard input
- b. Redirect standard error output (in some shells)
- c. Redirect standard output to a file and overwrite it
- d. Redirect standard output to a file and append to it
- e. Redirect standard input to be from a file

Question 2
----------

What is stored in `file.txt` after the following commands are run? Think about
what each command does, and think back to [Fortnight 6 of COMP 1002] to figure out
how you'd learn more about each. You may need to log on to Aviary to see the
contents of `/usr/share/dict/words`.

```shell
echo "hello " > file.txt
head -10 /usr/share/dict/words | grep 's$' | wc -l >> file.txt
```

[Fortnight 6 of COMP 1002]:
https://university-of-manitoba-computer-science.github.io/tools-n-techniques/topic06/topic-2.html
