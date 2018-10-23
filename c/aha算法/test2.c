//深度搜索, 图遍历
#include <stdio.h>

int inf = 999999;
int book[11];
// 邻接矩阵
int e[11][11];
// 
int stack[11];
int top;
int n;

void dfs(int i) {
	
	int k;
	
	if (top > n) {
		return;
	}
	
	
	// 遍历所有与i顶点相关关联的边
	for (k = 1; k <= n; k++) {
		if (e[i][k] != inf && book[k] == 0) {
			book[k] = 1;
			stack[top++] = k;
			dfs(k);
		}
	}
}

int main() {

	int u, v;
	int i, j;
	int m;
	scanf("%d %d", &n, &m);
	
	
	// 初始化邻接矩阵
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= n; j++) {
			if (i == j) e[i][j] = 0;
			else e[i][j] = inf;
		}
	}
	
	// 矩阵类型，无项图
	for (i = 1; i <= m; i++) {
		scanf("%d %d", &u, &v);
		e[u][v] = 1;
		e[v][u] = 1;
	}
	
    top = 1;
	book[1] = 1;
	stack[top++] = 1;
	dfs(1);
	
	for (i = 1; i < top; i++) {
		printf("%d ", stack[i]);
	}
	printf("\n");
	
	return 0;
}
