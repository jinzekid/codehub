#include <stdio.h>
#include <stdlib.h>

int numOfBook, numOfReader;
int a[10000000];
int ret[1000];
int idx = 0;

void swap(int x, int y) {
    int tmp;
    tmp = a[x];
    a[x] = a[y];
    a[y] = tmp;
}

void quick_sort(int low, int high) {
    int i, j;

    if (low >= high) return;
    
    int data = a[low];
    i = low+1;
    j = high;

    while (i < j) {
        while(i < j && data < a[j]) {
            j--;
        }

        while (i < j && data > a[i]) {
            i++;
        }

        if (i != j) {
            swap(i, j);
        }
    }

    swap(low, i);

    quick_sort(low, i-1);
    quick_sort(i+1, high);
}

void check_book(int len, int n) {
    int i;
    int yu;
    int isFind = -1;
    int tmpLen = len;
    int yuNum;
    // check book num 
    for (i = 0; i < numOfBook; i++) {
        yu = a[i] - n;
        if (yu == 0) {
            isFind = i;
            break;
        }
        else if (yu < 0) 
            continue;

        while(1) {
            yuNum = yu%10;
            if (yuNum == 0) {
                tmpLen--;
                yu /= 10;
            }
            else {
                break;
            }

            if (tmpLen == 0) {
                isFind = i;
                break;
            }
        }

        if (isFind != -1) {
            break;
        }
    }

    if (isFind == -1)
        ret[idx++] = -1;
    else
        ret[idx++] = a[isFind];
}


int main() {

    int i;
    int len, n;
    idx = 0;
    scanf("%d %d", &numOfBook, &numOfReader);

    for (i = 0; i <numOfBook; i++) {
        scanf("%d", &a[i]);
    }

    quick_sort(0, numOfBook-1);
    printf("\n---after sorted---\n");
    for(i = 0; i < numOfBook; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");

    for (i = 0; i < numOfReader; i++) {
        scanf("%d %d", &len, &n);
        check_book(len, n);
    }

    printf("\n---output---\n");
    for(i = 0; i < numOfReader;i++) {
        printf("%d\n", ret[i]);
    }

    return 0;
}
