#include <stdio.h>
#include <string.h>

// 自然数结构体，因为要保存很大的自然数1500 000 000（1.5*10^9）
// 所以使用了字符串进行保存
struct Data {
    char num[12];
};

struct Data book[200001];

// 对结构体进行交换
void swap(int i, int j){
    struct Data temp;
    
    temp = book[i];
    book[i] = book[j];
    book[j] = temp;
}

// 对大数字进行比较，字符比较
int compare_big_number(char a[], char b[]) {
    int i;
    int isSame = 0;
    if (strlen(a) > strlen(b)) return 1;

    if (strlen(a) < strlen(b)) return -1;

    for (i = 0; i < 12; i++) {
        if (a[i] > b[i]) {
            isSame = 1;
            break;
        }
        else if (a[i] < b[i]) {
            isSame = -1;
            break;
        }
    }

    return isSame;
}

// 使用快速排序对结构体中字符串数字进行比较
void quick_sort(int low, int high) {
    if (low > high) return;

    int i, j;
    char t[12];
    strcpy(t, book[low].num);

    i = low;
    j = high;
    while (i < j) {
        while (compare_big_number(book[j].num, t) >= 0 && i < j) 
            j--;

        while (compare_big_number(book[i].num, t) <= 0 && i < j) 
            i++;

        if (i < j) {
            swap(i, j);
        }
    }

    swap(low, i);
    quick_sort(low, i-1);
    quick_sort(i+1, high);
}


int main(){

    int i, j;
    int n;
    int cnt;
    scanf("%d", &n); // 输入自然数的个数

    // 输入对应的自然数数据 对于100%小于1500 000 000（1.5*10^9）
    for (i = 0; i < n; i++) {
        scanf("%s", book[i].num);
    }

    quick_sort(0, n-1);

//    printf("\n--------------------\n");
//    for (j = 0, i = 1; j < n; i++, j++) {
//        printf("%s\n", book[j].num);
//    }
//    printf("\n--------------------\n");
    
    cnt = 1;
    for (j = 0, i = 1; i < n; i++, j++) {
        if (compare_big_number(book[j].num, book[i].num) == 0) {
            cnt += 1;
        }
        else {
            printf("%s %d\n", book[j].num, cnt);
            cnt = 1;
        }

        if (i == n-1) {
            printf("%s %d\n", book[i].num, cnt);
            break;
        }
    }
    
    return 0;
}
