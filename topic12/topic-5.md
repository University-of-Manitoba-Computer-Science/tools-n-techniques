---
title: Configure and run a web server
author: Franklin Bristow
---

::: outcomes

* [X] Configure and run a web server.

:::

One very popular use for Linux is to run web servers. A web server is a program
that runs on a computer, waiting for requests to come from (for example) web
browsers, and sending back a response so your web browser can (for example) show
you videos of cats.

The first part of this is installing a web server. There are three popular web
servers:

1. [Apache HTTPD]
2. [NGINX] (pronounced like "engine-X")
3. [Caddy]

[Apache HTTPD]: https://httpd.apache.org/
[NGINX]: https://nginx.com/
[Caddy]: https://caddyserver.com/

Installing Caddy
================

Caddy can be installed using `apt`, but you need to do a little bit of extra set
up --- Caddy's packages are *not* in the Ubuntu repositories. Instead, Caddy
hosts its own repositories, and you can add that repository to the set of
repositories `apt` can download from on your system.

The [Caddy documentation] describes what commands you should run, you can run
these commands in your terminal in your Linux system. One addition to the Caddy
documentation is that you may need to install `curl` before following their
guide:

```bash
sudo apt install curl
```

After you've followed the steps in the documentation, Caddy should be running!
Open the web browser in your Linux system and browse to <http://localhost>.

[Caddy documentation]:
https://caddyserver.com/docs/install#debian-ubuntu-raspbian

Configuring Caddy
=================

Now that Caddy's installed, let's get it set up so that the server is serving
what we want instead of the default.

::: aside

Almost everything in this section is very specific to Caddy and isn't really
transferable anywhere else. Configuration files, locations, and what web servers
can do depends entirely on the web server, so what we do here will not in any
way apply to NGINX or Apache HTTPD.

:::

Serve a static string:

* Edit the file `/etc/caddy/Caddyfile` as root:
  ```bash
  sudo vim /etc/caddy/Caddyfile
  ```
* Comment out everything inside the block `:80 {}`
* Add `respond "Hello, world!"` inside the block.
* Restart Caddy so that it starts up with the changes you made.
  ```bash
  sudo systemctl restart caddy
  ```
* Open the web browser in your Linux system and navigate to <http://localhost>
* :wave:

Serve a static file:

* Edit the file `/etc/caddy/Caddyfile` as root.
* Uncomment the lines you commented out.
* Comment out the `respond` line you added.
* Restart caddy.
* Replace `/usr/share/caddy/index.html` with your own `index.html` (maybe by
  converting a Markdown file to HTML, you did this in [reading and changing
  permissions]). Your user account does not have permissions to write to this
  directory, so you can `mv` or `cp` the file with `sudo`:
  ```bash
  sudo mv index.html /usr/share/caddy/
  ```
* Refresh your web browser.
* :tada:

[reading and changing permissions]: ../topic05/topic-4.html

Further reading
===============

Installing a web server inside your Linux install is great, but its use for now
is limited to the web browser inside your Linux install.

Your next steps are to install Caddy on (for example) a virtual machine that
you've created on Azure, buy yourself a domain name, and have your own personal
web page running on Linux by following [some more documentation on the Caddy
website].

If you're running your Linux install in a VM, you can configure "port
forwarding" so that you can connect to your web server from the web browser
installed on your host system, or SSH to your virtual machine.

[some more documentation on the Caddy website]: https://caddyserver.com/docs/
