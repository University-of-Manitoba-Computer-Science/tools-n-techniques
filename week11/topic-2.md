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
* The operating system you're running (are you running Windows, macOS, or
  Linux?)
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
|              | of the box, though many [GUI front-ends for it exist]; is free |
|              | and open source.                                               |
|              | * Is extremely popular.                                        |
+--------------+----------------------------------------------------------------+
| [VirtualBox] | * Works on most hardware (Apple Silicon support is just        |
|              | beginning)                                                     |
|              | * Works on all platforms                                       |
|              | * Is user friendly; is mostly free and open source.            |
|              | * Is moderately popular.                                       |
+--------------+----------------------------------------------------------------+
| [VMWare]     | * Works on most hardware (Apple Silicon support is just        |
|              | beginning)                                                     |
|              | * Works on all platforms                                       |
|              | * Is user friendly, but is confusing to decide which product   |
|              | you should use; can be free, but is not open source.           |
|              | * Is extremely popular.                                        |
+--------------+----------------------------------------------------------------+

[QEMU]: https://www.qemu.org/
[VirtualBox]: https://www.virtualbox.org/
[VMWare]: https://www.vmware.com/
[GUI front-ends for it exist]:
https://wiki.qemu.org/Links#GUIs_and_management_tools/systems

We're going to use VirtualBox for this course and guide, but you're welcome to
choose whichever VM software you want.

Install VirtualBox
------------------

[Download VirtualBox for your platform] (you should download the
7.0.X series) and [install it].

You can also install the VirtualBox Extension Pack, but we don't need the
extension pack for the work we're doing in this course right now.

[Download VirtualBox for your platform]:
https://www.virtualbox.org/wiki/Downloads
[install it]: https://www.virtualbox.org/manual/UserManual.html#installation
