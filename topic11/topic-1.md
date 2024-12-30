---
title: Introduction
author: Franklin Bristow
---

The ideal way to give your program to someone else to use is either as source
code that they can download and compile (with a build tool!), then install on
their system.

But... sometimes our software grows to be so complex that it has dependencies on
*other* software. Sometimes our software grows to be so complex that it has
dependencies on *specific versions* of software, and it's not exactly reasonable
for you to expect someone to have that specific version on their computer.

Sometimes **you** want to use software that has these same kind of dependencies.
Maybe you want to try out a piece of software, but you can't or don't want to
install all of those dependencies on your main workstation.

Maybe you just want to have a Linux distribution installed on your main machine
without having to fully commit to using Linux all the time. It's OK! We can do
that!

A container is a way that we can package software *and* dependencies together.
Virtual machines are software that allow us to run entire **operating systems**
on our computer without actually installing the operating system as our main
environment.

"The Cloud"&trade; makes extensive use of containers and virtual machines.

We're going to spend some time setting up virtual machine software on our
computers, running a pre-installed operating system in the virtual machine
software, running commands in a container, configuring a container, and setting
up servers in "The Cloud"&trade;

::: outcomes

* [ ] Install and configure virtual machine software.
* [ ] Download and use a pre-installed operating system in a virtual machine
  software.
* [ ] Run a command within a container.
* [ ] Initialize a server in a publicly available cloud computing environment
  (e.g., AWS).

:::
