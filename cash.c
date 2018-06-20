#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float change;
    int changeRounded;
    int coinsReturned = 0;

    do
    {
        change = get_float("Change owed(in dollars): ");
    }
    while(change <= 0);


    changeRounded = change * 1000;
    changeRounded = changeRounded / 10;

    while(changeRounded % 25 < changeRounded)
    {
        changeRounded = changeRounded - 25;
        coinsReturned++;
    }

    while(changeRounded % 10 < changeRounded)
    {
        changeRounded = changeRounded - 10;
        coinsReturned++;
    }

    while(changeRounded % 5 < changeRounded)
    {
        changeRounded = changeRounded - 5;
        coinsReturned++;
    }

    while(changeRounded % 1 < changeRounded)
    {
        changeRounded = changeRounded - 1;
        coinsReturned++;
    }

    printf("coins returned: %i", coinsReturned);
    printf("\n");
}
