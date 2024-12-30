---
title: Practice Questions
author: Ikaro Costa
---

Question 1
==========

In COMP 1002, you have successfully built your personal webpage when
you learned about [Reading and Changing Permissions](../topic05/topic-4.html) of files. We are now
going to automate a few of those processes in building (or updating) your personal
webpage. For this, we are going to write a shell script to automate the conversion
from markdown to HTML and also to change the permissions of the generated HTML
file.

1. Let us convert the file from markdown to HTML. Name your script as
   `publish_webpage`. The script should take the name of the markdown file as
   parameter and convert it to HTML using `pandoc`. For example, if your
   markdown file is `index.md`, you would run it as:

   ```bash
   ./publish_webpage index.md
   ```

2. Now, we need to change the permissions of the recently generated file
   `index.html`. Recall that the permissions are:

   * `index.html`:
      * User must have read and write, but no execute permission.
      * Group must have read, but no write nor execute permissions.
      * Other must have read, but no write nor execute permissions.

Question 2
==========

Now, we improve the shell script `publish_webpage` from Question 1. 

Input Error Prevention
----------------------

Imagine that you shared your script with a friend but they did not check your
implementation.  The idea here is to prevent that your friend type an incorrect
name as the argument of `publish_webpage`. For this, before performing any
action in the script `publish_webpage`, check if the file passed on the command
line by the user actually exists. If the file do not exist, print to standard
output "File not found!" using `echo` command. Otherwise, print "File found!"
and execute the rest of the script.  If you need to recall the file operators
you can check the section on [Structures: conditional statements and
loops](../topic09/topic-4.html).

Question 3
==========

Using a glob to find all the `zip` files in a directory, write a shell script
called `unzipall` that uses a `for` loop to iterate over all the `zip` files,
then use `unzip` to extract the files from the compressed format.

Let's test the `unzipall` script. For this, we need a few `zip` files to extract.
Download the following file using the `wget` command:

<https://toolsntechniques.ca/topic09/to_extract.zip>

Extract the downloaded `to_extract.zip` file. Then, you will have five other
`zip` files. Use the script `unzipall` you have written to extract all the
compressed files. If you need help, the section on [Compiling and running
code](../topic03/topic-2.html) shows how to use `wget` and how to use `unzip` to
extract compressed `zip` files.

::: challenge

The use of glob can remove the need of loops in many actions on a shell script.
Globs are meant to make our life easier. Can you write the same `unzipall`
command but not using a `for` loop?

:::
