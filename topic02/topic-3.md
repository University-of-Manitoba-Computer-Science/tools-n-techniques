---
title: "Command line text editing"
author: Franklin Bristow
---

::: outcomes

* [X] Use a command-line text editor to open, inspect, edit, and save a file.

:::

Directories are great, they're a useful tool for organizing our lives. But we
really need to be able to actually *create* stuff on the command line. 

We've spent some time getting to know VS Code, and VS Code is an excellent text
editor and [*can* be used to edit remote files], but being able to use a
command-line text editor is useful because command-line text editors are
**always there**.

You are able to install VS Code on your own computer, but you don't always have
control over remote computers, and you (generally) don't have permissions to
install software on them. You definitely don't have permission to install
software on Aviary.

In this module we're going to start working with a command-line text editor
called [`vim`].

[`vim`]: https://en.wikipedia.org/wiki/Vim_(text_editor)
[*can* be used to edit remote files]:
https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh

Opening `vim`
=============

`vim` is a program, just like the programs that you've been running for creating
and navigating directories, so you can run it just like the other programs
you've been running so far:

::: example

You can start `vim` by typing `vim` at the "prompt" and pressing <kbd>Enter</kbd>.

::: aside

A "prompt" is what your shell prints out before it waits for you to enter
something. In our case, it's `[you@bird ~]> `.

:::

```bash
vim
```

When `vim` opens, you'll see something like this:

```
~                    VIM - Vi IMproved
~                                                          
~                     version 7.4.629
~                by Bram Moolenaar et al.
~            Modified by <bugzilla@redhat.com>
~       Vim is open source and freely distributable
~                                                          
~                Sponsor Vim development!
~     type  :help sponsor<Enter>    for information
~                                                          
~     type  :q<Enter>               to exit
~     type  :help<Enter>  or  <F1>  for on-line help
~     type  :help version7<Enter>   for version info
~                                                     
[No Name]                                0,0-1          All
```

You can quit `vim` by typing `:q` (colon, then q) and pressing <kbd>Enter</kbd>.

:::

`vim` has several "[modes]", but only two that we care about right now: normal
mode and insert mode.

When you start `vim`, you are in "normal" mode. In "normal" mode, you're
interacting with `vim` itself and you can give commands *to `vim`*, like saving
your file or exiting. In "insert" mode, you're actually able to make changes to
the file.

[modes]: https://en.wikipedia.org/wiki/Vim_(text_editor)#Modes

Editing and saving a file
=========================

Open `vim` again (if didn't close it, quit, then open it again), but this time
pass it a filename to create a new file with that name.

::: example

Create a new file with vim named `hello.md`.

```bash
vim hello.md
```

Once you're in `vim`, enter **insert mode** by typing <kbd>i</kbd> on your keyboard.
Now start typing!

Once you're finished, press <kbd>Esc</kbd> on your keyboard to get back into
**normal mode**.

Now *save* the file by "writing" the file. Similar to quitting, you can write
your file by typing `:w` (colon, then w) and pressing <kbd>Enter</kbd>.

Now you can quit `vim` and check out the file you just created.

:::::: columns
::: {.column .input width=50%}

```bash
ls
```
:::
::: {.column .output width=50%}
```
hello.md
```
:::
::::::

:::

`vim` isn't just good at making new files, you can also open existing files. You
can re-open the file that you just made by passing that same filename to `vim`
on the command line.

Cool :sunglasses:! Now you can create new text files on the command-line with
`vim`!

Copying and pasting into `vim`
==============================

You can create new text files on the command-line with `vim`, but sometimes you
also want to copy some text from one place and then paste it into `vim`, just
like you do with other programs.

You *can* paste into `vim`, but you have to tell `vim` that you're about to
paste something into it. You have to tell `vim` that you're going to paste
something into it so that `vim` knows not to do things like automatically indent
when you're editing a file with code in it.

We tell `vim` that we're going to paste something into it by "setting a flag"
called "paste".

::: example

Just before you paste something in `vim`, enter normal mode (press
<kbd>Escape</kbd> on your keyboard), then type `:set paste` and press
<kbd>Enter</kbd>.

Now re-enter insert mode (press <kbd>i</kbd> on your keyboard) and paste
whatever you wanted to paste.

Finally, enter normal mode, then type `:set nopaste` and press <kbd>Enter</kbd>.

:::

OK, but how do we paste?

<details><summary>Copying and pasting in Windows</summary>

You can copy in Windows by highlighting text, then either:

* Use menus: Edit &rarr; Copy, or
* Use keyboard shortcuts: press <kbd>Control</kbd>+<kbd>C</kbd> on your
  keyboard.

To paste text into your terminal window you can do one of two things:

* Use your mouse: Right-click, or
* Use keyboard shortcuts: press
  <kbd>Control</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd>. Notice that different from
  the normal shortcut for pasting!

</details>

<details><summary>Copying and pasting in macOS</summary>

You can copy and paste in macOS by highlighting text, then either:

* Use menus: Edit &rarr; Copy, or
* Use keyboard shortcuts: press <kbd>Command</kbd>+<kbd>C</kbd> on your
  keyboard.

To paste text into your terminal window you can do one of two things:

* Use menus: Edit &rarr; Paste, or
* Use keyboard shortcuts: press <kbd>Command</kbd>+<kbd>V</kbd> on your
  keyboard.

</details>

<details><summary>Copying and pasting in Linux</summary>

How you copy and paste may depend on the Linux distribution you're using and the
desktop environment that you're using.

Assuming that you're using Ubuntu with the default Gnome interface, you can copy
and paste text by highlighting some text, then either:

* Use menus: Edit &rarr; Copy, or
* Use your mouse: Right-click and select Copy, or
* Use keyboard shortcuts: press <kbd>Control</kbd>+<kbd>C</kbd> on your
  keyboard.

To paste text into your terminal window you can do one of two things:

* Use menus: Edit &rarr; Paste, or
* Use your mouse: Right-click and select Paste, or
* Use keyboard shortcuts: press
  <kbd>Control</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd>. Notice that different from
  the normal shortcut for pasting!


</details>

Cheatsheets
===========

Despite its minimal appearance, `vim` is a full-featured text editor that can do
everything that you might want. As you've seen, interacting with programs on the
command line is done entirely through your keyboard (you can keep clicking on
the terminal, but all you're doing is making fun clicking or tapping sounds).

When you're in normal mode, you can get `vim` to do many different things for
you, but listing out all of those different things would be painful and tedious.

You should seek out and find a "cheat sheet" for `vim` that lists a good set of
things that you can do with `vim` in normal mode. Some examples of operations
that you're going to want to do with `vim` frequently and should be included in
the cheat sheet are:

* Copying or cutting and pasting lines from one place to another (`y` to
  yank/copy, `d` to cut, `p` to paste).
* Undoing or redoing changes to a file (`u` to undo,
  <kbd>Control</kbd>+<kbd>R</kbd> to redo).
* Moving around on lines or around the file (`G` to go to the bottom of the
  file, `gg` to move to the top).
* Doing the same thing multiple times (cutting the next three lines `d3↓`).

Other editors
=============

`vim` is not the only text editor, and you're not required to use `vim` for this
course (or any course, really). You're welcome to try out and use other text
editors, like `nano`, `pico`, or `emacs`.
