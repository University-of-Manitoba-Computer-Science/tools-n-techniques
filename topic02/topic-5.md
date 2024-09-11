---
title: "Transferring files"
author: Franklin Bristow
---

::: outcomes

* [X] Transfer files between your computer and a remote computer.

:::

Doing your work on a remote computer using a command-line text editor like `vim`
is *fine*, but it's not exactly the most comfortable environment. Nothing is
going to feel the same as working directly on your own computer.

Transferring files between your computer and a remote computer (to the remote
computer and from the remote computer) is fairly straightforward. We'll look at
two different ways you can do it: using a graphical user interface (a GUI) and
using command-line tools.

Using a GUI
===========

You're going to need to install a new program on your computer to get a GUI to
transfer files between your computer and a remote computer. The program you use
depends on the operating system that you're using. The following are
*recommendations* for software that you can use, but there are many different
programs you can use to transfer files between computers.

::: tip

You only need to install software (in Windows and macOS) if you are planning to
use a GUI. You don't need to install anything at all if you are planning on
[Using the command line] to transfer files.

:::

<details><summary>GUIs for Windows</summary>
[MobaXterm] is a full software suite for working with remote computers on
Windows, including a(nother) terminal emulator.

::: aside

If you're planning on using MobaXterm, you should download the "Installer
edition" &mdash; this has a `.zip` file that contains a `.msi` file, and you
can install the `.msi` file in [the same way that you did with Pandoc].

:::

After you've installed MobaXterm, launch it. You can then connect to a remote
computer by clicking the "Start local terminal" button that's right in the
middle of the main window, then connecting *the same way you did in your other
terminal application*, i.e., 

```bash
ssh you@name.remote.ca
```

Once you're connected, MobaXterm will automatically display files and folders
that you have on this remote system on the left side of the window.

You can transfer files from Aviary to your computer by right-clicking on the
thing you want to copy to your computer and selecting "Download...". You will
then be asked where you want to put the files, and you can select the folder you
want to put them into.

You can transfer files from your computer to Aviary by opening Windows Explorer,
clicking on the file you want to copy to Aviary, and dragging it to the folder
display on the left of MobaXterm. MobaXterm will then start transferring the
file or folder that you've asked it to copy to the remote computer.

[MobaXterm]: https://mobaxterm.mobatek.net
[the same way you did with Pandoc]: ../topic01/topic-2.html
</details>

<details><summary>GUIs for macOS</summary>
[Cyberduck] is a tool designed specifically for transferring files between
computers. Installing Cyberduck is [the same process as installing VS Code]
(download the `.zip` file, copy the app into your Applications directory).

Once you've installed Cyberduck, create a new "SFTP" connection by clicking on
the + button on the bottom left side of the window. In the list of options at
the top, choose "SFTP (SSH File Transfer Protocol)". The **Server** is the name
and location (address) of the remote computer you want to connect to. Your
**username** and **password** are the same ones you used to connect remotely
with `ssh`. When you've finished entering that information, you can close this
window, then double-click on the entry that was created in the main Cyberduck
window.

Once you do that, you should see the files and folders that are on the remote
computer :tada:! You can interact with this window the same way you do with your
file explorer (e.g., drag files and folders to and from this window to transfer
them).

[Cyberduck]: https://cyberduck.io/
[the same process as installing VS Code]: ../topic01/topic-2.html
</details>

<details><summary>GUIs for Linux</summary>
Depending on the distribution that you have installed, you may just be able to
use your file explorer to connect to a remote computer with a GUI.

Open your file explorer program, and on the left side of the window look for an
entry that says something like "Other locations". You may see an option to
"Connect to a server" at the bottom of the window.

Another alternative is that you may be able to enter an address directly into
the address field.

If you see that option, you can enter the name and location of the remote
computer you want to connect to, but you need to tell the file explorer software
which "protocol" to use.

If you want to connect to aviary, you should enter
`ssh://aviary.cs.umanitoba.ca` and enter your **username** and **password** when
prompted.

If you've connected, then you'll see the files and folders that you saw in your
terminal in your regular file explorer window :tada:! You can interact with this
window in the same way you do with other file explorer windows (e.g., drag files
and folders to and from this window to transfer them).

</details>

Using the command line
======================

Transferring files on the command line is the same regardless of which operating
system you have on your computer.

[Open your terminal], then navigate to the directory that *contains* the file or
directory that you want to transfer from your computer to the remote computer.

::: aside

Navigating directories on Windows, macOS, and Linux uses *mostly* the same
commands: `cd` to **c**hange **d**irectories, `cd ..` to *go back*. The only
notable difference that we care about right now is that Windows doesn't have the
`~` special directory.

When you're navigating folders **on your own computer** (i.e., you're not
connected to something like Aviary with `ssh`), you can also take a shortcut to
avoid typing out very long folder paths: Open your terminal, type `cd ` (that's
`cd ` with a single space after it), then open your visual file explorer. Find
the folder that you want to navigate *to*, click the folder, then drag it to
your terminal window and drop it. The path to that folder *should* show up in
your terminal and then you can press <kbd>Enter</kbd> in your terminal to get
there quickly.

:::

Once you've navigated to that directory, we can use the `scp` program (secure
copy) to transfer files from our computer to the remote computer.

When we're copying files or folders with `scp`, we need to tell `scp` what we
want to copy (the **source**) and where we want to copy it to (the
**destination**).

Just like [when using SSH], any time we want to use a remote computer as a source
or a destination, we need to provide `scp` with our username and the address of
the remote computer. But since we're trying to *send something*, we also need to
tell `scp` where we want to put the file (a **destination** on the remote
computer).

[Open your terminal]: ../topic01/topic-2.html#verifying-that-pandoc-is-installed
[when using SSH]: ../topic02/topic-1.html#connect-to-a-remote-computer

Copying single files
--------------------

::: example

```bash
scp source-file.md you@remote.name.ca:~/folder
```

* `source-file.md` is the name of the file that you want to copy to the remote
  computer. Replace this with the name of the file that you want to copy.
* `you` is where you put your **username**. Replace `you` with *your* username.
* `name.remote.ca` is where you put the **address** of the remote computer.
  Replace `name.remote.ca` with the address that you want to send this file to.
* `:~/folder`, the colon (`:`) separates the address from the destination on the remote
  computer, and the tilde (`~/folder`) is the name of the folder on the remote
  destination. Remember that `~` is a special name for a directory that is your
  user directory, and in this case `folder` would be the name of a folder *in*
  your user directory.
  
  If you want to transfer the file directly to your user directory, you can
  completely leave out everything *after* the colon (`:`). For example, the
  command 

  ```bash
  scp source-file.md you@remote.name.ca:
  ```

  copies the file into your user directory on the remote computer.

If I want to send a file named `hello.md` from my Desktop folder on my computer
to `aviary.cs.umanitoba.ca`, then I would run:

```bash
cd Desktop
scp hello.md fbristow@aviary.cs.umanitoba.ca:
```

Similar to `ssh`, you will be prompted to enter your password, but you will get
no feedback as you type in your password.

:::

If you want to copy a file *from* a remote computer, you can also use `scp`, but
you reverse the order: the file on the remote computer comes first (the source)
and a place on our own computer comes second (the destination).

::: example

If I want to copy `hello.md` on Aviary back from the remote computer to my
current directory (`.`), I might do something like:

```bash
scp fbristow@aviary.cs.umanitoba.ca:hello.md .
```

:::

Copying directories
-------------------

We're not limited to copying individual files between computers. In fact, that
would get really tedious if we had many files we wanted to copy, or entire
folder structures!

Thankfully, we can copy entire directories using `scp` by passing an additional
argument or flag to `scp` to tell it to copy things *recursively*.

::: example

To copy a directory either to or from a remote computer, we include `-r` after
the `scp` command to tell it to copy recursively.

```bash
scp -r my-project you@remote.name.ca:
```

* `my-project` is the name of a complete **folder** that you want to copy.
* The destination part is the same as in copying a file.

Similarly, to copy *from* the remote computer we put the remote computer
location first.

```bash
scp -r you@remote.name.ca:my-project .
```

* The source part asks to copy the folder `my-project` that's in your user
  directory.
* The destination part is the same as in copying a file.

:::
