---
title: Getting help --- Examples
author: Franklin Bristow
---

These are contrived examples, but let's step through how we might approach
getting help on the command line through getting and assessing the quality of
help online.

Example: using `find` to match multiple patterns
================================================

Last week we used `find` for a few different reasons: to help us find all files
matching a pattern, to delete those files, and to run commands on those files.

In one situation we wanted to delete both `docx` and `pdf` files from our
repositories.

Let's ignore the first step: We know that running `find` by itself will just
print out the names of all files in the current directory and below, so there's
no point trying with that.

Can `find --help` help us?

::: output

```
Usage: find [-H] [-L] [-P] [-Olevel] [-D debugopts] [path...] [expression]

default path is the current directory; default expression is -print                       
expression may consist of: operators, options, tests, and actions:
operators (decreasing precedence; -and is implicit where no others are given):            
      ( EXPR )   ! EXPR   -not EXPR   EXPR1 -a EXPR2   EXPR1 -and EXPR2                   
      EXPR1 -o EXPR2   EXPR1 -or EXPR2   EXPR1 , EXPR2                                    
positional options (always true): -daystart -follow -regextype                            

normal options (always true, specified before other expressions):                         
      -depth --help -maxdepth LEVELS -mindepth LEVELS -mount -noleaf                      
      --version -xdev -ignore_readdir_race -noignore_readdir_race                         
tests (N can be +N or -N or N): -amin N -anewer FILE -atime N -cmin N                     
      -cnewer FILE -ctime N -empty -false -fstype TYPE -gid N -group NAME                 
      -ilname PATTERN -iname PATTERN -inum N -iwholename PATTERN -iregex PATTERN          
      -links N -lname PATTERN -mmin N -mtime N -name PATTERN -newer FILE                  
      -nouser -nogroup -path PATTERN -perm [-/]MODE -regex PATTERN                        
      -readable -writable -executable        
      -wholename PATTERN -size N[bcwkMG] -true -type [bcdpflsD] -uid N                    
      -used N -user NAME -xtype [bcdpfls]      -context CONTEXT                           

actions: -delete -print0 -printf FORMAT -fprintf FILE FORMAT -print                       
      -fprint0 FILE -fprint FILE -ls -fls FILE -prune -quit                               
      -exec COMMAND ; -exec COMMAND {} + -ok COMMAND ;                                    
      -execdir COMMAND ; -execdir COMMAND {} + -okdir COMMAND ;                           
```

:::

Actually yeah, maybe. It tells us one important thing: expressions aren't just
one "`-name`" and a pattern. Expressions are kinda closely related to something
we've seen in programming: they're Boolean expressions that can have groupings
with parentheses `()`, negation with `!` or `-not`, AND-ing with `-a` or `-and`,
OR-ing with `-o` or `-or`. We want to find files that have a name matching
`.docx` or `.pdf`, so let's try:

```bash
find . -name "*.docx" -or "*.pdf"
```

... that didn't work, and the message that `find` prints out isn't exactly
helpful.

Right, let's try the manual page, then:

```bash
man find # or man 1 find
```

I think I know I want to use the `-or` option, that's literally what my question
is, so I'll search for it by typing <kbd>/</kbd>, typing `-or`, then pressing
<kbd>Enter</kbd>.

The thing that I immediately see when I do this is:

```
expr1 -or expr2
       Same as expr1 -o expr2, but not POSIX compliant.
```

This... actually maybe isn't not helpful: it's telling me that `-or` requires
*two* expressions around it. When I think back to `find . -name "*.docx"` and
the `-name "*.docx"` being the expression part of the command, it's a hint that
maybe I can have *two* `-name` expressions, one on each side of the `-or`.

Let's keep looking through the manual page. I'm going to press <kbd>n</kbd> on
my keyboard to find the next instance of `-or`. It's in the examples section.
Its hard to decipher, but it does seem helpful:

```
Given the following directory of projects and their associated  SCM  ad‐
ministrative  directories, perform an efficient search for the projects'
roots:

  $ find repo/ \
	  \( -exec test -d '{}/.svn' \; \
	  -or -exec test -d '{}/.git' \; \
	  -or -exec test -d '{}/CVS' \; \
	  \) -print -prune

Sample output:

  repo/project1/CVS
  repo/gnu/project2/.svn
  repo/gnu/project3/.svn
  repo/gnu/project3/src/.svn
  repo/project4/.git
```

This example does more than I want, but it confirms what I thought before: you
can put multiple expressions (e.g., `-name`) around `-or`. Let's try that:

```bash
find . -name "*.docx" -or -name "*.pdf"
```

It works! Or at least it doesn't give us an error. We deleted all those files
last time, so it's hard to say if it works.

Re-generate those files using what you learned last week (`-exec`), and confirm
if this command does indeed find those files.

Now let's try delete those files using the same approach:

```bash
find . -name "*.docx" -or -name "*.pdf" -delete
```

Uh, that sort of worked. Run that command again without `-delete`. Let's check
the manual page again for `-delete`. You can search for `-delete` with
<kbd>/</kbd>, but you have to press <kbd>n</kbd> multiple times to get to the
option's documentation:

```
-delete
	  Delete files; true if removal succeeded.  If the removal failed, an  er‐
	  ror  message  is  issued.   If -delete fails, find's exit status will be
	  nonzero (when it eventually exits).  Use of -delete automatically  turns
	  on the `-depth' option.

	  Warnings: Don't forget that the find command line is evaluated as an ex‐
	  pression, so putting -delete first will make find try to  delete  every‐
	  thing below the starting points you specified.  When testing a find com‐
	  mand line that you later intend to use with -delete, you should  explic‐
	  itly  specify -depth in order to avoid later surprises.  Because -delete
	  implies -depth, you cannot usefully use -prune and -delete together.
```

This is a lot, but it does tell us (implicitly) why this didn't work: `the find
command line is evaluated as an expression`. This tells me that `find` is only
applying `-delete` to the right side of `-or`.

Wow. This is really taking a long time. I'm going to give up with the manual
page (<mark>Note</mark>: We could actually piece together what we need with the
parts of the manual pages we've seen already, but it's not immediately obvious).

I'll open my search engine and search:

> find delete with multiple extensions

and my top result is on StackOverflow:

<https://stackoverflow.com/questions/20617513/using-find-command-to-delete-multiple-extensions-older-than-certaint-time>

The question is "Using find command to delete multiple extensions older than
certaint(sic) time", and the question itself has an example command that *doesn't
include `-delete`*.

Looking at the accepted answer, even if it doesn't include the `-delete` option,
gives me a hint on something new to try: parenthesis.

I remember this from basic Boolean expressions, we can combine or set precedence
for an entire expression by wrapping it with parenthesis. Maybe that means that
increasing precedence for the whole `-or` expression with `find` will have the
`-delete` apply to the entire thing. The accepted answer also copies part of the
manual page explaining why I need to put `\` in front of the parenthesis, nice!

Let's try this. Start by regenerating your `.docx` and `.pdf` files, then:

```bash
find . \( -name "*.docx" -or -name "*.pdf" \) -delete
```

:tada:, it works!

Example: find the length of an array in C
=========================================

This isn't a programming course, but let's see what we can find about finding
the length of an array in C. 

We uh, can't run a command here, so we can immediately skip both steps of
running the command by itself, and running the command with `--help`. We also
have no idea what the command is (`.length` in Java is not even a method!).

Let's try using the search feature in the manual pages:

```bash
man -k array length
```

We do actually find some *interesting* things, but they aren't helpful:

```
bsearch (3)          - binary search of a sorted array                                                                                                                              
cciss (4)            - HP Smart Array block driver                                                                                                                                  
ftruncate (2)        - truncate a file to a specified length                                                                                                                        
ftruncate64 (2)      - truncate a file to a specified length 
...
strcspn (3)          - get length of a prefix substring                                   
strlen (3)           - calculate the length of a string                                   
strnlen (3)          - determine the length of a fixed-size string                        
strspn (3)           - get length of a prefix substring
```

`strlen` or `strnlen` are actually *sort of* related to what we're looking for,
but I'm trying to calculate the length of an array of integers. Let's forget
about the manual pages.



Here are two results that I get when I search for
"find array length in C":

* <https://www.knowprogram.com/c-programming/find-length-of-array-in-c/>
* <https://stackoverflow.com/questions/37538/how-do-i-determine-the-size-of-my-array-in-c>

Let's focus on the StackOverflow post. The most upvoted answer, with more than
1500 upvotes, and the one that's marked as correct seems to have a very short
and to the point example of how you find the length of an array in C. I'm
itching to copy and paste that fragment into my code (modifying it to use the
name of my array, of course), but I can see that there's more text below. Let's
read. It seems to make sense! I even think I can explain this in my own words
(`sizeof` tells me how many bytes an entire array has, and can also tell me how
many bytes one element is, so I can divide the number of bytes in the array by
the number of bytes of one element and get the size of the array. Neat
:camera:.)

Right, let's copy it and see if it works.

```c
#include <stdio.h>
int main(void)
{
    int array[10];
    int size = sizeof(array) / sizeof(array[0]); 
    printf("array size is %d\n", size);
    return 0;
}
```

I compile and run my program (`clang array_size.c -o array_size`) and it works!
Yes!

But then I also remember that I need to do this in a function:

```c
void do_stuff(int my_array[])
{
    int size = sizeof(my_array) / sizeof(my_array[0]);
    printf("array size is %d\n", size);
}
```

I compile and run my program... and it doesn't work? If you keep reading the
StackOverflow thread, the very replies to this tell you to keep reading. When
you read the next answer, it tells you more about why this won't work, and how
you should pass arrays and their size to functions in C.

The second link is worse than the StackOverflow post because it doesn't explain
why this doesn't work at all.

This example is contrived, but is a common example of an issue you can run into
when finding help online.
