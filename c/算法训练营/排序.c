
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// ================= 代码实现开始 =================
#define MAX 500000
//int A[MAX];

int a[MAX],n;//定义全局变量，这两个变量需要在子函数中使用
void quicksort(int left,int right)
{
    int i,j,t,temp;
    if(left>right)
        return;
    
    temp=a[left]; //temp中存的就是基准数
    i=left;
    j=right;
    while(i!=j)
    {
        //顺序很重要，要先从右边开始找
        while(a[j]>=temp && i<j)
            j--;
        //再找右边的
        while(a[i]<=temp && i<j)
            i++;
        //交换两个数在数组中的位置
        if(i<j)
        {
            t=a[i];
            a[i]=a[j];
            a[j]=t;
        }
    }
    //最终将基准数归位
    a[left]=a[i];
    a[i]=temp;
    
    quicksort(left,i-1);//继续处理左边的，这里是一个递归的过程
    quicksort(i+1,right);//继续处理右边的 ，这里是一个递归的过程
}

void printArr(int a[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");

}

// ================= 代码实现结束 =================


int main(int argc, const char * argv[]) {

    int ret = 0;
    int i, num;
    
    scanf("%d", &n);
    for (i = 0 ; i < n; i++) {
        scanf("%d", &num);
        a[i] = num;
    }
    
    quicksort(0, n-1);
    printArr(a, n);

    return ret;
}

