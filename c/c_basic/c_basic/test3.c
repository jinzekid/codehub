//#ifndef commonHeader_h
//#define commonHeader_h

typedef int status;
typedef int boolean;

#define TRUE    1
#define FALSE   0
#define OK      1
#define ERROR   0
#define INFEASIBLE -1

// 普通操作
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include <string.h>
#include <strings.h>
#include <time.h>
#include <errno.h>
#include <ctype.h>
#include <math.h>

// 文件与目录操作
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <dirent.h>

// 进程间通信
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/shm.h>
#include <sys/msg.h>
#include <sys/wait.h>
#include <semaphore.h>
#include <signal.h>

// 线程
#include <pthread.h>

// 网络
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>

//#endif /* commonHeader_h */

#define STACK_INIT_SIZE 10
#define STACK_INCREMENT_SIZE 5

//typedef char SElemType;
// 自定义数据类型，可以存储100位，并且记录长度
typedef struct SElemType {
    char z[100];
    int length;
}SElemType;


// 这里使用链表形式，也可以使用数组
typedef struct SeqStack {
    SElemType *top;
    SElemType *base;
    int length;
    int stackSize;
}SeqStack;

int init_stack(struct SeqStack *s) {
    SElemType *t_base = (SElemType *)malloc(STACK_INIT_SIZE*sizeof(SElemType));
    if (t_base == NULL){
        return ERROR;
    }
    
    s->top = t_base;
    s->base = t_base;
    s->stackSize = STACK_INIT_SIZE;
    s->length = 0;
    
    return OK;
}

status destory_stack(struct SeqStack *s) {
    free(s->base);
    s->base = NULL;
    s->top = NULL;
    s->stackSize = 0;
    s->length = 0;
    
    return OK;
}

status clear_stack(struct SeqStack *s) {
    s->top = s->base;
    s->length = 0;
    return OK;
}

int get_stack_length(struct SeqStack *s) {
    return s->length;
}

status stack_empty(struct SeqStack *s) {
    if (s->length == 0) {
        return TRUE;
    }
    return FALSE;
}

status get_top_elem(struct SeqStack *s, SElemType *e) {
    if (stack_empty(s)) {
        printf("栈已空\n");
        return ERROR;
    }
    
    *e = *(s->top-1);
    return OK;
}

status push(struct SeqStack *s, SElemType e) {
    if (s->length >= s->stackSize) {
        s->base = (SElemType *)realloc(s->base, (s->stackSize + STACK_INCREMENT_SIZE) * sizeof(SElemType));
        if (s->base == NULL)
            return ERROR;
        
        s->top = s->base+s->stackSize;
        s->stackSize += STACK_INIT_SIZE;
    }
    
    *s->top = e;
    s->top++;
    s->length++;
    return OK;
}

status pop(struct SeqStack *s, SElemType *e) {
    if (s->length == 0) {
        printf("栈已空\n");
        return ERROR;
    }
    
    *e = *(--s->top);
    s->length--;
    return OK;
}

void stack_traverse(struct SeqStack s, void(*visit)(SElemType)) {
    struct SeqStack tmpStack;
    tmpStack = s;
    
    while (tmpStack.top > tmpStack.base) {
        visit(*tmpStack.base++);
    }
    
    printf("\n");
    
}


#define CTI(x) (x - '0')
#define ITC(x) (x + '0')

int i, j;
char a[1000];

SeqStack seqA;
SeqStack seqB;

SeqStack OP;
SeqStack OPNR;
SeqStack sRet;

// 大数加法运算
void sum(SeqStack sa, SeqStack sb, SeqStack *pSResult) {
    int i, j;
    SElemType a, b;
    int r, gw, jw;

    jw = 0;
    while(get_stack_length(&sa) > 0 && get_stack_length(&sb) > 0) {
        pop(&sa, &a);
        pop(&sb, &b);

        r = CTI(a) + CTI(b);

        if (jw > 0) {
            r += jw;
        }

        if (r >= 10) {
            gw = r%10;
            jw = r/10;
        }
        else {
            jw = 0;
            gw = r;
        }
        push(pSResult, ITC(gw));
    }

    if (get_stack_length(&sa) > 0) {
        while (get_stack_length(&sa) > 0) {
            pop(&sa, &a);

            r = CTI(a) + jw;
            if (r >= 10) {
                gw = r%10;
                jw = r/10;
            }
            else {
                jw = 0;
                gw = r;
            }
            push(pSResult, ITC(gw));

        }
    }

    if (get_stack_length(&sb) > 0) {
        while (get_stack_length(&sb) > 0) {
            pop(&sb, &b);

            r = CTI(b) + jw;
            if (r >= 10) {
                gw = r%10;
                jw = r/10;
            }
            else {
                jw = 0;
                gw = r;
            }
            push(pSResult, ITC(gw));
        }
    }

    if (jw > 0) {
        push(pSResult, ITC(jw));
    }
}

// 大数的时候加和乘
//void calute(SeqStack sa, char x, SeqStack sb) {
//    int i, j, k;
//    char a, b;
//    int r, gw, jw;
//    SeqStack s1, s2;
//
//    SElemType *pt1, *pt2;
//
//    init_stack(&s1);
//    init_stack(&s2);
//
//    pt1 = sa.top;
//    pt2 = sb.top;
//
//    if (x == '+') {
//        sum(sa, sb, &sRet);
//    }
//    else {
//        //
//
//        for (i = 0; i < get_stack_length(&sa); i++) {
//            a = *(pt1+i);
//            jw = 0;
//            s2 = sRet;
//            clear_stack(&sRet);
//            for (j = 0; j < get_stack_length(&sb); j++) {
//                b = *(pt2+j);
//
//                r = CTI(a) * CTI(b);
//                r += jw;
//
//                if (r >= 10) {
//                    gw = r % 10;
//                    jw = r / 10;
//                }
//                else {
//                    jw = 0;
//                    gw = r;
//                }
//
//                push(&s1, ITC(r));
//            }
//
//            if (jw > 0) {
//                push(&s1, ITC(r));
//            }
//
//            // 开始移位i
//            for (k = i; k > 0; k--) {
//                push(&s1, ITC(0));
//            }
//
//            sum(s1, s2, &sRet);
//        }
//    }
//}


// 判断是否是加减符号
status in(SElemType c) {
    switch(c) {
        case '+':
        case '-':
        case '*':
        case '/':
        case '(':
        case ')':
        case '\n':return TRUE;
        default: return FALSE;
    }
}

SElemType operate(SElemType a, SElemType theta, SElemType b) {
    switch(theta) {
        case '+': return a+b;
        case '-': return a-b;
        case '*': return a*b;
    }
    return a/b;
}

char precede(SElemType t1, SElemType t2) {
    char f;
    switch(t2) {
        case '+':
        case '-':
            if (t1 == '(' || t1 == '\n')
                f = '<';
            else
                f = '>';
            break;
        case '*':
        case '/':
            if (t1 == '*' || t1 == '/' || t1 == ')')
                f = '>';
            else
                f = '<';
            break;
        case '(':
            if (t1 == ')') {
                printf("括号不匹配\n");
                exit(ERROR);
            }
            else {
                f = '<';
            }
            break;
        case ')':
            switch(t1) {
                case '(':
                    f = '=';
                    break;
                case '\n':
                    printf("缺乏左括号\n");
                    exit(ERROR);
                default: f = '>';
            }
            break;
        case '\n':
            switch(t1) {
                case '\n':
                    f = '=';
                    break;
                case '(':
                    printf("缺乏右括号\n");
                    exit(ERROR);
                default:
                    f = '>';
            }
    }
    
    return f;
}

SElemType EvaluateExpression() {
    SeqStack OPTR, OPND;
    SElemType a, b ,d, x;
    char c;
    char z[11];
    int i;
    init_stack(&OPTR);
    init_stack(&OPND);
    push(&OPTR, '\n');
    c = getchar();
    get_top_elem(&OPTR, &x);
    
    while(c != '\n' || x != '\n') {
        if (in(c)) {
            switch(precede(x, c)) {
                case '<':push(&OPTR, c);
                    c = getchar();
                    break;
                case '=':pop(&OPTR, &x);
                    c = getchar();
                    break;
                case '>':pop(&OPTR, &x);
                    pop(&OPND, &b);
                    pop(&OPND, &a);
                    push(&OPND, operate(a, x , b));
            }
        }
        else if (c >= '0' && c <= '9'){
            i = 0;
            while (c >= '0' && c <= '9') {
                z[i++] = c;
                c =getchar();
            }
            z[i] = 0;
            d = atoi(z);
            push(&OPND, d);
        }
        else {
            printf("出现非法字符\n");
            exit(ERROR);
        }
        
        get_top_elem(&OPTR, &x);
    }
    pop(&OPND, &x);
    if (!stack_empty(&OPND)) {
        printf("表达式不正确\n");
        exit(ERROR);
    }
    
    return x;
}

int main() {
    
//    printf("请输入算术表达式，负数要用（0-正数）表示\n");
    int i = 0;
    SeqStack out;
    init_stack(&out);
    SElemType k, x;
    
    int ret = EvaluateExpression();
    if (ret > 10000) {
        while (i < 4) {
            k = ret % 10;
            push(&out, k);
            ret = ret/10;
            i++;
        }
    }
    else {
        while (ret > 0) {
            k = ret % 10;
            push(&out, k);
            ret = ret/10;
            i++;
        }
    }
    
    while(i > 0) {
        pop(&out, &x);
        printf("%d",x);
        i--;
    }
    return 0;

}
