---
title: Download and use a pre-installed OS in VM software (UTM)
author: Franklin Bristow
---

Download and use a pre-installed OS in VM software (UTM)
==================================================

::: outcomes

* [X] Download and use a pre-installed operating system in a virtual machine
  software.

:::

You've been using macOS (or [maybe Linux]!) on your personal computer and you're
using Linux when you connect to Aviary.

[maybe Linux]: https://asahilinux.org/

::: challenge

Instead of proceeding with the following sections, try getting [SerenityOS] up
and running on your machine by following the [Build Instructions for macOS].

This is a **big** challenge because it requires you to go through the process of
installing *even more* software, including [Homebrew] (a package manager for
macOS).

::: aside

SerenityOS is a fascinating project: it's a brand new, from scratch operating
system and environment that was started by one person that's grown into a pretty
big community.

The main author of SerenityOS (Andreas Kling) has been developing SerenityOS
entirely in the open, including [live-streaming coding on YouTube].

[live-streaming coding on YouTube]: https://www.youtube.com/c/AndreasKling
[SerenityOS]: https://serenityos.org
[Build Instructions for macOS]: https://github.com/SerenityOS/serenity/blob/master/Documentation/BuildInstructionsMacOS.md
[Homebrew]: https://brew.sh/

:::

:::

Download an image
-----------------

UTM makes getting pre-made OS images fairly straightforward. When you first
start UTM, you should see a button labelled "Browse UTM Gallery":

![UTM's main window.](UTM.png)

Click on that button, or go directly to <https://mac.getutm.app/gallery/>.

You can pretty safely choose any of the images that are in the gallery, but to
be consistent, we'll choose [the ReactOS image].

[the ReactOS image]: https://mac.getutm.app/gallery/reactos-0-4-14

::: aside

[ReactOS] is a free and open-source re-implementation of Microsoft Windows. It's
ultimate goal is for people using ReactOS to be able to run ReactOS using
hardware drivers that were built for Windows, and be able to run software that
was built for Windows, but in an entirely free and open-source operating system.

[ReactOS]: https://reactos.org/

:::

You have two options for proceeding: 

1. You can have UTM completely automatically download and configure the virtual
   machine by clicking on the "Open in UTM" button on [the ReactOS image] page,
   or
2. You can configure the virtual machine by yourself.

For now we're content with running the new operating system in a virtual,
so click on the "Open in UTM" button and try it out!

Run the VM
----------

Once you've got ReactOS in your UTM window, you can click on the Play button and
start playing with ReactOS!

### Cloning and running without changes

Virtual machines are entire operating systems running on your computer in
*software*. Because this isn't a complete actual physical computer, we can do a
couple of interesting things that we can't do with real hardware:

1. We can *clone* an existing virtual machine.
2. We can temporarily run the virtual machine without persisting any changes
   made to the OS (sort of like being able to revert a commit with `git`).

#### Cloning

Right click on the ReactOS virtual machine in UTM and select "Clone...". This
will ask if you want to duplicate the entire virtual machine and will make... an
entire copy of the virtual machine. You should now have two copies of the same
virtual machine in UTM.

This can be helpful if you want to (for example) install an operating system
into a virtual machine, then try stuff out and be able to get back to a known
good state. For example, you might be working on figuring out what dependencies
are required when installing your application on a new operating system, you can
run that operating system in a virtual machine, clone it, make changes, and get
back to the original state very quickly.

#### Running without changes

UTM also has the ability to run a virtual machine and discard any changes that
you make while the VM is running.

Right click on the ReactOS virtual machine (one of the two you have now, anyway)
and select "Run without saving changes".

Any changes you make to the virtual machine should be discarded when you power 
the virtual machine off.