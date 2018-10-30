#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){

    int i, len;
    char *s;
    s = (char *)malloc(sizeof(char) * 1024);
    
    gets_s(s);

    len = strlen(s);
    printf("content:\n");
    printf("%s\n", s);

    return 0;
}
