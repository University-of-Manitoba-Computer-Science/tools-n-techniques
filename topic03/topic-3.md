---
title: "Version Control"
author: Franklin Bristow
---

::: outcomes

* [X] Use version control software on your own code to keep track of changes
  that you make over time (initializing and adding changes to a repository).
* [X] Use version control software on your own code to make changes and quickly
  be able to revert to a working state.
* [X] Identify files that should not be version controlled and make sure they
  aren't included in a repository's history (`.gitignore`).

:::

Version control is something that's been around for a long time and different
people have different opinions about how to do version control and which
software should be used for version control. We're going to focus on a specific
version control tool: [`git`].

Version control software helps you keep track of the changes that you've made to
your own code or any kind of file over time. Version control isn't entirely
automatic, you have to tell the software which files to track and when it should
track changes.

[`git`]: https://en.wikipedia.org/wiki/Git

Initializing a repository
=========================

We have to tell our version control software where the files are that we want it
to help us manage. Most of the time this is a single folder where you keep your
source code for a specific assignment or project. We're going to call this
location where files are a "repository".

We have to "initialize" the repository. Initializing the repository has the
version control software create some new files and folders that *it* uses to
help keep track of the changes we make to our files.

::: example

Let's start by making a new directory (somewhere appropriate in your folder
structure).

```bash
mkdir my-project
cd my-project
```

Once in the directory that contains the files (or *will* contain the files) that
we want to track, we can ask our version control software to initialize the
folder as a repository. With Git, this is a special command called `init`.

```bash
git init -b main 
```

Git should then tell you that it's "Initialized an empty Git repository" in this
directory!

:::

::: aside

When you initialized the repository, Git told you that it initialized the
repository in your directory and then there was a folder at the end named
`.git/`.

Try running `ls` in your directory. Can you see that folder?

...

No. You can't see that folder. Where is it?

You *can* see that folder if you ask `ls` to list **a**ll files:

:::::: columns
::: {.column .input width=50%}

```bash
ls -a
```

:::
::: {.column .output width=50%}

```
./  ../  .git/
```

:::
::::::

And look at that, there are those two special directories that we've seen
before: `.` the current directory and `..` the parent directory.

:::

Now that we've got an empty repository, we can start adding files to it. Version
control software generally requires that you tell it specifically which files
you want it to keep track of. That means that Git isn't going to keep track of
files that just happen to be in the same directory as the repository, you have
to tell Git to actually keep track of those files.

Adding files to a repository
============================

Create some new files in the repository:

* Make a new plain text file with some text in it using a command-line text
  editor like `vim`. Name the file `README.md`.
* Transfer a file from your computer to Aviary into this directory.
* Copy the `hello` folder from wherever it is to this directory. 

  ::: aside

   You can copy files from one place to another on the same computer using the
   `cp` command. You can copy entire folders from one place to another using the
   `-r` option for recursive (just like `scp`!).

   To copy the `hello` folder here, you can use `cp` from this directory:

   ```bash
   cp -r ../hello . # if hello is in the parent directory
   ```

  :::

Even though we put these files into this directory with the repository, Git
still doesn't know anything about them. We have to add these files to the
repository in two steps:

1. "Staging" the changes by adding them with the `add` subcommand, and
2. Committing the changes using the `commit` subcommand.

"Staging" changes
-----------------

Adding files to the repository is straightforward: you use `git add` and then
tell Git which files should be added to the repository.

Files that you add with `git add` are "staged" --- Git knows that the files
exist and that you want it to track changes to these files, but Git isn't
actually ready to track the changes.

::: example

You can add files and changes to the repository one at a time using `git add`
and including the name of the file that you want to add:

```bash
git add README.md
```

You can also add entire folders to the repository:

```bash
git add hello
```

You can also add *everything in the current working directory* to the
repository:

```bash
git add .
```

:::

Git doesn't tell you anything when you add files or changes to be staged, but
you can ask Git to tell you about the current state it's in by using the
`status` subcommand.

::: example

You can find out which files or changes are staged to be committed using `git
status`:

:::::: columns
::: {.column .input width=50%}

```bash
git status
```

:::
::: {.column .output width=50%}

```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
          new file:   README.md
```

:::
::::::

Git helpfully tells you how to *unstage* a file if you accidentally added a file
or change you didn't want to add to the repository.

:::

Committing changes to the repository
------------------------------------

Even though Git knows about the files or changes that you've staged, you haven't
told git that you *really* want it to track changes to those files.

A "commit" is what Git really manages: what a specific set of files looked like
at a specific point in time.

When you make a commit to a repository, you're telling your version control
software that the changes that you've made to these files are important and it
should keep track of that. Some important times where you would want to keep
track of things:

* The first time you create a repository and you're adding some files to it.
* When the thing you're working on *works*.
* When you've finished working on a small part of a bigger project.

When you make a commit to a repository, you have to include a "commit message":
a brief, human-readable message describing what you're committing to the
repository.

We can commit staged changes to our repository using the `commit` subcommand.

::: aside

Unfortunately, we've got to do some one-time set up before we can make our first
commit. It's OK If you skip this step (you can fix it later), but things will
flow more smoothly if you do it now.

Before we can make a commit, we need to tell `git` who we are. We can configure
`git` and tell it who we are with the `git config` command:

```bash
git config --global user.name "Your name"
git config --global user.email you@myumanitoba.ca # you should use your own
                                                  # e-mail address here.
```

You only need to do this once per physical computer that you're using `git` on.
In other words: if you're using two computers, you'll need to run this set up
step on each computer, but you only need to do it once.

:::

::: example

We can commit staged changes to a repository using `git commit` and either
writing a commit message in the command itself, or writing a longer commit
message in your text editor.

:::::: columns
::: {.column .input width=50%}

```bash
# commit with a message inline
git commit -m "Initial commit"
```

:::
::: {.column .output width=50%}

```
[main (root-commit) acff39c] Initial commit
 1 file changed, 10 insertions(+), 0 deletions(-)
 create mode 100644 README.md
```

:::
::::::

Your commit is going to look different from mine because you added more files
than me to your commit and you used a different commit message.

You can write a longer commit message by leaving out the `-m` part, and this
will ask Git to open up your text editor where you can write a longer message.

```bash
git commit # opens your text editor to write a message
```

:::

After you commit your changes to the repository, everything still looks pretty
normal. Your files are all still there. Great :tada:!

You can ask Git to tell you what its status is again with `git status`, but this
time it's just going to say that there is nothing to commit

:::::: columns
::: {.column .input width=50%}

```bash
git status
```

:::
::: {.column .output width=50%}

```
On branch main
nothing to commit, working tree clean
```

:::
::::::

::: aside

Git commit messages are important metadata (data about your data) that help you
(or others) better understand the changes that you've made to your files over
time. They're a lot like writing comments in code in the sense that they
shouldn't describe the files that you changed or even describe how you changed
the files, but should describe why you changed the files and what the ultimate
side-effect is ("I fixed this bug!").

Lots of people have opinions on Git commit messages:

* Tim Pope writes about them in [A Note About Git Commit Messages].
* Chris Beams writes about them in [How to Write a Git Commit Message].
* Randall Munroe visualizes them in [Git Commit].

[A Note About Git Commit Messages]:
https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[How to Write a Git Commit Message]: https://cbea.ms/git-commit/
[Git Commit]: https://xkcd.com/1296/

:::

Adding changes and committing them to your repository is something that you
should be doing not just when you initialize the repository, but frequently as
you're doing your work. You should add any changes to your repository each time
you accomplish something (a new method is working, a bug has been fixed, a
feature is complete).

Reverting changes
=================

Initializing our repository and adding and committing files and changes to our
repository is great, but just adding stuff to the repository isn't exactly
useful.

One important use for version control is being able to go back in time to
changes that were previously committed to the repository.

Let's make some changes to our file. We don't actually care what the changes are
because we're making these changes to be able to see how to *undo* changes.

We can revert uncommitted changes to a file using the `restore` subcommand in
Git.

::: example

Mess up your `README.md`. Go ahead. Have fun!

Here are some things you can do:

* Open it in your text editor and start typing.
* "Accidentally" copy a file and replace `README.md` with that file

  ```bash
  cp hello/compiled/hello.c README.md
  ```
* Remove your `README.md`

  ```bash
  rm -f README.md # LIVE DANGEROUSLY
  ```

Once you've made changes to your file, you can ask Git to tell you about the
status of the file (with `git status`). Depending on what you did, Git will tell
you different things, but it will importantly *notice that something has
changed*. Git will also helpfully give you a hint about how to get your files
back to the state they were in before.

Now revert the changes you made to your `README.md` with the `restore` subcommand

```bash
git restore README.md
```

Now open up your `README.md` again, and it's back to the way it was before you
made the changes!

:::

Files that *shouldn't* be version controlled
============================================

Being able to keep track of changes to our important files is great, but there
are some files that will have changes that *don't* care about.

Some examples of files that will change as you change your own files:

* The `.class` files that get generated when you compile Java programs.
* The `.docx` and `.pdf` files that you generate when converting from Markdown to
  those formats.
* Output files that get generated when you run certain programs.

The common identifying property of all of these files is that they are files
that get *generated* or *created* by something else from the file that you want
to keep track of (`.class` files are generated from the `.java` files you care
about; `.docx` in this case is generated from the `.md` files that you care
about).

We don't usually want to include these files in a version control repository for
a couple of reasons:

1. We can really quickly re-generate them from the files that we're working
   from (it's pretty easy to run `pandoc` again!).
2. Sometimes these files can be **really** big in terms of file size.
3. They are extra changes in our version control history that we *don't care
   about*.

We can tell Git to ignore certain files when they change by created a special
file named [`.gitignore`] in our repository.

::: example

Use your text editor to create a new file named `.gitignore` in the same folder
as your repository.

Each line in a `.gitignore` file is either a comment (lines beginning with `#`)
or describes specific filenames or "patterns" of filenames to be ignored.

Here's an example of what a `.gitignore` file might look like:

```ini
# Ignore README.docx (a specific filename)
README.docx

# Ignore all .class files (a "pattern", any file that ends with .class)
*.class

# Ignore the entire build directory
build/
```  

:::

The `.gitignore` file *is* a file you want Git to keep track of, so you need to
add this file to your repository (use `git add`).

::: aside

Just like the `.git` folder, the `.gitignore` file is "hidden", it doesn't show
up when you try to look at the contents of a directory using commands like `ls`.
This is true in general: any file that begins with a period (`.`) is considered
to be "hidden" on Linux and macOS, but you can see those files by telling a
command like `ls` to list everything (`ls -a`).

:::

[`.gitignore`]: https://git-scm.com/docs/gitignore

Further reading
===============

This document gets you started with version control and Git, but you're
definitely going to run into situations where you want to do things that are
more complex than what we've seen here, or you're going to make a mistake and
need to fix it.

You can find lots of good information online about Git and version control, but
here are some resources that are particularly good or helpful:

* Roger Dudler's [git - the simple guide] does a great job of quickly
  summarizing the tasks you might need to do when doing version control with
  Git.
* Seth Robertson's [On undoing, fixing, or removing commits in git] is a "choose
  your own adventure"-style guide on ... well, undoing, fixing, or removing
  commits in Git! Maybe you accidentally committed a file that you don't want to
  be in your repository, or maybe you accidentally forgot to include a file in a
  commit that *should* have been included in that commit. This will guide you
  through getting into the state that you want to be in.
* If you're OK with some profane language in English, Katie Sylor-Miller's [Oh
  Sh\*t, git!?!] is also an excellent source of solutions to "Please help me!"
  moments that you will *definitely* encounter when you're using `git`.

  ::: aside

  Yeah. I know you can swear on the internet. But I have children. One of my
  children can read and the other is *learning* to read, and they will both
  eventually be able to figure out what sh\*t means (and I'm OK with that), I
  still feel some parental sense of responsibility to keep it clean.

  :::

[git - the simple guide]: https://rogerdudler.github.io/git-guide/
[On undoing, fixing, or removing commits in git]: https://sethrobertson.github.io/GitFixUm/fixup.html
[Oh Sh\*t, git!?!]: https://ohshitgit.com/
