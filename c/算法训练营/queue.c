/*
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// ================= 代码实现开始 =================
typedef long long ll;

#define MAX_LENGTH 100000
char *p[MAX_LENGTH];
char buf[20];
ll head = 0;
ll tail = 0;

// 判断是否队列已满
bool is_full() {
    return head == (tail+1) % MAX_LENGTH;
}

// 判断是否队列为空
bool is_empty() {
    return head == tail;
}

// 队尾入队
// name：入队人的姓名
int enqueue(char* name, int len){
    
    char *tmp = NULL;
    tmp = name;
    int i = 0;
    // 判断是否队列已满
    if (is_full()) {
        printf(">>:func push error: head == ((tail + 1) MAX_BUF)");
        return -2;
    }
    
    if (name == NULL) {
        printf(">>:func enqueue error: name == NULL");
        return -1;
    }
    
    if (len > 15) {
        printf(">>:func enqueue error: len > 15");
        return -3;
    }
    
    i = 0;
    while (*tmp) {
        if ((*tmp < 'a' || *tmp > 'z') ||
            (*tmp == ' ' && (i > 0 && i < len-1))) {
            printf(">>:func enqueue error: *tmp < 'a' || *tmp > 'z'");
            return -4;
        }
            
        tmp++;
        i++;
    }

    p[tail] = (char*)malloc(len+1);
    strcpy(p[tail], name);
    tail = (tail+1) % MAX_LENGTH;

    return 0;
}

// 队首出队
// 返回值：队首的姓名
int dequeue(char *e){
    
    // 判断队列非空
    if (is_empty()) {
        printf(">>:func dequeue error: is_empty()");
        return -2;
    }
    
    strcpy(e, p[head]);
    head = (head+1) % MAX_LENGTH;
    return 0;
}

// 询问队列中某个位置上的人的姓名（队首位置为1，往后位置依次递增）
// pos：询问的位置
// 返回值：pos位置上人的姓名
int query(int pos, char *e){
    
    if (is_empty()) {
        printf(">>:func dequeue error: is_empty()");
        return -2;
    }
    
    if (pos < head || pos > tail) {
        printf(">>:func dequeue error: pos < head || pos >= tail");
        return -1;
    }
    
    strcpy(e, p[pos]);
    return 0;
}

// ================= 代码实现结束 =================


int main(int argc, const char * argv[]) {
    
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
            ret = enqueue(name, len);
            
            if (ret != 0) {
                ;
            }
        }
        else if (op == 2) {
            ret = dequeue(buf);
            if (ret != 0) {
                ;
            }
            printf("%s\n", buf);
        }
        else {
            scanf("%d", &pos);
            ret = query(pos, buf);
            if (ret != 0) {
                ;
            }
            printf("%s\n", buf);
        }
    }
    
    return 0;
}
*/
