/*
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define MAX_BUF 10000
char *p[MAX_BUF];
char buf[20];
int cur_pos = 1;

// 压栈
int push(char* name, int len){
    if (name == NULL) {
        printf(">>:func push error: name == NULL");
        return -1;
    }
    
    if (len > 15) {
        printf(">>:func push error: len > 15");
        return -4;
    }
    
    if (cur_pos >= MAX_BUF){
        printf(">>:func push error: cur_pos >= MAX_BUF");
        return -2;
    }
    
    p[cur_pos] = (char*)malloc(len+1);
    strcpy(p[cur_pos], name);
    cur_pos++;
    return 0;
}

// 出栈
int pop(char *e){
    cur_pos--;
    if (cur_pos < 1) {
        printf(">>:func pop error: cur_pos < 1");
        return -1;
    }
    
    strcpy(e, p[cur_pos]);
    return 0;
}

// 查询
int query(int pos, char *e){
    if (pos < 1 || pos > MAX_BUF)  {
        return -1;
    }
    
    strcpy(e, p[pos]);
    return 0;
}


int main_stack(int argc, const char * argv[]) {

    int pos, n, ret = 0;
    int len = 0;
    scanf("%d", &n);
    char name[20];
    for (; n--; ) {
        int op;
        scanf("%d", &op);
        if (op == 1){
            scanf("%s", name);
            len = (int)strlen(name);
            ret = push(name, len);
            
            if (ret != 0) {
                break;
            }
        }
        else if (op == 2) {
            ret = pop(buf);
            if (ret != 0) {
                break;
            }
            printf("%s\n", buf);
        }
        else {
            scanf("%d", &pos);
            ret = query(pos, buf);
            if (ret != 0) {
                break;
            }
            printf("%s\n", buf);
        }
    }
    
    return 0;
}
*/
