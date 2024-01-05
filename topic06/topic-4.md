---
title: "Academic misconduct"
author: Franklin Bristow
---

Academic misconduct (or is this inappropriate help?)
===================

::: outcomes

* [X] Identify whether or not a situation is considered academic misconduct.

:::

We have looked at using version control locally (i.e., using it on the
command-line on your own computer or in your own personal folders on a shared
computer system like the ones in Aviary). This week we're going to be spending
some time looking at using version control software with your web browser using
GitHub or GitLab.

One of the things that you're going to quickly find out is that there's a lot of
source code that's published publicly on the internet. Sometimes that source
code is published (for example) as part of a programming language. You can find
[source code for the JDK] on GitHub. You can find [source code for Python] on
GitHub. You can also find source code that [implements many algorithms in a
variety of programming languages] on GitHub.

Unfortunately, just because you can find these projects publicly posted on
GitHub doesn't mean that you have been given permission to include that code in
the code you write that's being assessed as part of your university courses.

Sometimes it's a legal issue: the code that's posted on web sites like GitHub is
copyrighted by the person who wrote the code. That person may grant a broad open
source license for other people to use their code, but that doesn't grant you
permission to use that code in your own code.

Regardless of whether or not it's a legal issue, including source code that's
not your own (you did not think about the solution, then write it yourself) is
an issue of academic integrity.

::: aside

Source code is copyrighted, but may also be licensed. Some software licenses are
proprietary (you're not allowed to re-use or re-publish that source code in any
way, shape, or form unless you pay for a specific license); some software
licenses are [open source] (you're allowed to re-use or re-publish that source
code in your own projects, provided you include the license); some are [public
domain] (you're free to do whatever you want, however you want with the source
code and you're not required to include the original license).

When you are in a position of licensing your software (which you may not be
right now!), a site like [Choose an open source license] can help you decide
what kind of license you want to use when you publish your source code for the
world to use.

:::

Academic misconduct is an issue that can affect you, and one that you should
take seriously.

The learning outcome in this topic is for you to identify whether or not certain
situations would be considered academic misconduct, specifically in the context
of Computer Science and software development, so we're going to show you some
specific situations, give you a chance to think about those situations, and then
tell you about why or why not something is considered academic misconduct.

[Choose an open source license]: https://choosealicense.com/
[public domain]: https://en.wikipedia.org/wiki/Public_domain
[open source]: https://en.wikipedia.org/wiki/Open-source_software
[implements many algorithms in a variety of programming languages]:
https://github.com/TheAlgorithms
[source code for Python]: https://github.com/python/cpython
[source code for the JDK]: https://github.com/openjdk/jdk
[GitHub]: https://github.com
[GitLab]: https://gitlab.com

Situations
----------

### Situation 1

Michael and Rob are both working on their assignment for COMP 1020. Rob is
having a bit of trouble, so asks Michael if they can talk for a while on Discord
about the assignment.

Michael and Rob work together on the assignment for a while, but Michael never
shows Rob any of his code. Michael and Rob only talk about the assignment,
make general design suggestions, or suggestions on which data structures to use.

<details><summary>Have Michael and Rob committed academic misconduct?</summary>

No, Michael and Rob have not committed academic misconduct. Students are
permitted to generally discuss assignments that they are working on.

The one caveat to this situation would be if the assignment itself was to decide
on what kind of data structure to use, but if this were a general programming
assignment, discussing data structures in and of itself is not academic
misconduct.

</details>

### Situation 2

John and Franklin are both working on their assignment for COMP 2140. Franklin
is really struggling with the assignment and asks John if they can meet over
Discord. Franklin and John both talk about the assignment for a while, but John is
starting to think that Franklin is really in over his head.

John suggests that he share his code by screen sharing so that Franklin can
have a better idea about how to link together two nodes in Java. Franklin agrees
and reads John's code. Franklin then writes his own implementation.

<details><summary>Have John and Franklin committed academic
misconduct?</summary>

Yes, John and Franklin have committed academic misconduct. When John showed
Franklin his source code, even though the intent wasn't for Franklin to copy the
source code and Franklin *didn't* copy the source code, John and Franklin were
participating in [inappropriate collaboration] as soon as John showed Franklin
his source code.

[inappropriate collaboration]:
https://umanitoba.ca/student-supports/academic-supports/academic-integrity#inappropriate-collaboration

</details>


### Situation 3

Franklin and Heather are both working on their assignment for COMP 2160.
Franklin is really stuck trying to figure out how the first part of the
assignment works. He asks Heather if they can meet on Discord, but Heather is
not available to help. Instead, she e-mails Franklin her partial implementation
that includes how she set up the assignment.

<details><summary>Have Franklin and Heather committed academic
misconduct?</summary>

Yes, just like John and Franklin, Heather and Franklin are participating in
[inappropriate collaboration]. In this case, since Heather is physically sending
Franklin a file, it feels a little bit more clear than just screen sharing
because sending a file by e-mail (or as an attachment in whatever communication
tool you're using) is more tangible and permanent than screen sharing.

</details>

#### Situation 3 (a)

Franklin copies and pastes some of the code that Heather shared with him, but he
doesn't tell Heather. Franklin submits that code as part of his own assignment.

<details><summary>Have Franklin and Heather committed academic
misconduct?</summary>

Yes. In fact, even though Franklin seems to be the only one doing something
wrong here, unfortunately Heather is also guilty of academic misconduct because
they are participating in [inappropriate collaboration] together.

</details>

### Situation 4

Franklin is getting really desperate. He just can't figure out how to find the
length of an array in C. While Franklin is looking for help on the internet, he
finds some code that looks *a lot* like it's supposed to be a solution for the
assignment that he's working on, and may in fact be the sample solution provided
by the instructor in previous terms..

Franklin reads the code and it helps him figure out how to find the length of an
array in C. He doesn't copy any code.

<details><summary>Has Franklin committed academic misconduct?</summary>

Yes. Similar to our first case with John, Franklin is participating in
[inappropriate collaboration], but that seems less obvious because there's no
other person that's directly involved in participating.

That said, there is technically another person who is participating here: the
person who originally posted the sample solution on the internet. They're
*passively* involved in this misconduct, but they are involved.

</details>

#### Situation 4 (a)

Franklin copies and pastes a small fragment of the code that was in the file he
found (maybe a single function).

<details><summary>Has Franklin committed academic misconduct?</summary>

Yes, this is definitely misconduct and it's significantly clearer than the last
couple of cases because Franklin is explicitly using and submitting work that he
did not create for assessment. This is an example of [plagiarism].

[plagiarism]:
https://umanitoba.ca/student-supports/academic-supports/academic-integrity#plagiarism

</details>

#### Situation 4 (b)

Franklin submits the entire file he found with enough modifications to satisfy
the current assignment description.

<details><summary>Has Franklin committed academic misconduct?</summary>

Just like the last example, by submitting work that is not his own and he is
committing [plagiarism].

</details>

### Situation 5

Franklin managed to get the assignment done for COMP 3430 (barely), and he
handed it in at the very last second. In his rush to hand in the assignment, he
forgot to include a part of the report that was listed in the assignment
requirements section. This part of the report isn't itself essential for the
code to work, but is essential to help confirm the results/conclusions that
Franklin is writing about in the report.

<details><summary>Has Franklin committed academic misconduct?</summary>

No, Franklin has not committed academic misconduct. Franklin has not plagiarized
any work, has not collaborated inappropriately with any of his peers, and did
not commit [academic fraud] (he did not make up the results).

[academic fraud]:
https://umanitoba.ca/student-supports/academic-supports/academic-integrity#academic-fraud

</details>

<details><summary>Would Franklin be at risk of being accused of academic misconduct?</summary>

Maybe. In this specific case, Franklin appears at first glance to have committed
academic fraud, and it might be reasonable for Franklin's instructor to assume
that Franklin has committed academic fraud.

If Franklin's submission is identified as a possible case of academic misconduct
due to academic fraud, Franklin's instructor might reach out to him and ask for
clarification or for the evidence that's missing, and the issue would be
resolved.

If Franklin's instructor still believes that Franklin committed academic
misconduct, the instructor would forward the case to the Associate Head (AH) of
Computer Science for Student Experience. The AH would then act as an independent
third party in the case and conduct an investigation, including giving Franklin
an opportunity to discuss the situation. The AH would render a decision about
the situation (this is or is not a case of academic misconduct), and share that
decision with both Franklin and Franklin's instructor.

</details>

::: notes

Some additional scenarios to consider:

* Franklin's instructor has given some code in the assignment.
* Franklin's instructor has pointed Franklin at a web site that has code on it.
* Franklin posts his code on GitHub (privately).
    * Nobody finds it.
    * Somebody finds it and uses it..

:::

Further reading
---------------

You've seen some specific examples, but academic integrity is a pretty big
topic.

You can find more information about academic integrity:

* On the Computer Science Department's [Expectations for individual work in
  Computer Science page].
* On the Faculty of Science's [academic integrity page].
* On the U of M's [Student support on academic integrity page].

[Expectations for individual work in Computer Science page]:
https://sci.umanitoba.ca/cs/expectations/
[Student support on academic integrity page]:
https://umanitoba.ca/student-supports/academic-supports/academic-integrity
[academic integrity page]:
https://sci.umanitoba.ca/students/undergraduate-students/academic-integrity/
