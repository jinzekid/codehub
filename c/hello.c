#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define DEBUG 1
#ifdef DEBUG
#define OneArgument(a) printf(a) 
#define TwoArguments(a, b) printf(a, b)
#else
#define OneArgument(a) ;
#define TwoArguments(a, b) ;
#endif

#define GetMacro(_1, _2, NAME, ...) NAME
#define PRINT(...) GetMacro(__VA_ARGS__, TwoArguments, OneArgument, ...)(__VA_ARGS__)

int array[] = {10,8,9,34,5,1,2,3,4,0};
void itoj(int a[], int i, int j) {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
      }
      
      void quick_sort(int a[], int low, int high) {
        if (low > high) return;
        
        int pi = a[low];
        int i = low;
        int j = high;
        
        while (i < j) {
          while (a[j] >= pi && i < j) j--;
          while (a[i] <= pi && i < j) i++;

          if (j > i) {
            itoj(a, i, j);
          }
       }
       
       itoj(a, low, i);
       quick_sort(a, low, i-1);
       quick_sort(a, i+1, high);
      }


int main() {
    int i;
    int len;
    len = (sizeof(array)/sizeof(array[0]));
    printf("len=%d\n", len);
    PRINT("before sort\n");
    for (i = 0; i < 10; i++){
        PRINT("%d\n", array[i]);
    }

    PRINT("after sort\n");
    quick_sort(array, 0, 9);
    for (i = 0; i < 10; i++){
        PRINT("%d\n", array[i]);
    }


    return 0;
}
