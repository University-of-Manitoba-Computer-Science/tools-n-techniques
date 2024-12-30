---
title: Install packages
author: Franklin Bristow
---

::: outcomes

* [X] Install packages using a package manager on the command line.
    * [X] Install packages using a GUI package manager.

:::

Now that you've got a running Linux system, you can (and should) use it with the
software that's installed.

You will eventually want or need to install other software that doesn't come
with the distribution by default. While you may need to compile some software
from source on Linux to install it, most distributions have a wide variety of
software available to be installed using something called a [package manager].

A package manager is a program that downloads, installs, and manages "packages".
A package is just another word to describe an application or a piece of software
that's going to be installed on the system.

On Ubuntu (and its [upstream] source Debian) use "Debian packages". Debian
packages are files with an extension of `.deb`. A `.deb` package is *kind of*
the same thing as a `.msi` file on Windows or a `.pkg` or `.app` on macOS.

There are two ways we're going to install and update packages in Ubuntu: on the
command-line and using a GUI.

[package manager]: https://en.wikipedia.org/wiki/Package_manager
[upstream]: https://en.wikipedia.org/wiki/Upstream_(software_development)

Administrative users (`root`)
=============================

Installing software is an administrative task, and only users that have
permissions can install software on a system. Since this is your Linux
installation, *you* are the administrative user and you can install new
software.

The main administrator account on Linux and UNIX systems (including macOS!) is
called `root`. Windows users can be administrative users, but there isn't really
a "main" administrator account name.

You may be prompted for an administrative password when managing software on
your Linux system. On Ubuntu, the password you should be entering is the same as
your user account's password.

Using the Software Center
=========================

Ubuntu has separate GUI apps for updating and installing new packages.

Updating packages with a GUI
----------------------------

[Start the program called "Software updater"] and follow the on-screen
instructions.

Make sure that your install is completely up to date by installing new packages.

[Start the program called "Software updater"]:
https://ubuntu.com/tutorials/upgrading-ubuntu-desktop#2-launch-the-software-updater

Installing new packages with a GUI
----------------------------------

You can install new software using the ["Ubuntu Software"] app.

Install Meld Merge using the Ubuntu Software app by searching for it, then
installing it.

["Ubuntu Software"]:
https://help.ubuntu.com/stable/ubuntu-help/addremove-install.html.en

On the command line
===================

Installing packages with a GUI is great, but you don't always have access to a
GUI (like when you're connecting to a remote server with SSH that doesn't even
have a GUI installed), and some packages aren't listed in the GUI app (notably
packages that contain command-line programs). You can also install packages on
the command line.

On Ubuntu (and Debian) the command line package manager is `apt`.

Updating packages on the command line
-------------------------------------

Updating packages on the command line actually consists of two separate steps:

1. Updating the lists of available packages.
2. Updating out-of-date packages.

You use `apt` to do both of these things:

```bash
sudo apt update
sudo apt upgrade
```

The first time you run a command with `sudo` you'll be asked to enter your
password. This is the password for your user account.

::: aside

What the heck is "[`sudo`]"?

When you install packages or apps using the GUI in any OS you're asked to
"elevate privileges": demonstrate that you are an administrative user for this
system by entering your password (macOS) or by ... clicking a button (Windows).

The `sudo` command is how you temporarily elevate your privileges on the command
line for the command that you want to run.

By default, the `sudo` command effectively runs the program you're trying to run
as the `root` user, meaning that the command you're going to run pretty much has
permission to read and write all files on your computer (necessary to install
files to system directories).

[`sudo`]: https://en.wikipedia.org/wiki/Sudo

::: aside

How the heck do you say "`sudo`"?

I (me, Franklin) say "Ess-You-Do", but other people say "Sue-Do". My preference
is "Ess-You" because we're "**S**witching **U**ser" and running a program. I
don't say "Sue-Do" because I don't know anybody named Sue.

:::

:::

::: warning

Running a command with `sudo` means that **it has permission to read and write
*all files on your computer***.

When you're installing packages, you can generally be confident that the
packages the package manager downloads and installs on your computer will not
modify *your* files or important system files.

When you're getting advice from strangers on the internet, though, you can't
always be confident that what they're asking you to do will not modify your
files or important system files.

Common advice that you read on the internet when something doesn't work,
specifically related to "Permission denied" is "Run it with `sudo`". Do not "Run
it with `sudo`". Instead, stop and ask why you're getting this error in the
first place.

You do not have `sudo` privileges on public, shared systems like Aviary, so
don't try using `sudo` on those systems (its use is logged and reported to the
administrators who will probably politely ask you to stop).

:::

Installing new packages on the command line
-------------------------------------------

You will almost certainly also want to install new packages on the command line.
Installing a package on the command line usually consists of two steps:

1. Figure out what the name of the package is that you want to install.
2. Install the package.

### Figuring out package names

Sometimes you already know the name of the package that you want to install and
you can proceed immediately to step 2, but more often than not you don't know
the name of the package.

There are a few ways to figure out what the name of the package is that you want
to install:

* Try running the command you want to use on the command line, and your terminal
  may helpfully tell you what to install:

  :::::: columns
  ::: {.column width=50% .input}
  ```bash
  pandoc
  ```
  :::
  ::: {.column width=50% .output}
  ```
  Command 'pandoc' is not found, but can be installed with:
  sudo apt install pandoc
  ```
  :::
  ::::::
* Search for the name of the program or words related to the program's name with
  `apt search` (you don't need to use `sudo` to do this, `apt search` is not
  installing new files):

  :::::: columns
  ::: {.column width=50% .input}

  ```bash
  apt search tmux
  ```
  :::
  ::: {.column width=50% .output}
  ```
  Sorting... Done
  Full Text Search... Done
  aerc/plucky 0.8.2-1 amd64
    World's Best Email Client
  // LOTS MORE
  tmux/plucky 3.2a-4build1 amd64
    terminal multiplexer
  ```
  :::
  ::::::

  You can decode the results above as:

  * `tmux` is the name of the program
  * `plucky` is the name of the Ubuntu release this package was made for (Plucky
    Puffin)
  * `3.2a-4build1` is the version of this package.
  * `amd64` is the architecture that this package was built for.
* Search for what you're looking for online and have the website tell you what
  to install.

### Installing a package by name

Once you know the name of the package, you can use `apt` to install it:

```bash
sudo apt install tmux
```

:tada:, you just installed a package!

Here are some other packages you can install:

```
fish # a different shell
make # it's make!
build-essentials # a meta-package including a C compiler
```

Installing a packages *outside* of repositories
===============================================

When you're installing packages with `apt` or Ubuntu Software, you're
downloading and installing packages that are hosted in the official
"[repository]". The Ubuntu and Debian repositories are... comprehensive. There's
a huge amount of software packaged for Ubuntu and Debian in the repositories.

Despite the huge amount of software in the repositories, some software *isn't*
in the repositories (including some popular software like Google's Chrome or VS
Code). Some software in the repositories is out of date compared to the version
you want to install.

You can also install packages with your package manager by downloading a package
yourself (e.g., from a project's web site).

::: example

Let's install a more current version of Pandoc than what's in Ubuntu's
repositories.

In your Linux system, open your web browser (Firefox is installed by default),
navigate to Pandoc's home page, go to the "Installing" tab, then click on the
bug "Download the latest installer" button. This will take you to GitHub.
Download the `.deb` version of Pandoc for your architecture (`arm64` for M1 Mac,
`amd64` for everyone else).

This will download the `.deb` package to your `Downloads` folder. You can then
either double-click the package and install the package with your GUI, or open
your terminal and install the package with `apt`:

```bash
# the `./` is important; you must include the full filename.
# your full filename for pandoc might be different from this one!
sudo apt install ./pandoc-2.19.2-1-amd64.deb
```

:::

[repository]: https://help.ubuntu.com/community/Repositories/Ubuntu

Further reading
===============

As with most topics in this course, we're barely scratching the surface here,
especially because we're focusing on Ubuntu. There are **many** Linux
distributions. While Debian has a lot of descendants (and thus lots of other
distros using `apt` and `deb` packages), there are just as many other
distributions that do not use `deb` or `apt`. If you're using this as an
opportunity to try out a different distribution, you should make sure you know
how to install packages in that distribution.

Package managers aren't just for Linux! Both macOS and Windows have unofficial
and official package managers:

* macOS (and Linux, apparently!) has [Homebrew].
* Another macOS package manager is [MacPorts].
* Microsoft makes an official package manager for Windows called [winget].
* Another package manager for Windows is [Chocolatey].

[Homebrew]: https://brew.sh/
[winget]: https://learn.microsoft.com/en-us/windows/package-manager/
[Chocolatey]: https://chocolatey.org/
[MacPorts]: https://www.macports.org/
