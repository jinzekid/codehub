/*
// 类似桶排序

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

// ================= 代码实现开始 =================
typedef long long ll;

#define MAX_LEN 500000
int book[MAX_LEN] = {0};

int insert(ll x){
    
    int ret = 0;
    if (book[x] != 0) {
        // 已经在盒子中
        return -1;
    }
    
    book[x] = 1;
    return ret;
}

int delete(ll x){
    
    int ret = 0;
    if (book[x] == 0) {
        return -1;
    }
    
    book[x] = 0;
    return ret;
}




bool check(int op, ll x) {
    
    if (x > pow(10, 18))
        return false;
    
    int ret = 0;
    if (op == 1) {
        // 插入操作
        ret = insert(x);
        if (ret != 0) {
            return false;
        }
    }
    else if (op == 2) {
        // 删除操作
        ret = delete(x);
        if (ret != 0) {
            return false;
        }
    }
    else {
        printf(">>:func check error: op in {1,2}");
        return false;
    }
    
    return true;
}

// ================= 代码实现结束 =================

int main(int argc, const char * argv[]) {
    
    int a = 2;
    int b = 5;
    
    int ret = 0;
    int Q, op;
    ll x;
    scanf("%d", &Q);
    
    while (Q--) {
        scanf("%d%lld", &op, &x);
        puts(check(op, x) ? "Succeeded" : "Failed");
    }
    
    return ret;
}
 */
