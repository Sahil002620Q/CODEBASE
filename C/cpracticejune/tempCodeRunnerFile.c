#include <stdio.h>

int main() {
    
    char str[6];

    printf("Enter your grade: ");
    fgets(str,sizeof(str),stdin); // TRAP: This won't wait for you to type!

    printf("str: %s\n",  str);
    return 0;
}