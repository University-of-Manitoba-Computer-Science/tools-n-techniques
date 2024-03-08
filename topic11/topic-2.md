---
title: Install and configure a virtual machine
author: Franklin Bristow
---

Install and configure a virtual machine
=======================================

::: outcomes

* [X] Install and configure virtual machine software.

:::

All of the topics this week are interrelated (everything's going to be running a
"virtual machine" of some kind), so let's start by getting ourselves set up with
some virtual machine software on our own computers.

What even is a virtual machine?
-------------------------------

... yeah, what the heck even is a "virtual machine"?


You have a physical machine (hardware) in front of you. You're using it right
now to read these words. Physical machines have:

* A CPU (the processor, made of silicon; [the rock we tricked into thinking]).
  CPUs are really good at doing math really really fast (billions of
  calculations per second).
* Some memory (the RAM, also made of silicon; you can imagine this as the
  scratchpad where the CPU can write stuff down temporarily while it's doing
  math really really fast).
* More persistent storage (a disk or drive, ... also increasingly [made of
  silicon], but may be "[spinning rust]"; this is where your files literally live
  as bits and bytes).
* Peripherals (displays, keyboards, touch pads or mice, stuff plugged in to USB
  ports).

You are running a lot of *soft*ware on this hardware:

* Your web browser (Chrome, Firefox, Edge, Safari).
* A terminal emulator.
* Pandoc.

And under all this software lives an "operating system" (Windows, macOS), the
software that controls and manages the resources provided by your hardware so
that programs like Pandoc and your terminal emulator don't have to care about
memory, keyboards, or persistence (they use "system calls" to ask the operating
system to do stuff; the operating system cares about hardware).

Virtual machine software is a program (it's just bits and bytes, just like
`"Hello, world!"`) that can *pretend* to be hardware.

::: aside

Importantly, though, a virtual machine does not "emulate" hardware. An emulator
is a program that will read a binary program that's designed to run on different
hardware (like a game console) that uses a completely different architecture.

A virtual machine provides access to the physical hardware on your machine by
working together with the operating system that's installed on your computer.

:::

Virtual machine software gives us the ability to install and run entire
operating systems *in* the operating environment that we currently have. In
other words, if you have a Mac and you're running macOS, virtual machine
software gives you the ability to run Windows *within* your macOS environment.

[the rock we tricked into thinking]:
https://jakec007.github.io/2020-06-28-how-we-trick-rocks-to-think/
[spinning rust]: https://en.wikipedia.org/wiki/Hard_disk_drive
[made of silicon]: https://en.wikipedia.org/wiki/Solid-state_drive

Choosing your VM software
-------------------------

There are many different choices for Virtual Machine software. Which one you
choose depends on a few different things:

* The hardware you're running (are you running Apple Silicon, or an `x86_64` AMD
  or Intel processor?)
* The "platform" or operating system you're running (are you running Windows,
  macOS, or Linux?)
* The features that the VM software provides (a nice GUI, "snapshots", the kinds
  of hardware it can provide to the OS running within it)
* The popularity of the VM software (yeah, it's a little bit of a popularity
  contest, but more popular VM software means more or better support from a
  community compared to something that's unpopular).

Here are some options:

+--------------+----------------------------------------------------------------+
| Software     | Things to consider                                             |
+==============+================================================================+
| [QEMU]       | * Works on all hardware                                        |
|              | * Works on all platforms                                       |
|              | * Is not at all user friendly (entirely command-line based out |
|              | of the box, though many [GUI front-ends for it exist]); is     |
|              | free and open source.                                          |
|              | * One GUI front-end for macOS is called [UTM], and it is       |
|              | generally quite user-friendly.                                 |
|              | * Is extremely popular.                                        |
+--------------+----------------------------------------------------------------+
| [VirtualBox] | * Works on most hardware (it **does not** run on Apple         |
|              | Silicon).                                                      |
|              | * Works on all platforms                                       |
|              | * Is user friendly; is mostly free and open source.            |
|              | * Is moderately popular.                                       |
+--------------+----------------------------------------------------------------+
| [VMWare]     | * Works on most hardware (Apple Silicon support is getting     |
|              | better).                                                       |
|              | * Works on all platforms                                       |
|              | * Is user friendly, but is confusing to decide which product   |
|              | you should use; can be free, but is not open source.           |
|              | * Is extremely popular.                                        |
+--------------+----------------------------------------------------------------+

We're going to use  either VirtualBox (on Windows, Linux, or macOS with Intel
processors) or a front-end for QEMU called [UTM] (on macOS, especially with
Apple Silicon, but it also works on Intel processors) for this course and guide,
but you're welcome to choose whichever VM software you want.

If you are using Windows or Linux, you should [Install VirtualBox]. 

If you are using macOS with an Intel processor, you can [Install VirtualBox] or
[Install UTM]. If you are using macOS with Apple Silicon, you 
[**must**]{.underline} [Install UTM].

[QEMU]: https://www.qemu.org/
[VirtualBox]: https://www.virtualbox.org/
[VMWare]: https://www.vmware.com/
[GUI front-ends for it exist]:
https://wiki.qemu.org/Links#GUIs_and_management_tools/systems
[UTM]: https://getutm.app/

::: aside

How do I find out what kind of processor I'm using? There are two kinds of
information you may want to know about your processor: the brand (the company
that manufactures the processor) and the "architecture" or "[instruction set
architecture]".


<details><summary>On Windows</summary>

The answer in 2024 is almost guaranteed to be an Intel or AMD processor. The
architecture that your processor uses is called (interchangeably) "x86_64" or
"amd64". If you have a _really_ old computer it might just be "x86", but that's
highly unlikely if your laptop is less than 15 years old.

This is changing, but Windows on other kinds of processors is not yet common.

You can find out what brand and model of processor you have installed on Windows
by [opening the task manager].

[opening the task manager]: https://support.microsoft.com/en-us/windows/find-out-how-many-cores-your-processor-has-3126ef99-0247-33b3-81fc-065e9fb0c35b

</details>

<details><summary>On macOS</summary>

The answer in 2024 could be either Intel or Apple. You can find out what kind of
processor your mac has by [opening the "About This Mac" dialog].

If you bought your Mac as any of "M1", "M2", or "M3" (after 2021), then your 
computer is using Apple Silicon. The instruction set architecture of Apple
Silicon is called "ARM".

If you your Mac was made before 2021 (or you have built a ["Hackintosh"]), then 
your computer may be using an Intel processor and uses the "x86_64" or "amd64" 
(used interchangeably) instruction set architecture. If your Mac is _really_ 
old, it may use the "x86" instruction set architecture.

[opening the "About This Mac" dialog]: https://support.apple.com/en-us/102767
["Hackintosh"]: https://en.wikipedia.org/wiki/Hackintosh

</details>

<details><summary>On Linux</summary>

As with most things Linux, how you accomplish this visually depends on the
[desktop environment] that you have installed.

If you're using [GNOME] and [Ubuntu], you can [discover information about your
system hardware].

If you're using something else (or using GNOME and Ubuntu but want to approach
this a different way), you can find out information about your computer's
processor using the `lscpu` command in your terminal. Depending on what's 
installed on your system, you may also be able to find out information about
your system using the `lshw` command or something like [`neofetch`].

Regardless of the distribution or desktop environment that you're using, you're
almost certainly using an Intel or AMD processor, and the architecture that your
processor uses is called (interchangeably) "x86_64" or "amd64". If you have a 
_really_ old computer it might just be "x86", but that's highly unlikely if your
laptop is less than 15 years old.

[desktop environment]: https://en.wikipedia.org/wiki/Desktop_environment
[GNOME]: https://en.wikipedia.org/wiki/GNOME
[Ubuntu]: https://ubuntu.com/
[discover information about your system hardware]: https://help.ubuntu.com/stable/ubuntu-help/about-hardware.html.en
[`neofetch`]: https://github.com/dylanaraps/neofetch

</details>

[instruction set architecture]: https://en.wikipedia.org/wiki/Instruction_set_architecture
:::



Install VirtualBox
------------------

[Download VirtualBox for your platform] (you should download the
7.0.X series) and [install it].

You can also install the VirtualBox Extension Pack, but we don't need the
extension pack for the work we're doing in this course right now. You *don't*
need to enable Python support (VirtualBox can be configured and managed with
Python scripts, but that's out of scope for this course).

If you're using VirtualBox, you should proceed to [Download and use a 
pre-installed OS in VM software (VirtualBox)]

[Download VirtualBox for your platform]:
https://www.virtualbox.org/wiki/Downloads
[install it]: https://www.virtualbox.org/manual/UserManual.html#installation
[Download and use a pre-installed OS in VM software (VirtualBox)]: topic-3.html

Install UTM
-----------

As above, [UTM for macOS] is a front-end for QEMU for macOS. You should
[download and install UTM].

[UTM for macOS]: https://mac.getutm.app/
[download and install UTM]: https://docs.getutm.app/installation/macos/

::: aside

UTM is free and [open source]. The developer of UTM has published UTM in the
Apple App Store, and where you can buy the software to install it. Buying the 
software on the App Store supports the developer of UTM.

The developer also makes UTM [available for installation on GitHub]. Downloading
UTM from GitHub is free. You should scroll down to the "Assets" section of the
latest release and download the `.dmg` file.

[open source]: https://en.wikipedia.org/wiki/Open-source_software
[available for installation on GitHub]: https://github.com/utmapp/UTM/releases

:::

If you're using UTM, you should proceed to [Download and use a 
pre-installed OS in VM software (UTM)].

[Download and use a pre-installed OS in VM software (UTM)]: topic-4.html
