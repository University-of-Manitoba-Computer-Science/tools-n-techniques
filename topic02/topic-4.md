---
title: "Tab completion"
author: Franklin Bristow
---

Tab completion
==============

::: outcomes

* [X] Complete commands and filenames with tab completion.

:::

Interacting with the command line requires [a lot] of typing (you can keep
clicking on the terminal window, but seriously, that clicking and tapping is
going to get really annoying).

Here's a little tip to save you (some) typing: You can use the <kbd>Tab</kbd>
key on your keyboard to *complete* a command or filename when you are typing.

::: example

Change back to your home directory (`~`), then start changing into the `hello`
directory, but before you finish typing `hello`, press the <kbd>Tab</kbd> key on
your keyboard.

```bash
[you@bird somewhere]> cd ~
[you@bird ~]> cd he#TAB
```

Your shell (the thing you're typing commands into) will try to automatically
complete the name of the file. [Neat :camera_flash:]!

:::

[a lot]:
http://hyperboleandahalf.blogspot.com/2010/04/alot-is-better-than-you-at-everything.html
[Neat :camera_flash:]: https://www.youtube.com/watch?v=u6RNtjYxiNw
