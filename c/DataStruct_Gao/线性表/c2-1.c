#include "../commonHeader.h"

#define OK              1
#define ERROR           0
#define LIST_INIT_SIZE  10
#define LIST_INCREMENT  2

typedef int Status;
typedef int ElemType;

typedef struct SQList{
    ElemType* data;
    int length;
    int list_size;
}SQList;

Status init_list(SQList *list, int len){
    
    ElemType* tmp = (ElemType *)malloc(sizeof(ElemType) * len);
    if (tmp == NULL) {
        return ERROR;
    }

    list->data = tmp;
    list->length = 0;
    list->list_size = len;

    printf(">>:初始化列表成功...\n");
    return OK;
}

Status clear_list(SQList *list) {
    if (list == NULL) {
        printf(">>:func desotry list err: list == NULL");
        return ERROR;
    }

    if (list->length > 0) {
        free(list->data);
    }

    list->length = 0;
    list->list_size = 0;

    printf(">>:clear list success...");
    return OK;
}


Status destory_list(SQList *list) {
    if (list == NULL) {
        printf(">>:func desotry list err: list == NULL");
        return ERROR;
    }

    if (list->length > 0) {
        free(list->data);
    }
    list->data = NULL;

    list->length = 0;
    list->list_size = 0;

    return OK;
}

Status is_empty(SQList *list) {
    if (list->length == 0){
        return true;
    }
    return false;
}

Status is_full(SQList *list) {
    if (list->length == list->list_size) {
        return true;
    }
    return false;
}

int get_list_length(SQList *list) {
    return list->length;
}

Status locate_elem_pos(SQList *list, ElemType e, int *pos){

    if (list == NULL) {
        printf(">>:func get_elem is err: list == NULL");
        return ERROR;
    }

    int i = 0;
    bool is_find = false;
    ElemType *tmp = list->data;
    for(i = 0; i < list->length; i++) {
        if (*(tmp + i) == e) {
            is_find = true;
            break;
        }
    }

    if (is_find) {
        *pos = i;
    }
    else {
        *pos = -1;
        return ERROR;
    }

    return OK;
}

Status get_elem(SQList *list, int i, ElemType *e) {
    if (i < 1 || i > list->length){
        printf(">>:func get_elem err:i >= list->length");
        return ERROR;
    }

    ElemType *tmp = list->data;
    *e = *(tmp + i - 1);

    return OK;
}

Status get_pre_elem(SQList *list, ElemType e, ElemType *pre_e) {

    int i = 0;
    ElemType *tmp = list->data;
    while(i < list->length && *(tmp+i) != e) {
        i++;
    }

    if (i == 0) {
        *pre_e = -1;
        return ERROR;
    }

    if (i < list->length) {
        *pre_e = *(tmp+i-1);
        return OK;
    }

    *pre_e = -1;
    return ERROR;
}

Status del_elem(SQList *list, int pos, ElemType *e) {
    if (pos < 1 || pos > list->length){
        return ERROR;
    }

    int i;
    ElemType *tmp = list->data;
    ElemType temp_elem = *(tmp+pos);
    for (i = pos; i< list->length; i++) {
        *(tmp+pos) = *(tmp+pos+1);
    }

    list->length--;
    *e = temp_elem;
    printf(">>:元素 %d 删除成功\n", temp_elem);
    return OK;
}

Status insert_list(SQList *list, ElemType e) {
    ElemType *tmp = NULL;
    int len = list->length;

    if (is_full(list)) {
        // 新增分配内存
        ElemType *new_base = (ElemType *)realloc(list->data, (list->list_size+LIST_INCREMENT)*sizeof(ElemType));
        if (new_base == NULL) {
            printf(">>:插入元素时候，分配新的内存失败\n");
            return ERROR;
        }

        list->data = new_base;
        list->list_size += LIST_INCREMENT;
    }
    
    tmp = list->data;
    *(tmp + len) = e;
    list->length++;
    printf(">>:元素 %d 插入列表成功!\n", e);
    return OK;
}

Status show_list(SQList *list){
    if (list == NULL) {
        printf(">>:func show list err: list is null");
        return ERROR;
    }

    if (list->length == 0) {
        printf(">>:列表为空!\n");
        return OK;
    }

    int i = 0;
    ElemType* tmp = NULL;
    tmp = list->data;
    printf("\n==============列表元素==============\n");
    for (i = 0; i< list->length; i++) {
        printf("%d ", *(tmp+i));
    }

    printf("\n");

    return OK;
}

Status list_traverse(SQList *list, void(*vi)(ElemType *e)){

    int i;
    ElemType *tmp = NULL;
    tmp = list->data;
    for (i = 0; i< list->length; i++) {
        vi((tmp+i));
    }
}

Status list_traverse3(SQList *list, ElemType(*vi)(ElemType e)){
    int i;
    ElemType *tmp = NULL;
    tmp = list->data;
    for(i = 0; i< list->length; i++) {
        *(tmp+i) = vi(*(tmp+i));
    }
}


Status list_union(SQList *la, SQList *lb) {
    
    int la_len, lb_len;
    int i;
    int pos;
    ElemType *tmp, e;
    Status ret;

    la_len = get_list_length(la);
    lb_len = get_list_length(lb);

    tmp = lb->data;
    for (i = 0; i < lb_len; i++) {
        e = *(tmp+i);
        locate_elem_pos(la , e, &pos);
        printf("e=%d, pos=%d\n", e, pos);
        if (pos == -1) {
            insert_list(la, e);
        }
    }

    return OK;
}

void quick_sort(SQList *list, int low, int high) {
    
    if (low > high) {
        return;
    }

    int i, j;
    ElemType tmp_e, c_e;
    ElemType *tmp = list->data;
    c_e = *(tmp+low);
    i = low;
    j = high;

    while(i != j) {

        while(*(tmp+j) >= c_e && i < j) {
            j--;
        }

        while(*(tmp+i) <= c_e && i < j) {
            i++;
        }

        if (i < j) {
            tmp_e = *(tmp+i);
            *(tmp+i) = *(tmp+j);
            *(tmp+j) = tmp_e;
        }
    }

    *(tmp+low) = *(tmp+i);
    *(tmp+i) = c_e;

    quick_sort(list, low, i-1);
    quick_sort(list, i+1, high);

}

void merge_list(SQList *la, SQList *lb, SQList *lc) {

    if (la == NULL || lb == NULL) {
        printf(">>:func merge_list err:la == NULL || lb == NULL");
        return;
    }

    int i, j, k;
    int len_a, len_b;
    ElemType *la_e;
    ElemType *lb_e;
    ElemType *lc_e;

    la_e = la->data;
    lb_e = lb->data;

    len_a = get_list_length(la);
    len_b = get_list_length(lb);

    init_list(lc, len_a+len_b);
    printf("list c length=%d\n", (lc->list_size));
    // sort la 
    quick_sort(la, 0, len_a-1);
    quick_sort(lb, 0, len_b-1);

    // 非递增的合并方式
    k = 0;
    i = 0;
    j = 0;
    while(i < len_a && j < len_b) {

        if (*(la_e+i) > *(lb_e+j)) {
            insert_list(lc,*(lb_e+j));
            j++;
        }
        else {
            insert_list(lc, *(la_e+i));
            i++;
        }
    }

    while (i < len_a) {
        insert_list(lc, *(la_e+i));
        i++;
    }

    while (j < len_b) {
        insert_list(lc, *(lb_e+j));
        j++;
    }

}



void db(ElemType *e) {
    *e = 2 * (*e);
}

ElemType db3(ElemType e) {
    return e * 3;
}


void print_menu() {
    printf("\n======================================\n");
    printf("1.初始化列表\n");
    printf("2.显示列表内容\n");
    printf("3.插入列表数据\n");
    printf("4.删除列表数据\n");
    printf("5.获取列表数据\n");
    printf("6.清空列表\n");
    printf("7.列表数据翻倍\n");
    printf("8.列表数据3倍\n");
    printf("9.查找前驱元素\n");
    printf("10.合并列表\n");
    printf("11.合并列表以非递减方式排列\n");
    printf("12.列表进行递增排序\n");
    printf("\n======================================\n");
}

int main(){

    int n, m, i, input_n;
    int pos;
    ElemType e, pre_e;
    SQList list;
    SQList aList, bList, cList;
    bool is_loop;
    Status ret;


    while(1){
        print_menu();
        scanf("%d", &input_n);

        switch(input_n){
            case 1:
                printf("Please input list length:");
                scanf("%d", &n);
                init_list(&list, n);
                break;
            case 2:
                show_list(&list);
                break;
            case 3:
                is_loop = true;
                while(is_loop){
                    printf(">>:请输入列表元素(q/Q:退出):");
                    scanf("%d", &e);

                    if (e == -1)
                        is_loop = false;
                    else {
                        Status ret = insert_list(&list, e);
                        if (ret == ERROR) {
                            is_loop = false;
                        }
                    }
                }
                break;
            case 4:
                while(1){
                    printf(">>:请输入要删除的元素(q/Q:退出):");
                    scanf("%d", &e);

                    if (e == -1){
                        goto END;
                    }

                    Status ret = locate_elem_pos(&list, e, &pos);
                    if (ret == OK) {
                        Status ret2 = del_elem(&list, pos, &e);
                        if (ret2 == OK) { 
                            show_list(&list);
                        }
                    }
                    else{
                        printf(">>:元素 %d 不在列表中\n", e);
                    }
                }
                break;
            case 5:
                while(1){
                    printf(">>:请输入要查询元素的位置(q/Q:退出):");
                    scanf("%d", &e);

                    if (e == -1){
                        goto END;
                    }

                    Status ret = locate_elem_pos(&list, e, &pos);
                    if (ret == OK) {
                        printf(">>:元素 %d 在列表中的位置：%d\n", e, pos);
                    }
                    else {
                        printf(">>:元素 %d 不在列表中\n", e);
                    }
                }
                break;
            case 6:
                clear_list(&list);
                break;
            case 7:
                list_traverse(&list, &db);
                break;
            case 8:
                list_traverse3(&list, &db3);
                break;
            case 9:
                while(1){
                    printf(">>:请输入要查询元素q/Q:退出):");
                    scanf("%d", &e);

                    if (e == -1){
                        goto END;
                    }

                    Status ret = get_pre_elem(&list, e, &pre_e);
                    if (ret == OK) {
                        printf(">>:元素 %d 的前驱动元素为：%d\n", e, pre_e);
                    }
                    else {
                        printf(">>:元素 %d 无前驱元素\n", e);
                    }
                }
                break;
            case 10:
                printf(">>:请初始化列表1的长度(q/Q:退出):\n");
                scanf("%d", &n);
                init_list(&aList, n);
                printf(">>:请输入列表元素\n");
                for(i = 0; i < n; i++) {
                    scanf("%d", &e);
                    insert_list(&aList, e);
                }

                printf(">>:请初始化列表2的长度(q/Q:退出):\n");
                scanf("%d", &n);
                init_list(&bList, n);
                printf(">>:请输入列表元素\n");
                for(i = 0; i < n; i++) {
                    scanf("%d", &e);
                    insert_list(&bList, e);
                }

                ret = list_union(&aList, &bList);
                if (ret == OK) {
                    list = aList;
                    printf(">>:合并列表成功\n");
                }
                break;
            case 11: 
                printf(">>:请初始化列表1的长度(q/Q:退出):\n");
                scanf("%d", &n);
                init_list(&aList, n);
                printf(">>:请输入列表元素\n");
                for(i = 0; i < n; i++) {
                    scanf("%d", &e);
                    insert_list(&aList, e);
                }

                
                printf(">>:请初始化列表2的长度(q/Q:退出):\n");
                scanf("%d", &n);
                init_list(&bList, n);
                printf(">>:请输入列表元素\n");
                for(i = 0; i < n; i++) {
                    scanf("%d", &e);
                    insert_list(&bList, e);
                }

                merge_list(&aList, &bList, &cList);
                printf(">>:排序完成\n");
                show_list(&cList);

                break;
            case 12:
                quick_sort(&list, 0, list.length-1);
                printf(">>:排序完成\n");
                show_list(&list);
                break;


        }

    END:
        printf("\n");
    }

    getchar();
    return 0;
}

