/*
 使用并查集：
 判断两个元素是否属于同一集合，只需要看他们的代表元是否相同即可。

 用途：
 1、维护无向图的连通性。支持判断两个点是否在同一连通块内，和。
 2、判断增加一条边是否会产生环：用在求解最小生成树的Kruskal算法里。
 */

/*
 3 5
 3 3 1
 1 2 0
 1 2 1
 3 2 0
 1 2 1
 会有问题！！
 */


//#include <stdio.h>
//#include <stdlib.h>
//#include <string.h>
//#include <stdbool.h>
//
//// ================= 代码实现开始 =================
//#define MAX_T 100    // 数据组数
//#define MAX_M 500000 // 变量个数
//#define MAX_N 500000 // 约束条件
//
////typedef struct Node{
////    int data;
////    int rank;
////    int parent;
////}Node;
////
////Node nodes[MAX_M];
//
//int ret[MAX_N];
//
//int father[MAX_M];
//int rank[MAX_M];
//int eq[MAX_M];
//
//int A[MAX_M];
//int B[MAX_M];
//int E[MAX_M];
//
//void make_set(int x){
//    father[x]   = x;
//    rank[x]     = x;
//}
//
///**
// *查找集合i（一个元素是一个集合）的源头（递归实现）。
// 如果集合i的父亲是自己，说明自己就是源头，返回自己的标号；
// 否则查找集合i的父亲的源头。
// 寻找祖先时，我们一般采用递归查找，但是当元素很多亦或是整棵树变为一条链时，
// 每次Find_Set(x)都是O(n)的复杂度。为了避免这种情况，我们需对路径进行压缩，
// 即当我们经过”递推”找到祖先节点后，”回溯”的时候顺便将它的子孙节点都直接指向祖先，
// 这样以后再次Find_Set(x)时复杂度就变成O(1)了
// **/
//int find_set(int x) {
//    if (father[x] != x) {
//        father[x] = find_set(father[x]); // 回溯时的压缩路径是精华
//    }
//    
//    return father[x]; // 如果源头是自己就返回自己的标号
//}
//
//
///**
// 按秩合并x,y所在的集合
// 下面的那个if else结构不是绝对的，具体根据情况变化
// 但是，宗旨是不变的即，按秩合并，实时更新秩。
// **/
//void union_set(int x, int y) {
//    x = find_set(x);
//    y = find_set(y);
//    
//    if (x == y)
//        return;
//    if (rank[x] > rank[y]){
//        father[y] = x;
//    }
//    else {
//        if (rank[x] == rank[y]){
//            rank[y]++;
//        }
//        father[x] = y;
//    }
//}
//
//char* getAnswer(int n, int m, int a[], int b[], int e[]) {
//    
//    int index = 0;
//    bool* ptr = (bool *)malloc(sizeof(bool) * m);
//    bool *tmp = ptr;
//    
//    //make set
//    for (int i = 0; i < n; i++) {
//        make_set(i);
//    }
//    
//    int ev, x1, x2;
//    
//    for (int j = 0; j < m; j++) {
//        ev = e[j];
//        x1 = a[j];
//        x2 = b[j];
//        
//        if (ev == 1) {
//            if (x1 != x2) {
//                if (find_set(x1) != find_set(x2)){ // 不同根
//                    union_set(x1, x2); // 合并集合
//                    *tmp = true;
//                }
//                else{
//                    *tmp = true;
//                }
//            }
//            else{
//                *tmp = true;
//            }
//        }
//        else {
//            if (x1 == x2) {
//                *tmp = false;
//            }
//            else{
//                if (find_set(x1) == find_set(x2)){
//                    *tmp = false;
//                }
//                else{
//                    *tmp = true;
//                }
//            }
//        }
//        tmp++;
//    }
//    
//
//    // 遍历结果
//    tmp = ptr;
//    bool ret = true;
//    for (int j = 0, i = 1; j < m; i++, j++) {
//        ret &= *(tmp+j);
//    }
//    
//    return ret?"Yes":"No";
//}
//
//
//// ================= 代码实现结束 =================
//
//int main(int argc, const char * argv[]) {
//
//    int ret = 0;
//    int T;
//    for (scanf("%d", &T); T--; ) {
//        int n, m;
//        scanf("%d%d", &n, &m);
//
//        for (int i = 0; i < m; ++i) {
//            int a, b, e;
//            scanf("%d%d%d", &a, &b, &e);
//            A[i] = a;
//            B[i] = b;
//            E[i] = e;
//        }
//        printf("%s\n", getAnswer(n, m, A, B, E));
//    }
//    return 0;
//
//    return ret;
//}
