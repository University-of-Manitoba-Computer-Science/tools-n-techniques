---
title: Choose a Linux distribution
author: Franklin Bristow
---

::: outcomes

* [X] Choose a Linux distribution.

:::

When we're thinking about installing Linux on our computer or in a virtual
machine we've got to make some choices *before we can even begin* installing
Linux. Before we can make those decisions, we've got to get on the same page
about some terminology.

What even is Linux?
===================

Linux is an [overloaded] word, it can mean at least two different things:

1. Linux can mean an entire operating system, or
2. Linux can mean just the "kernel" for an operating system.

What's an [operating system]? An operating system is one or more pieces of
software that manage hardware resources and provide a consistent "interface" for
programs (not a GUI, but a set of "functions" to ask for things to be done like
reading and writing files). An operating system usually consists of a "kernel"
and a suite of utilities that a regular human can interact with (like a shell or
a GUI).

What's a [kernel]? A kernel is a *big* piece of software (usually written in C
(Linux) or C++ (Windows), but sometimes written in newer languages like [Rust]
(Redox)) that does the low-level hardware resource management.

The [Linux kernel] is an operating system that's written in C and is used
**everywhere** (it's on your computer *right now*; if you're using an Android
phone, it's also in your pocket!).

When the Linux kernel is put together as a complete operating system, [it's
usually bundled with "GNU" utilities]. You're more than welcome to read about
the entire idea of GNU/Linux, but be forewarned: this is a **deep** [rabbit
hole].

[overloaded]: https://en.wikipedia.org/wiki/Function_overloading
[operating system]: https://en.wikipedia.org/wiki/Operating_system
[Rust]: https://rust-lang.org
[Redox]: https://redox-os.org/
[Linux kernel]: https://kernel.org/
[it's usually bundled with "GNU" utilities]:
https://www.gnu.org/gnu/linux-and-gnu.html
[rabbit hole]: https://en.wiktionary.org/wiki/rabbit_hole
[kernel]: https://en.wikipedia.org/wiki/Kernel_(operating_system)

What is a distribution?
=======================

Linux can be minimally distributed as the kernel plus the GNU suite of
utilities, but it would be *really* minimal. Installing new software would be
painful and tedious. Browsing the web would pretty much be impossible (this
isn't a challenge; yes, you could do it, but gosh, it would be painful).

When we are getting a "Linux operating system", we're usually choosing a
"distribution" of Linux. A distribution (also often shortened to "distro")
is a complete package that usually consists of the following:

* The Linux kernel
* The GNU suite of utilities
* Many other command-line programs that are useful, but not part of the GNU
  suite of utilities.
* An [init system], a program that starts up other programs when your computer
  starts up.
* A [package manager] that you can use to download and install other programs
  (instead of downloading and compiling source code).
* A [desktop environment] (or DE); a GUI that you can use to run graphical
  programs like a web browser.
* A suite of graphical software (e.g., [LibreOffice], [Firefox]).

There are *a lot* of distributions to choose from: 

![Timeline of Linux distributions ([&copy; FabioLolix, CC BY-SA 3.0](https://en.wikipedia.org/wiki/Linux_distribution#/media/File:Linux_Distribution_Timeline_21_10_2021.svg))](distros.svg)

Like a lot a lot. Seriously. [Open this image in a new tab] and just scroll.

Why?! Why are there so many???!!! (Can you sense the exasperation in this?)

Here's the short answer: there are so many because people get [*just annoyed
enough* to make something new], and because they can.

Anyone can make a new Linux distribution (yes, even you!) because Linux and most
of the software that come packaged in distributions are [free and open-source].

[init system]: https://en.wikipedia.org/wiki/Init
[desktop environment]: https://en.wikipedia.org/wiki/Desktop_environment
[package manager]: https://en.wikipedia.org/wiki/Package_manager
[LibreOffice]: https://www.libreoffice.org/
[Firefox]: https://www.mozilla.org/en-US/firefox/
[Open this image in a new tab]:
https://upload.wikimedia.org/wikipedia/commons/b/b5/Linux_Distribution_Timeline_21_10_2021.svg
[free and open-source]:
https://en.wikipedia.org/wiki/Free_and_open-source_software
[*just annoyed enough* to make something new]:
https://en.wikipedia.org/wiki/Devuan

How should I choose one?
========================

OK, so there are a lot. Like a lot a lot. But that's overwhelming. How do I
choose?

Here are some questions you can answer that will help you decide which of the
popular Linux distributions you should choose:

* Do you want an OS that has a friendly user interface, or are you OK using the
  command-line to do most things?
* Do you want an OS where it's very easy to ask for or pay to get help, or are
  you OK reading lots of documentation to help you out when you get stuck with
  something?
* Do you usually want the latest and greatest versions of software, or would you
  prefer to stick with stable and secure, even if it is older?

The most popular distributions are the best starting point; here's a list of
some popular distributions:

* [Ubuntu] (user friendly; easy to ask or pay to get help; tries to compromise
  between stability and keeping up to date with the latest and greatest).
* [Fedora] (user friendly; easy to ask for help; tries to compromose between
  stability and keeping up to date with the latest and greatest).
* [OpenSUSE] (user friendly; easy to ask or pay to get help; tries to compromise
  between stability and keeping up to date with the latest and greatest).
* [Red Hat Enterprise Linux] (user friendly; pay to get help; focus
  primarily on stability).
* [ArchLinux] (not user friendly, most things are done on the command-line; easy
  to ask for help; trying to keep up with the latest and greatest sometimes at
  the expense of stability).
* [Debian] (user friendly-ish; easy to ask for help; focus primarily on
  stability).

For the purposes of this course , we recommend that you choose [Ubuntu]. Ubuntu
is easy to use, has a very large community of users to get support from, and has
a company backing it ([Canonical]) that you can pay for support you, if you need
it.

That said: if you're interested in trying something new, or you want to go
through the process of making your own choice, you can use a tool like
[Distrochooser] to help you.

[Distrochooser]: https://distrochooser.de/
[Ubuntu]: https://ubuntu.com/
[Fedora]: https://getfedora.org/
[OpenSUSE]: https://www.opensuse.org/
[Red Hat Enterprise Linux]:
https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux
[ArchLinux]: https://archlinux.org/
[Debian]: https://www.debian.org/
[Canonical]: https://canonical.com/

Why use Linux at all?
=====================

"My computer came with an operating system (Windows, macOS). Why would I want to
use a different operating system at all?"

Here's why I (me, Franklin) use Linux on my computers:

1. Linux is free. Windows and macOS come with your computer, but they are not free.
   They are neither [free as in speech nor free as in beer]. You pay for Windows
   and macOS when you buy your computer. For Windows: if you never use the
   Windows installed on your computer, you can (in theory) request a refund from
   the manufacturer of your computer.

   Linux is free as in beer (you do not need to buy Linux, it's freely available
   on the internet), and is free as in speech (not only can you download and use
   it for free, but you can also read its source code, modify its source code,
   and republish its source code).

   I consider both of these to be important.
2. (Get ready to put on your [tin foil hats]) Windows is slowly  *becoming* free
   as in beer (you don't pay anything for it), but the reality is that Microsoft
   is making money from users by showing ads ([[1]], [[2]], [[3]]) and Microsoft
   [collects a lot of data about your usage].
3. Linux distributions make it easy for me to do what I want to do with my
   computer. I spend a lot of time writing in `vim` (mostly code and Markdown).
   I write a lot of code in Java and C. I spend a lot of time on the command
   line (I use [`fish`]). Installing and using all of these tools is
   straightforward or trivial with Linux distributions.

   Microsoft is making it *easier* to do that (I do spend a lot of time using
   the Windows subsystem for Linux), and tools like [Homebrew] make it easier
   for me to do that in macOS, but why use systems where it's just now being
   made easier when it's already easy in another system?
4. Linux distributions give me choices about a lot of things. Even when I'm
   picking a distribution like Ubuntu that's made a lot of choices for me, I can
   still make decisions about what I want later on:

   * I can use different terminal software ([Terminator], [kitty], [Hyper]).
   * I can trivially change [icon themes].
   * I can completely switch [desktop environments] ([Gnome], [KDE],
     [Elementary]).
   * I can even go *without* desktop environments and use bare [window managers]
     ([berry], [enlightenment], [Hyprland]).

Of course, these are idealistic reasons to use Linux. Why *shouldn't* you use
Linux?

1. There are still issues with some (generally the newest) hardware. Linux is
   *barely* running on [Apple Silicon]. Sleep doesn't always work on the newest
   laptops, or it does with tinkering. That said, Linux works surprisingly well
   on older hardware.
2. Microsoft Office, Adobe Photoshop, many (but fewer than before) commercial
   games do not work on Linux at all. Yes, there's [Wine]; yes, there are web
   versions of Office; yes, Steam and Proton are amazing; but they aren't
   drop-in replacements for everything.
3. Getting support can be harder. The Windows community is... to say that it's
   huge is an understatement. The market share for Linux is [lower than
   "Unknown"]. That said, you can pay for support (but that sort of negates the
   whole "free" thing), and the support communities for Linux are *generally*
   welcoming and helpful.

[tin foil hats]: https://en.wikipedia.org/wiki/Tin_foil_hat
[free as in speech nor free as in beer]:
https://en.wikipedia.org/wiki/Gratis_versus_libre
[[1]]:
https://www.pcmag.com/news/microsoft-experiments-with-ads-in-the-windows-11-start-menu
[[2]]:
https://www.bleepingcomputer.com/news/microsoft/microsoft-is-showing-ads-in-the-windows-11-sign-out-menu/
[[3]]:
https://arstechnica.com/gadgets/2022/03/microsoft-accidentally-reveals-that-it-is-testing-ads-in-windows-explorer/
[collects a lot of data about your usage]:
https://privacy.microsoft.com/en-us/data-collection-windows
[Homebrew]: https://brew.sh/
[Terminator]: https://gnome-terminator.org/
[kitty]: https://sw.kovidgoyal.net/kitty/
[Hyper]: https://hyper.is/
[icon themes]: https://www.omgubuntu.co.uk/best-icon-themes-ubuntu
[desktop environments]: https://en.wikipedia.org/wiki/Desktop_environment
[GNOME]: https://www.gnome.org/
[KDE]: https://kde.org/
[Elementary]: https://elementary.io/
[window managers]: https://en.wikipedia.org/wiki/Window_manager
[berry]: https://berrywm.org/
[enlightenment]: https://www.enlightenment.org/
[Hyprland]: https://hyprland.org/
[Apple Silicon]: https://asahilinux.org/
[Wine]: https://www.winehq.org/
[lower than "Unknown"]:
https://gs.statcounter.com/os-market-share/desktop/worldwide
[`fish`]: https://fishshell.com
