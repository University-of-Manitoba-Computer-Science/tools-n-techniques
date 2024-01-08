---
title: Practice Questions
author: Ikaro Costa
---

Practice Questions
==================

Question 1
----------

The following C code is supposed to calculate the sum of the first $n$ integers.
However, there are bugs in this code. Using the pencil-and-paper method, find the
bugs on this code. For example, when $n = 5$ the correct result should be $15$.
Then, start with $n=5$ and keep track of each variable in the code.

    ```C
    int sum_first_n_integers(int n)
    {
        int i = 1;
        int sum = i;
        
        while(i <= n){
            sum = sum + i;
            i = i + 1;
        }

        return sum;
    }
    ```

Question 2
----------

Another method to debug the code in the previous question would be to use a log-based
method. Recall that the C command to print to *standard output* (spoiler of one
of the next topics: [Standard Streams](https://en.wikipedia.org/wiki/Standard_streams#:~:text=std%3A%3Acin%20.-,Standard%20output%20(stdout),Not%20all%20programs%20generate%20output.))
is:

    ```C
    printf("The variable result is %d\n", var);
    ```

    This will replace the `%d` by the current value of `var` when the this line is reached.
    Rewrite the previous code including a lob-based debugging and find the bugs in the code.

Question 3
----------

Regarding debuggers, define in your own words the meaning of the following key terms:

a. Breakpoints;
b. Step in;
c. Step over;
d. Step out.
