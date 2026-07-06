#include <stdio.h>
#include <windows.h>
int main () {
    int coutd = 10;
    while (coutd >= 0)
    {
        printf("%d\n",coutd);
        coutd--;
        sleep(1)
    }
    printf("BOOM!\n");
}
