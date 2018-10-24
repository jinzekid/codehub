// 深度搜索 DFS
#include <stdio.h>
// 邻接矩阵
int e[101][101];
int book[101]; // 标记顶点是否记录
int inf = 999999;
int stack[101];
int top;
int n;

void dfs(int v) {

	int k;
	// 判断边界
	if (top > n) return;
	
	// 尝试每种可能性
	for (k = 1; k <= n; k++) {
		if (e[v][k] != inf && book[k] == 0) {
			book[k] = 1;
			stack[top++] = k;
			dfs(k);
		}
	}
}

int main() {
	
	int i, j;
	int m;
	int u, v;
	scanf("%d %d", &n, &m);
	
	// 初始化邻接矩阵
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= n; j++) {
			if (i == j) e[i][j] =  0;
			else e[i][j] = inf;
		}
	}
	
	// m条边, 输入每条边的权值都是1
	// 无向图的输入
	for (i = 1; i <= m; i++) {
		scanf("%d %d", &u, &v);
		e[u][v] = 1;
		e[v][u] = 1;
	}
	
	// 从1号顶点开始搜索
	top = 1;
	stack[top++] = 1;
	book[1] = 1;
	dfs(1);
	
	// 输入遍历结果
	for (i = 1; i < top; i++) {
		printf("%d ", stack[i]);
	}
	printf("\n");
	
	
	return 0;
}
