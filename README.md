Introduction to Tools and Techniques in Computer Science
========================================================

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img
alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work
is licensed under a <a rel="license"
href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons
Attribution-ShareAlike 4.0 International License</a>.

Welcome to Introduction to Tools and Techniques in Computer Science. This is an
introductory lab-based course.

Every Computer Scientist needs to make use of an expansive set of modern
computing tools and techniques. This course provides a hands-on experiential
introduction to working with the tools and techniques we use every day to
design, develop, analyze, and maintain software.

Building the book
-----------------

This book was originally written with [Pandoc]'s Markdown in mind. A tool that
can use Pandoc to render something like a book is [Rippledoc]. We're using [a
fork of Rippledoc] that uses Pandoc to get metadata instead of blindly trying to
use the first line as the title.

Here's the strategy for building this book:

1. Switch to the `main` branch from whatever branch you're currently on.
2. Make changes to the Markdown files you want to make changes to.
3. Commit your changes and optionally push them to remote.
4. Switch to the `book` branch, and merge `main` into `book`:
   ```bash
   git merge main
   ```
5. Run the `rippledoc.py` to regenerate HTML sources.
6. Commit the changes and push to remote to redeploy.

[Pandoc]: https://pandoc.org
[Rippledoc]: https://gitlab.com/uvtc/rippledoc/
[a fork of Rippledoc]: https://github.com/fbristow/rippledoc
