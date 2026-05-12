#include <stdio.h>
#include <stdlib.h>

int add(const int left, const int right);

int main(void)
{
    int left, right, sum;

    printf("Let's add x+y!\n");
    printf("Enter the left side (x): ");
    scanf("%d", &left);

    printf("Enter the right side (y): ");
    scanf("%d", &right);

    printf("Thanks! Calculating...\n");
    sum = add( left, right );
    printf("The sum is %d\n", sum);
    printf("Thanks for letting me calculate for you!");

    return EXIT_SUCCESS;
}

int add(const int left, const int right)
{
    int sum;

    printf("\tAbout to add left to right.\n");
    sum = left + right;
    printf("\tHeading back to the caller.\n");

    return sum;
}
