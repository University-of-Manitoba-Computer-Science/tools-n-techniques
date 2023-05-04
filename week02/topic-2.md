---
title: Installing software on your personal computer
author: Franklin Bristow
---
  
Installing software on your personal computer
=============================================

::: outcomes

* [X] Install software on your personal computer (e.g., `pandoc` and VS Code).

:::

Before we can really do *anything* in this course, you're going to need to
install some software on your computer. Your computer already has lots of
software installed on it and you maybe installed some of that software yourself.

We're going to install two pieces of software that you're going to be using
throughout the course: [Visual Studio Code] (henceforth "VS Code") and [Pandoc].

Installing software is generally fairly straightforward, and the first thing
you're going to need to do is download the software to your computer.

[Visual Studio Code]: https://code.visualstudio.com/
[Pandoc]: https://pandoc.org/

VS Code
-------

### Downloading VS Code

Open your web browser (e.g., Edge, Chrome, Safari, Firefox) and navigate to
<https://code.visualstudio.com/>.

The VS Code website is usually smart enough to figure out which operating system
you're running and lets you pick the right type of file to download on the main
page, but you can also go straight to [the download page]. You'll need to
download the right package for your operating system. There are lots of options,
but you should just click on the big buttons for "Windows", "Mac", or
`.deb`/`.rpm` if you're running Linux.

[the download page]: https://code.visualstudio.com/Download

### Installing VS Code

How you install VS Code depends on the operating system you're using.

<details><summary>Installing VS Code on Windows</summary>

Find the file that you downloaded (a `.exe` file) and double-click on it. Follow
the prompts.

</details>

<details><summary>Installing VS Code on macOS</summary>

Find the file that you downloaded (a `.zip` file) and double-click on it. Copy
and paste the folder into your "Applications" directory to install it.

</details>

<details><summary>Installing VS Code on Linux</summary>

Find the file that you downloaded (a `.deb` or `.rpm` file) and double-click on
it. Your software manager should then prompt you to install the package, follow
the prompts.

</details>

### Verifying that VS Code is installed

Once you've gone through the install process, you should check that VS Code is
actually installed on your computer by running VS Code.

<details><summary>Running VS Code on Windows</summary>

VS Code *may* have added an icon to your desktop, depending on whether or not
you allowed it to when it was installing. If you can find an icon on your
desktop for VS Code, double-click on it.

If you can't find an icon on your desktop for VS Code, you will be able to find
it in the Start menu. Either click on the Microsoft logo in the corner of your
screen, or press the Microsoft key (the "super" key) on your keyboard, then
start typing "VS Code". When you see VS Code appear, click on it.

</details>

<details><summary>Running VS Code on macOS</summary>

Find the VS Code folder in your Applications folder and double-click on it.

Optionally drag the VS Code icon from your Applications folder to your dock so
that opening VS Code later is easier.

</details>

<details><summary>Running VS Code on Linux</summary>

VS Code *may* have added an icon to your desktop. If you can find an icon on
your desktop for VS Code, double-click on it.

If you can't find an icon for VS Code on your desktop, you will be able it find
it in your application launcher menu. Either click on the application launcher
menu in the corner of your screen, or press the Microsoft key (the "super" key)
on your keyboard, then start typing "VS Code". When you see VS Code appear,
click on it.

</details>

Pandoc
-----

### Downloading Pandoc

Open your web browser (e.g., Edge, Chrome, Safari, Firefox) and navigate to
<https://pandoc.org>. Click on the "Installing" link at the top of the page.

The Pandoc website is *sometimes* smart enough to figure out which operating
system you're running and links you directly to the right type of file to
download on this page. You can still also go directly to [the latest release
page on GitHub].

The latest releases page has [a lot] of choices, I recommend that you pick:

* The `.msi` file if you're on Windows.
* The `.pkg` file if you're on macOS.
* The `-amd64.deb` file if you're using a Debian-based Linux distribution like
  Ubuntu or Pop!\_OS. If you're using something else and need help, ask for help
  now.

[the latest release page on GitHub]:
https://github.com/jgm/pandoc/releases/latest
[a lot]:
http://hyperboleandahalf.blogspot.com/2010/04/alot-is-better-than-you-at-everything.html

### Installing Pandoc

How you install Pandoc depends on the operating system you're using.

<details><summary>Installing Pandoc on Windows</summary>

Find the file that you downloaded (a `.msi` file) and double-click on it. Follow
the prompts.

</details>

<details><summary>Installing Pandoc on macOS</summary>

Find the file that you downloaded (a `.pkg` file) and double-click on it. Follow
the prompts.

</details>

<details><summary>Installing Pandoc on Linux</summary>

Find the file that you downloaded (a `.deb`) and double-click on it and your
software manager will prompt you to install it.

::: aside

Depending on your experience with Linux-based operating systems, you might be
asking "Why aren't you using a package manager for this?". The answer to that
question is "We're going to use package managers later in the course." If you
feel comfortable using your package manager right now, feel free to install
`pandoc` using your package manager instead of using the `.deb` package.

If you don't know what a "package manager" is, don't worry! We'll get there!

:::

</details>

### Verifying that Pandoc is installed

Unlike VS Code, Pandoc is not a program that has a graphical user interface
(GUI), so no icon will be made for running the program after it's been
installed.

Instead, Pandoc is a program that runs in your **terminal**. To check if Pandoc
has been installed, you're going to need to open your terminal program.

<details><summary>Opening your terminal on Windows</summary>

You have a few different options for terminals on Windows. The one that's built
in is called the "Command Prompt". You can alternatively install another one
from the Microsoft Store called "[Windows Terminal]". I recommend that you
install this (it's worlds better than the Command Prompt), but it's not
required.

Your terminal program **does not** have a desktop icon, so either click on the
Microsoft logo (the "Start menu") or press the Microsoft key (the "super" key)
on your keyboard, then start typing "cmd".  When you see Command Prompt appear,
click on it.

[Windows Terminal]:
https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-ca&gl=CA

</details>

<details><summary>Opening your terminal on macOS</summary>

macOS has a built-in terminal called "Terminal.app". Apple has [good
documentation about how to open Terminal], but the short version is that you
should open your Applications folder, then find the Utilities folder and open
that, then double-click on "Terminal" (*not* "Console"!).

You can optionally drag the Terminal icon to your dock so that it's easier to
launch later (you're going to have to do this every class!).

[good documentation about how to open Terminal]:
https://support.apple.com/en-ca/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac

</details>

<details><summary>Opening your terminal on Linux</summary>

Your terminal program **does not** have a desktop icon, so either click on the
application launcher menu in the corner of your screen, or press the Microsoft
key (the "super" key) on your keyboard, then start typing "terminal". When you
see a terminal application appear, click on it.

</details>

### Running Pandoc

Now that you've got your terminal open, you should be able to run Pandoc. At
this point, it doesn't matter what operating system you're using, running Pandoc
is the same for all.

In your terminal, type in `pandoc` and press <kbd>Enter</kbd>. As soon as you
press <kbd>Enter</kbd>, Pandoc is patiently waiting for you to type something
in.

If you see anything printed to the screen (like an error message), stop here and
ask for help.

If you don't see anything (which is what you should see!), ... type something
in! Let's do the classical "Hello, world". After you type in "Hello, world",
press <kbd>Enter</kbd> on your keyboard, then press (on macOS and Linux)
<kbd>Ctrl</kbd>+<kbd>D</kbd> or (on Windows) press <kbd>Ctrl</kbd>+<kbd>Z</kbd>
then <kbd>Enter</kbd>.

Pandoc should then take your input and turn it into [HTML]:

```html
<p>Hello, world</p>
```

If you see that, then success :tada:! Pandoc is installed.

[HTML]: https://en.wikipedia.org/wiki/HTML
