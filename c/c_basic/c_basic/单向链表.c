#include "commonHeader.h"

// 单向链表
typedef struct Node{
    int             data;
    struct Node*    next;
}Node, *singly_list, *pNode;

// 判断列表是否为空
bool is_empyt(singly_list list){
    if (list == NULL || list->next == NULL){
        return true;
    }
    return false;
}

// 创建新节点
pNode create_node(data) {
    
    pNode new_node = (pNode)malloc(sizeof(Node));
    if (new_node == NULL) {
        printf(">>:func insert_node err: create new node failed");
        return NULL;
    }

    new_node->data = data;
    new_node->next = NULL;

    return new_node;
}

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
    p = mylist->next;

    if (is_empyt(mylist)){
        printf(">>:func print_list err: list is empty");
        return;
    }

    printf("\n当前节点内容:\n");
    while(p != NULL) {
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
}

// 插入节点前面
int insert_node_pre(singly_list mylist, pNode anchor, pNode node){

    int ret = 0;
    pNode pre_node = NULL;
    pNode cur_node = NULL;

    if (mylist == NULL) {
        ret = -1;
        goto END;
    }

    // 如果是空链表直接添加在表头
    if (is_empyt(mylist)){
        ret = 3;
        goto END;
    }
    
    // 第一个节点找到后，就前插入列表
    pre_node = mylist;
    cur_node = mylist->next;
    if (cur_node->data == anchor->data){
        ret = 2;
        goto END;
    }

    do{
        pre_node = cur_node;
        cur_node = cur_node->next;

        if (cur_node->data == anchor->data){
            ret = 2;
            goto END;
        }
    }while(cur_node);

    // 如果没有找到要插入的节点
    if (cur_node == NULL) {
        ret = -1;
        goto END;
    }

END:
    if (ret == -1) {
        printf(">>:func insert_node_pre err: no find data");
    }
    else if (ret == -2) {
        printf(">>:func insert_node_pre err: list empty");
    }
    else if (ret == 2) {
        // 找到并t且只有一个节点
        node->next = pre_node->next;
        pre_node->next = node;
    }
    else if (ret == 3) {
        // 空链表的添加操作
        mylist->next = node;
        node->next = NULL;
    }

    return ret;
}

// 插入节点后面
int insert_node_next(singly_list mylist, pNode anchor, pNode node){
    
    int ret = 0;
    pNode pre_node = NULL;
    pNode cur_node = NULL;

    if (mylist == NULL) {
        ret = -1;
        goto END;
    }

    // 如果是空链表直接添加在表头
    if (is_empyt(mylist)){
        ret = 3;
        goto END;
    }
    
    // 第一个节点找到后，就前插入列表
    pre_node = mylist;
    cur_node = mylist->next;
    if (cur_node->data == anchor->data){
        ret = 2;
        goto END;
    }

    do{
        pre_node = cur_node;
        cur_node = cur_node->next;

        if (cur_node->data == anchor->data){
            ret = 2;
            goto END;
        }
    }while(cur_node);

    // 如果没有找到要插入的节点
    if (cur_node == NULL) {
        ret = -1;
        goto END;
    }

END:
    if (ret == -1) {
        printf(">>:func insert_node_pre err: no find data");
    }
    else if (ret == -2) {
        printf(">>:func insert_node_pre err: list empty");
    }
    else if (ret == 2) {
        // 找到并t且只有一个节点
        node->next = cur_node->next;
        cur_node->next = node;
    }
    else if (ret == 3) {
        // 空链表的添加操作
        mylist->next = node;
        node->next = NULL;
    }

    return ret;

}

// 删除节点
int remove_node(singly_list mylist, pNode del_node){

    int ret             = 0;
    pNode cur_node      = NULL;
    pNode pre_node      = NULL;

    cur_node = mylist;
    if (is_empyt(mylist)){
        printf(">>:func remove_node err: is_empyt()");
        ret = -1;
        goto END;
    }

    // 当前只有一个头节点
    // 如果相等直接删除并且返回
    if (cur_node->data == del_node->data) {
        ret = 0;
        goto END;
    }

    do {
        pre_node = cur_node;
        cur_node = cur_node->next;

        if (cur_node->data == del_node->data){
            ret = 0;
            goto END;
        }
    }while(cur_node);

    // 没有找到节点
    if (cur_node == NULL) {
        ret = -1;
        goto END;
    }
    
END:
    if (ret == -1) {
        return ret;
    }
    else if (ret == 0) {
        pre_node->next = cur_node->next;
    }

    return ret;
}

// 移动节点
int move_node_next(singly_list mylist, pNode p, pNode anchor){
    if (mylist == NULL) {
        return -1;
    }

    if (is_empyt(mylist)){
        printf(">>:func move_node_next err: empyt list");
        return -2;
    }

    // 首先删除p
    remove_node(mylist, p);
    // 然后在anchor后面添加p
    insert_node_next(mylist, anchor, p);
    return 0;
}

int move_node_pre(singly_list mylist, pNode p, pNode anchor) {
    if (mylist == NULL) {
        return -1;
    }

    if (is_empyt(mylist)){
        printf(">>:func move_node_next err: empyt list");
        return -2;
    }

    // 首先删除p
    remove_node(mylist, p);
    // 然后在anchor后面添加p
    insert_node_pre(mylist, anchor, p);
    return 0;
}

/*
int main(int argc, const char *argv[]){

    singly_list mylist = NULL;

    // 创建一个头节点
    mylist = init_list();
    
    for (int i = 1; i <= 3; i++){
        pNode new_node = create_node(i);
        if (new_node == NULL) {
            printf(">>:func insert_node err: create new node failed");
        }
        else {
            insert_node_pre(mylist, mylist->next,  new_node);
        }
    }

    pNode new_node = create_node(10);
    insert_node_pre(mylist, create_node(2), new_node);
    print_list(mylist);

    pNode new_node2 = create_node(11);
    insert_node_next(mylist, create_node(2), new_node2);
    print_list(mylist);

    pNode del_node = create_node(2);
    remove_node(mylist, del_node);
    print_list(mylist);

    move_node_next(mylist, create_node(10), create_node(1));
    print_list(mylist);

    move_node_next(mylist, create_node(3), create_node(10));
    print_list(mylist);

    move_node_pre(mylist, create_node(100), create_node(1));
    print_list(mylist);

    system("Pause");
    return 0;
}
*/
