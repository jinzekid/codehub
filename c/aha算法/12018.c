#include <stdio.h>

#define MAX 100001
int stack[100001];
int top = 1;
int n;

int is_empty() {
    if (top - 1 < 1) {
        return 1;
    }
    return 0;
}

int is_full() {
    if (top > MAX) 
        return 1;

    return 0;
}

int pop() {
    int v;
    if (is_empty()) {
        return;
    }

    top -= 1;
    v = stack[top];
    stack[top] = 0;
    return v;
 }

void push(int i){

    int k;
    if (is_full()) return;

    stack[top] = i;
    top++;

    /*
    printf("\n============\n");
    for (k = 1; k < top; k++) {
        printf("%d ", stack[k]);
    }
    printf("\n");
    */
}

int main(){
    
    int i;
    int t;
    char c;
    scanf("%d", &n);

    for (i = 1; i <= n; i++) {
        scanf(" %c", &c);
        
        if (c == 'I') {
            scanf("%d", &t);
            push(t);
        }
        else if (c == 'O'){
            int v = pop();
            //printf("pop value:%d\n", v);
        }
    }

    for (i = 1; i < top; i++) {
        printf("%d ", stack[i]);
    }

    printf("\n");
    return 0;
}
