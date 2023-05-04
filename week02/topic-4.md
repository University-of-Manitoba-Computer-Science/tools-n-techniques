---
title: Converting documents to different formats
author: Franklin Bristow
---


Converting documents to different formats
=========================================

::: outcomes

* [X] Convert plain text documents to different formats (e.g., `docx`).

:::

We installed Pandoc, then shifted to writing a bunch of plain text. Now we're
back to using Pandoc. The purpose of installing Pandoc is that it's a tool we
can use to take the plain text document that we're writing and convert it into a
format that's easier to share with other people who are expecting things like
Word or PDF documents.

We're going to use Pandoc to convert a plain text Markdown-formatted document
into a Word-formatted document. We're going to have to do a *little bit* of work
in our Terminal, so if you closed your terminal, you should open it up again
like you did before when [verifying that Pandoc is installed].

First: **Save** your plain text Markdown-formatted document *somewhere*. I'm
going to recommend that (for now!) you save this file to your Desktop folder.

Make sure that you save your file with a name that has a `.md` extension. This
isn't *super* important, but it makes Pandoc's job a little easier when deciding
what kind of file it's converting, and it makes opening the Markdown file with
VS Code a little bit easier.

Once you've saved your file, switch to your terminal, then type:

```bash
cd Desktop
```

Congratulations :tada:! You just ran your second terminal command (Second?!
Yeah! you ran `pandoc` earlier!).

Converting to Word
------------------

OK, but now we need to do the hard work of actually converting our
Markdown-formatted document to a Word file. It's actually straightforward:

```bash
pandoc "your_file.md" -o "your_file.docx"
```

You should replace `your_file.md` with whatever your file's name is, and you
should replace `your_file.docx` with whatever you want the Word-formatted
document to be named.

If everything's working, Pandoc won't print out anything, but you *should* be
able to look at your desktop and see *two* files: your Markdown-formatted plain
text file **and** a Word-formatted `.docx` file :tada:!

Open up the Word-formatted file with Microsoft Word, Office 365, or Google Docs
and take a look.

If Pandoc *did* print something out, a few things could be wrong:

* You might not have saved your file to your Desktop folder. Try saving the
  document in VS Code again (use File &rarr; Save as...) and make sure to save
  it to your Desktop folder.
* You might not have saved your file with a `.md` extension. Try saving the
  document in VS Code again (use File &rarr; Save as...) and make sure that when
  you enter a name for your file that the name of the file ends with `.md`.
* Your terminal might not be in the Desktop directory when you ran the `pandoc`
  command. Try entering `cd Desktop` again. If nothing gets printed out, then
  you *should* be in your Desktop folder. If something does get printed out,
  then you can't access your Desktop folder from where you are right now. Your
  terminal could be anywhere right now, so your best course of action would be
  to ask for help!
