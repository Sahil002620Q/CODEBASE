#include <stdio.h>
int main() {
    char ch;
    
    printf("\033[H\033[2J");
    printf("first line ");
    ch = getchar();

    putchar(ch);

}
