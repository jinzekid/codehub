#include "commonHeader.h"

// 单向链表
typedef struct Node{
    datatype        data;
    struct node*    next;
}Node, *singly_list, *pNode;

// 初始化空链表
singly_list init_list(void){
    singly_list mylist = (pNode)malloc(sizeof(Node));

    if (mylist != NULL) {
        mylist->next = NULL;
    }

    return mylist;
}

// 打印列表
void print_list(singly_list mylist){
    
    pNode p = NULL;
    p = mylist;

    if (is_empyt(mylist)){
        printf(">>:func print_list err: list is empty");
        return;
    }

    while(p) {
        print(">>:data %d\n", p->data);
        p = p->next;
    }
}

// 插入节点
void insert_node(singly_list p, pNode new){

    if (p == NULL || new == NULL) {
        return;
    }

    new->next = p->next;
    p-next = new;
}

// 删除节点
int remove_node(singly_list mylist, int data, pNode *del_node){

    int ret             = 0;
    pNode del_node      = NULL;
    pNode cur_node      = NULL;
    pNode pre_node      = NULL;

    cur_node = mylist;
    if (is_empyt(mylist)){
        print(">>:func remove_node err: is_empyt()");
        ret = -1;
        goto END;
    }

    // 当前只有一个头节点
    // 如果相等直接删除并且返回
    if (cur_node->data == data) {
        ret = 0;
        goto END;
    }

    do {
        pre_node = cur_node;
        cur_node = cur_node->next;

        if (cur_node->data == data){
            ret = 0
            goto END;
        }
    }while(cur_node);

    // 没有找到节点
    if (cur_node == NULL) {
        ret -1;
        goto END;
    }
    
END:
    if (ret == -1) {
        return ret;
    }
    else if (ret == 0) {
        pre_node->next = cur_node->next;
        *del_node = cur_node;
    }

    return ret;
}

int main(int argc, const char *argv[]){

    singly_list mylist = NULL;


    mylist = init_list();
    for (int i =0;i < 10; i++){
        insert_node(mylist, i);
    }
    print_list(mylist);
    print("\n");

    system("pause");
    return 0;
}
