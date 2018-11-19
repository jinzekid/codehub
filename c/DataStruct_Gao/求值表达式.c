#include "commonHeader.h"
#include "SequenceStack.c"

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
	    printf("z:%s\n", z);
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

    printf("请输入算术表达式，负数要用（0-正数）表示\n");
    printf("%d\n", EvaluateExpression());
    return 0;
}
