/*
堆排序
动态线性表结构
*/

#include <stdio.h>
#include <stdlib.h>

#define ERROR 0
#define OK    1

typedef int Status;
typedef int ElemType;

struct Node {
	ElemType *data;
	int lengthSize;
}Node;

void print_heap(struct Node **ppHeap) {
	printf("-----print heap-----\n");
	struct Node *tpHeap = *ppHeap;

	printf("heap length:%d\n", tpHeap->lengthSize);
	int i;
	// 打印
	ElemType *e = tpHeap->data;
	for (i = 0; i < tpHeap->lengthSize; i++) {
		printf("%d ", *(e+i));
	}
	printf("\n-------------------\n");
}

Status get_elem(struct Node *pHeap, int i, ElemType *e) {
	struct Node *tpHeap = pHeap;	
	*e = *(tpHeap->data + i);

	return OK;
}

Status swap(struct Node **ppHeap, int i, int pi) {
	struct Node *tpHeap = *ppHeap;
	ElemType *pe, t;

	pe = tpHeap->data;
	
	t = *(pe + pi);
	*(pe + pi) = *(pe + i);
	*(pe + i) = t;
	
	return OK;
}

// 向下调整
Status sift_down(struct Node **ppHeap, int n) {
	struct Node *pHeap = *ppHeap;
	ElemType e, le, re;

	int t_pos, i = 0;
	//int n = pHeap->lengthSize;

	
	// 小于最大根节点的位置
	t_pos = i;
	while(i < n/2) {
		get_elem(pHeap, i, &e);
		get_elem(pHeap, 2*i+1, &le);
		
		if (le < e) 
			t_pos = 2*i+1;
		
		if (2*i+2 < n) {
				get_elem(pHeap, t_pos, &e);
				get_elem(pHeap, 2*i+2, &re);
				if (re < e) {
					t_pos = 2*i+2;
				}
		}
		
		if (t_pos != i) {
			swap(ppHeap, t_pos, i);
			i = t_pos;
		}
		else {
			break;
		}
	}
	
	return OK;
}

// 向上调整
Status sift_up(struct Node **ppHeap) {
	struct Node *pHeap = *ppHeap;
	ElemType e, pe;
	int n = pHeap->lengthSize;
	int i = n-1;
	
	while (i > 0) {
		get_elem(pHeap, i, &e);
		get_elem(pHeap, i/2, &pe);
		printf("e=%d, pe=%d\n", e, pe);
		if (pe > e) {
			swap(ppHeap, i, i/2);
		}
		i = i/2;
	}
	
	return OK;
}

Status init_heap(struct Node **ppHeap) {
	struct Node *pNewHeap = (struct Node *)malloc(sizeof(Node));
	if (pNewHeap == NULL) return ERROR;
	
	pNewHeap->lengthSize = 0;
	pNewHeap->data = NULL;
	
	*ppHeap = pNewHeap;
	return OK;
}

Status insert_heap(struct Node **ppHeap, ElemType e) {
	struct Node *tpHeap = *ppHeap;
	int lengthSize = tpHeap->lengthSize;
	// 动态增加内存
	ElemType *pNewData = (ElemType *)realloc(tpHeap->data, (lengthSize+1)*sizeof(ElemType));
	if (pNewData == NULL) return ERROR;
	
	tpHeap->data = pNewData;
	*(tpHeap->data + lengthSize) = e;
	tpHeap->lengthSize += 1;
	
	return OK;
}

Status heap_sort(struct Node **ppHeap) {
	struct Node *pHeap = *ppHeap;
	int n = pHeap->lengthSize;
	int i;
	while (n > 0) {
		swap(ppHeap, 0, n-1);
		n--;
		sift_down(ppHeap, n);
	}
	return OK;
}

int main() {
	
	int i;
	struct Node *heap;
	ElemType *tmp;
	int n;
	ElemType e;
	scanf("%d", &n);
	
	init_heap(&heap);
	printf("heap address:%p\n", heap);
	printf("heap data:%p\n", heap->data);
	printf("heap length size:%d\n", heap->lengthSize);

	for (i = 0; i < n ; i++) {
		//scanf("%d", &e);
		// n = i，i一直在增长，直到
		//insert_heap(&heap, e);
		insert_heap(&heap, i+1);
		sift_down(&heap, heap->lengthSize);
		//sift_up(&heap);
	}
	
	heap_sort(&heap);
	printf("\n-----after heap sort-----\n");
	// 打印
	tmp = heap->data;
	for (i = 0; i < heap->lengthSize; i++) {
		printf("%d ", *(tmp+i));
	}
	printf("\n");


	return 0;
}
 

