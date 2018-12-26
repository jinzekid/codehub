#include <stdio.h>

int a[101];
int n;

// 交换数据
void swap(int a[], int i, int j) {
	int t;
	
	t = a[i];
	a[i] = a[j];
	a[j] = t;
}

// 快速排序
/*
void quick_sort(int a[], int low, int high) {
	int left, right, tmp;
	if (low >= high) return;

	tmp = a[low];
	left = low;
	right = high;
	
	while (left != right) {
		
		while (a[right] >= tmp && right > left)
			right--;
		
		while (a[left] <= tmp && right > left)
			left++;
			
		if (left < right) {
			swap(a, left, right);
		}	
	}
	
	// 进行基数的交换
	swap(a, low, left);

	quick_sort(a, left+1, high);	
	quick_sort(a, low, left-1);

}
*/

void quick_sort(int a[], int low, int high) {

	if (low > high) return;

	int i, j;
	int t = a[low];

	i = low;
	j = high;
	while(i<j) {
		while (a[j]>=t && i<j)
			j--;
		
		while(a[i]<=t && i<j)
			i++;
		
		if (i<j) {
            printf("swap:i=%d,j=%d\n", i, j);
			swap(a, i, j);
		}
	}
		
	
	// 交换基数值
	swap(a , low, i);
	quick_sort(a, low, i-1);
	quick_sort(a, i+1, high);
}

int main() {

	int i;
	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	
	printf("排序前数据:\n");
	for (i = 0; i < n; i++) {
		printf("%d ",a[i]);
	}
	printf("\n");

	quick_sort(a, 0, n-1);
	printf("排序后数据(从大到小):\n");
	for (i = 0; i < n; i++) {
		printf("%d ", a[i]);
	}
	printf("\n");
	
	return 0;
}
