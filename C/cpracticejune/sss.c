#include <stdio.h>
int main() {
    char ch;
    
    // Uncomment this! It completely destroys Code Runner's ugly command text
    printf("\033[H\033[2J"); 
    
    printf("first line ");
    ch = getchar();
    
    putchar(ch);
}