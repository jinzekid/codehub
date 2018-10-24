#include <stdio.h>
int h[101];
int n;

void swap(int a, int b) {
	int t;
	
	t = h[a];
	h[a] = h[b];
	h[b] = t;
}

// 堆结构
// 向下调整
void sift_down(int i, int n){
	int t;
	int flag = 0;
	
	while (i <= n/2 && flag == 0) {
		if (h[i] > h[i*2]){
			t = i*2;
		}
		else {
			t = i;
		}
		
		if (2*i+1 <= n) {
			if (h[t] > h[i*2+1]){
				t = i*2+1;
			}
		}
		
		if (t != i) {
			swap(t, i);
			i = t;
		}
		else {
			flag = 1;
		}
	}
}

// 向上调整
void sift_up(int i) {

	int t;
	int flag = 0;
	if (i == 1) return;
	
	while (i > 1 && flag == 0) {
		if (h[i] < h[i/2]) {
			i = i/2;
			sift_up(t);
		}
		else {
			flag = 1;
		}
	}
}

// 创建最小堆
void create_heap(int n) {
 	int i;
 	// 从最后一个根结点开始，向下调整
	for (i = n/2; i >=1; i--) {
		sift_down(i, n);
	}
}

void heap_sort(int n) {
	int k;
	while(n > 1) {
		swap(1, n);
		n--;
		sift_down(1, n);
		
		printf("\n调整过后的堆:\n");
		for (k = 1; k <= n; k++) {
			printf("%d ", h[k]);
		}
		printf("\n");
	}
}

int main() {
	int i;
	int v;
	// 输入n个数
	scanf("%d", &n);
	
	for (i = 1; i <= n; i++) {
		scanf("%d", &h[i]);
	}
	printf("排序前数据:\n");
	for (i = 1; i <= n; i++) {
		printf("%d ",h[i]);
	}
	printf("\n");
	
	create_heap(n);
	printf("创建最小堆结构:\n");
	for (i = 1; i <= n; i++) {
		printf("%d ", h[i]);
	}
	printf("\n");

	heap_sort(n);
	printf("排序后数据(从大到小):\n");
	for (i = 1; i <= n; i++) {
		printf("%d ", h[i]);
	}
	printf("\n");

	return 0;
}
