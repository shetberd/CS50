#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;

    do
        {
            height = get_int("Height: ");
        }
    while(height < 0 || height > 23);

    int spaceCount = height;
    int brickCount = height;


    for (int j = 0; j < height ; j++)
    {
        for (int i = 0; i < spaceCount - 1; i++)
        {
            printf(" ");
        }
        for (int k = height; k < brickCount + 2; k++)
        {
            printf("#");
        }
       /* for (int o = 0; o < 2; o++)
        {
            printf(" ");
        }

        for (int k = height; k < brickCount + 1; k++)
        {
            printf("#");
        }*/
        spaceCount--;
        brickCount++;
        printf("\n");
    }
}
