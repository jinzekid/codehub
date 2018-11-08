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
void quick_sort(int a[], int low, int high) {

	int i;
	int left, right;
	int tmp;

	if (low >= high) return;

	tmp = a[low];
	left = low+1;
	right = high;
	
	while (left < right) {
		
		if (right > left && a[right] > tmp)
			right--;
		
		if (left < right && a[left] < tmp)
			left++;
			
		if (left != right) {
			swap(a, left, right);
		}	
	}
	
	// 进行基数的交换
	swap(a, low, left);
	
	/*
	printf("排序:%d, %d\n", low, left);
	for (i = 1; i <= n; i++) {
		printf("%d ",a[i]);
	}
	printf("\n");
	*/
	
	quick_sort(a, left+1, high);
	quick_sort(a, low, left-1);
}


int main() {

	int i;
	scanf("%d", &n);

	for (i = 1; i <= n; i++) {
		scanf("%d", &a[i]);
	}
	
	printf("排序前数据:\n");
	for (i = 1; i <= n; i++) {
		printf("%d ",a[i]);
	}
	printf("\n");

	quick_sort(a, 1, n);
	printf("排序后数据(从大到小):\n");
	for (i = 1; i <= n; i++) {
		printf("%d ", a[i]);
	}
	printf("\n");
	
	return 0;
}
