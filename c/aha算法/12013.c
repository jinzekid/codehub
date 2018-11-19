#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    char a[100];
    int flag = 0;
    int i, j;
    scanf("%s", a);

    int len = strlen(a);

    if (len <= 1) {
        flag = 1;
    } 
    else {
        i = 0;
        j = len - 1;
        flag = 1;
        while (i < j) {
            if (a[i] == a[j]){
                i++;j--;
            }
	    else {
		flag = 0;
            	break;
	    } 
        }
    }


    if (flag == 1) {
        printf("YES\n");
    }
    else {
        printf("NO\n");
    }

    return 0;
}
