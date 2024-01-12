import os
import emoji
import termcolor
from tabulate import tabulate

if __name__ == "__main__":
    print(emoji.emojize("Hey! :smile:", language='alias'))
    print(emoji.emojize("Did you know you could use emojis in Python and print on the command line? :eyes:", language='alias'))
    print(emoji.emojize("It is useful for example when testing your code:"))
    print(emoji.emojize("This test passed :heavy_check_mark:", language='alias'))
    print(emoji.emojize("This test failed :heavy_multiplication_x:", language='alias'))
    print(emoji.emojize(":sparkles: Nice! :sparkles:\n", language='alias'))
    print("You can also add colors to your text:")
    print(termcolor.colored('Test passed', 'green'))
    print(termcolor.colored('Test failed', 'red'))

    print("Another great tool is to use Tabulate to print out tables.\n")

    table = [['Test', 'Status'], ['Sanity test', termcolor.colored('Passed', 'green')], ['Coverage', termcolor.colored('55%', 'yellow')]]
    print(tabulate(table, headers='firstrow', tablefmt="fancy_grid"))

    print("You can also print the table in Makdown style:\n")

    print(tabulate(table, headers='firstrow', tablefmt="grid"))
