---
title: Download and use a pre-installed OS in VM software (VirtualBox)
author: Franklin Bristow
---

Download and use a pre-installed OS in VM software (VirtualBox)
==================================================

::: outcomes

* [X] Download and use a pre-installed operating system in a virtual machine
  software.

:::

You've been using Windows or macOS (or maybe Linux!) on your personal computer
and you're using Linux when you connect to Aviary.

We're going to try something a little different here and use a brand new
experimental operating system called [SerenityOS].

::: aside

SerenityOS is a fascinating project: it's a brand new, from scratch operating
system and environment that was started by one person that's grown into a pretty
big community.

The main author of SerenityOS (Andreas Kling) has been developing SerenityOS
entirely in the open, including [live-streaming coding on YouTube].

[live-streaming coding on YouTube]: https://www.youtube.com/c/AndreasKling

:::

[SerenityOS]: https://serenityos.org

Download an image
-----------------

We're going to download an "image". The full name for this thing is "disk
image", this is a bit for bit copy of a hard drive or disk. Everything else that
we need to set up is going to be done in VirtualBox itself.

::: warning

For our virtual machine, we are going to use one specific version from January 2023.
Download the SerenityOS from the following link:
<https://serenity-builds.halves.dev/builds/2023-01-03/>

:::

The latest image of SerenityOS can be found here:
<https://serenity-builds.halves.dev/>

There are two options: a "Raw image" or "VirtualBox VDI". The raw image can be
used in software like qemu or can be converted to work with other VM software.
We're using VirtualBox, so let's just download the VirtualBox VDI.

The image that you download is compressed using GZip, so you're going to need to
decompress the image before you can use it with VirtualBox.

<details><summary>Decompressing with macOS or Linux</summary>

Open your terminal and change directory to where the image was downloaded
(probably your Downloads) folder.

Once you're there, you can decompress it with `gunzip`:

```bash
gunzip *.gz
```

</details>

<details><summary>Decompressing with Windows</summary>

Windows doesn't support decompressing GZipped files by default, so you're going
to need to install a new decompression tool that does.

We recommend you install [7-zip]; it's free and open source, supports a really
wide variety of compression formats, and is fast.

Once you've installed 7-zip, you should be able to just double-click on the file
you downloaded and decompress it.

[7-zip]: https://7-zip.org/

</details>

Create a new VM
---------------

We're going to be creating a new VM from an existing image. You should actually
follow the instructions in [the SerenityOS documentation for VirtualBox].

[the SerenityOS documentation for VirtualBox]:
https://github.com/SerenityOS/serenity/blob/master/Documentation/VirtualBox.md#creating-the-virtual-machine

Run the VM
----------

Once you've got the VM configured, it's time to [start it]!

If everything worked out, you should see SerenityOS starting up :tada:!

[start it]: https://www.virtualbox.org/manual/ch01.html#intro-running

### Snapshots

One thing we can do with running virtual machines that we can't do with physical
hardware is *take snapshots* :camera:. Taking a snapshot of a virtual machine
gives you the ability to capture the state of the virtual machine, then go back
to that state.

Read a bit more about snapshots in [the VirtualBox documentation about
snapshots], then try it out!

[the VirtualBox documentation about snapshots]:
https://www.virtualbox.org/manual/ch01.html#snapshots
