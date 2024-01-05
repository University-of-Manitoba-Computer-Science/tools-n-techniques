#include <stdio.h>
#include <stdlib.h>

void get_input(char *);

int main(void)
{
    char *my_input = NULL;

    get_input(my_input);

    printf("Here's the input: %d on line %d\n", *my_input, __LINE__);

    return EXIT_SUCCESS;
}

void get_input(char *input)
{
    printf("Please enter some input: ");
    scanf("%s", input);
    return;
}
