#include <stdio.h>
#include <string.h>

char a[101];
char stack[101];
int top = 1;

int is_empty(){
    if (top-1 < 1) 
        return 1;
    return 0;
}

int is_full() {
    if (top > 101)
        return 1;
    return 0;
}

void push(char c) {
    if (is_full()) return;

    stack[top] = c;
    top++;
}

char pop() {
    int i;
    if (is_empty()) return ' ';

    top--;
    char c = stack[top];
    stack[top] = ' ';

    /*
    for (i = 1; i < top; i++) {
        printf("%c ", stack[i]);
    }
    printf("\n");
    */
    return c;
}

char top_e() {
    char c;
    c = stack[top-1];

    return c;
}

int main() {

    char c;
    int i;
    int len;
    scanf("%s", a);

    len = strlen(a);
    //printf("len=%d\n", len);

    for (i = 0; i < len; i++) {
        if (is_empty()) {
            push(a[i]);
        }
        else {
            c = top_e();
            if (a[i] == ')' && c == '(') {
                pop();
            }
            else if (a[i] == ']' && c == '[') {
                pop();
            }
            else if (a[i] == '}' && c == '{') {
                pop();
            }
            else {
                push(a[i]);
            }
        }
    }

    if (is_empty()) {
        printf("YES\n");
    }
    else {
        printf("NO\n");
    }

    return 0;
}
