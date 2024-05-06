---
title: "Connecting to a remote computer"
author: Franklin Bristow
---

Connecting with SSH
===================

::: outcomes

* [X] Connect to a remote computer using `ssh`.

:::

You opened your terminal *briefly* in [installing software on your personal
computer] to install and run Pandoc to convert your Markdown-formatted plain
text document into a `.docx` file.

Your terminal isn't just for running Pandoc: terminals can be used to run many
different programs, including running programs that will let you connect to
other computers and run programs on *those* computers.

::: warning

These instructions assume that you are connecting to a remote computer when you
are on campus connected to U of M WiFi. If you are trying to do this from home,
you first need to install, configure, and connect to the U of M's VPN. You can
find instructions for installing, configuring, and connecting to the U of M's
VPN on [IST's Virtual Private Network (VPN) page].

:::

If you're on campus connected to U of M WiFi or you're off campus but you've
installed the VPN and connected to it, let's open up our terminals and get
connected to a different computer.

[installing software on your personal computer]: ../topic01/topic-2.html
[IST's Virtual Private Network (VPN) page]:
https://umanitoba.ca/information-services-technology/my-security/vpn-support

Open your terminal
------------------

We opened our terminals in week 2. If you forget how to open your terminal (and
it's totally OK if you do!), refer back to the notes on [verifying that Pandoc
is installed].

[verifying that Pandoc is installed]:
../topic01/topic-2.html#verifying-that-pandoc-is-installed

Connect to a remote computer
----------------------------

Now that your terminal is open, let's connect to a remote computer.

Just like we used the `pandoc` command to run Pandoc, we need to run a command
to connect to a remote computer. The command that we run to connect to a remote
computer is called `ssh`.

::: aside

`ssh` stands for **S**ecure **Sh**ell. Really formally: [SSH] is a "protocol",
an agreed upon way that two computers can talk to each other. SSH consists of a
server (a program running on remote computers waiting for connections) and a
client (the program running on your computer trying to connect to the remote
computer).

Before SSH was [Telnet], but Telnet wasn't secured in any way (someone could
trivially eavesdrop on your connection to the remote computer).

[SSH]: https://en.wikipedia.org/wiki/Secure_Shell
[Telnet]: https://en.wikipedia.org/wiki/Telnet

:::

When we're connecting to a remote computer we need to have some information to
tell the program on our computer how to connect to the remote computer, and some
information that we're going to use to identify ourself.

::: checklist

Before you start connecting to a remote computer, you need:

1. [ ] The **name and location** of the remote computer (an address).
2. [ ] Our **username** on the remote computer (how we identify ourselves to the
   computer).
3. [ ] Our **password** on the remote computer (how we prove our identity to the
   computer).

:::

Here's what you need to know to connect to the U of M CS computer systems.

1. [X] The **name and location** (address) of the remote computer for the CS
   department is

   ```
   aviary.cs.umanitoba.ca
   ```

   ::: aside
    
   Aviary is not actually a real computer, but instead is an address for
   **many** computers. Each time you connect to the address
   `aviary.cs.umanitoba.ca`, you will be redirected to a different computer
   named for a specific bird (e.g., `pelican.cs.umanitoba.ca`).

   Aviary is a [round-robin DNS] name. Get it??? Round-**robin** :bird:. An
   [aviary] is a big bird house! It's funny! It's a joke!

   [aviary]: https://en.wikipedia.org/wiki/Aviary
   [round-robin DNS]: https://en.wikipedia.org/wiki/Round-robin_DNS

   :::
2. [X] Your **username** on this remote computer is your UMNetID (the part of
   your @myumanitoba.ca e-mail address before @myumanitoba.ca).
3. [X] Your initial default **password** is the letters `Cs#` (this is
   upper-case C, lower-case S, and the [number
   sign/hash/hashtag/hex/octothorpe/sharp/...]) followed by your
   student number. If your student number is 1234567, then your initial default
   password would be `Cs#1234567`.

   You will be required to change this the first time you log in to aviary.

[number sign/hash/hashtag/hex/octothorpe/sharp/...]:
https://en.wikipedia.org/wiki/Number_sign#Names

Now that you've got that information we can actually start connecting to a
remote computer. When we're connecting to remote computers, we're going to use
the `ssh` command and tell `ssh` how to connect to the remote computer. Connecting
to a remote computer will always look like this:

::: example

```bash
ssh you@name.remote.ca
```

* `you` is where you put your **username**. Replace `you` with *your* username.
* `name.remote.ca` is where you put the **name and location** of the remote
  computer. Replace `name.remote.ca` with the address you want to connect to.

If I want to connect to Aviary, my username is `fbristow` and the address is
`aviary.cs.umanitoba.ca`, so:

```bash
ssh fbristow@aviary.cs.umanitoba.ca
```

:::

When you press <kbd>Enter</kbd> on your keyboard, the very first time you
connect to a system, `ssh` is going to ask you if it's safe to connect:

```
The authenticity of host 'aviary.cs.umanitoba.ca (130.179.28.114)' can't be established.
ED25519 key fingerprint is SHA256:XXXXXXX.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

This is a pretty scary looking warning! The summary of this is that `ssh` is
telling you that it doesn't recognize the computer you're trying to connect to.
When you're connecting to Aviary, you *may* see this warning more than once. You
can safely enter `yes` (and you must enter `yes`, not just `y`) and press
<kbd>Enter</kbd>.

Next, `ssh` is going to ask you to enter your password. Type in your password,
but note that you won't see any feedback as you're typing (you won't see any `*`
or dots), but type in your password, then press <kbd>Enter</kbd> on your
keyboard again. If everything's worked out, you should be connected to the
remote computer :tada:!

::: example

Here's what I see when I connect to the CS Department's aviary. 

```bash
ssh fbristow@aviary.cs.umanitoba.ca
Password: 
[fbristow@hawk ~]> 
```

This time I'm connected to a computer named `hawk`, you could be connected to
[one of many bird machines]. You can disconnect from a remote computer by typing
the command `exit` on your keyboard, then pressing <kbd>Enter</kbd>.


[one of many bird machines]:
https://linux-www.cs.umanitoba.ca/cgi-bin/man?machines

:::
