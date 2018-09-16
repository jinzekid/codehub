/*
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// ================= 代码实现开始 =================
typedef struct SNode{
    int data;               // 数据域
    struct SNode *left;     // 左节点
    struct SNode *right;    // 右节点
}SNode;

#define MAX_LEN 100000

int height = 0;
SNode *rootNode = NULL;
int pos = 0;
int ans[MAX_LEN] = {0};

//创建新节点
SNode* create_node(int data) {
    
    SNode* p = (SNode *)malloc(sizeof(SNode));
    if (p == NULL) {
        printf(">>:func create_node error: p == NULL");
        return NULL;
    }
    
    p->left     = NULL;
    p->right    = NULL;
    p->data     = data;
    return p;
}

// 插入新节点
void insert(int data) {
    
    int ret = 0;
    SNode* new_node = NULL;

    if (data < 1 || data > 100000){
        printf(">>:func insert error: data < 1 || data > 100000");
        return;
    }

    if (height > 50) {
        return;
    }
    
    new_node = create_node(data);
    if (new_node == NULL) {
        printf(">>:func create_node error: new_node == NULL");
        return;
    }
    
    // 如果是空树，就直接赋值
    if (rootNode == NULL) {
        rootNode = new_node;
        height++;
        return;
    }
    else {
        SNode* tmp = rootNode;
        while (tmp) {
            if (tmp->data < data){
                // 右节点小于输入数
                if (tmp->right == NULL) {
                    tmp->right = new_node;
                    if (tmp->left == NULL)
                        height++;
                    break;
                }
                else{
                    tmp = tmp->right;
                }
            }
            else if (tmp->data > data){
                // 左节点大于输入数
                if (tmp->left == NULL){
                    tmp->left = new_node;
                    if (tmp->right == NULL)
                        height++;
                    break;
                }
                else{
                    tmp = tmp->left;
                }
            }
            else {
                // 如果相等，说明树中已经存在，不需要插入
                break;
            }
        }
    }
    
    return;
}

// 前序遍历
void DLR(SNode* pNode) {
    
    if (pNode == NULL) {
        return;
    }
    
//    printf("%d ", tmp->data);
    ans[pos++] = pNode->data;
    DLR(pNode->left);
    DLR(pNode->right);
}

// 后序遍历
void LRD(SNode* pNode) {
    
    if (pNode == NULL) {
        return;
    }
    
    LRD(pNode->left);
    LRD(pNode->right);
//    printf("%d ", tmp->data);
    ans[pos++] = pNode->data;
    
}

void getAnswer(){
    pos = 0;
    
    DLR(rootNode);
    LRD(rootNode);
}

// ================= 代码实现结束 =================


int main(int argc, const char * argv[]) {
    
    int ret = 0;
    // 2 6 9 3 5 7 10 8 4 1
    // SNode* root = NULL;// create_node(2);

    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        int x;
        scanf("%d", &x);
        insert(x);
    }
    
    getAnswer();
    
    // 前序遍历
    printf("\n前序遍历:\n");
    for (int i = 0; i < n; ++i)
        printf("%d ", ans[i]);
    printf("\n");
    
    
    // 后序遍历
    printf("\n后序遍历:\n");
    for (int i = 0; i < n; ++i)
        printf("%d ", ans[n+i]);
    printf("\n");
    
    return ret;
}
*/
