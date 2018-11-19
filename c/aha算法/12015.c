#include "../DataStruct_Gao/commonHeader.h"
typedef char SElemType;
#include "../DataStruct_Gao/SequenceStack.c"

#define CTI(x) (x - '0') 
#define ITC(x) (x + '0')

int i, j;
char a[1000];

SeqStack seqA;
SeqStack seqB;

SeqStack OP;
SeqStack OPNR;
SeqStack sRet;

// 加法运算
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
void calute(SeqStack sa, char x, SeqStack sb) {
    int i, j, k;
    char a, b;
    int r, gw, jw;
    SeqStack s1, s2;

    SElemType *pt1, *pt2;

    init_stack(&s1);
    init_stack(&s2);

    pt1 = sa.top;
    pt2 = sb.top;

    if (x == '+') {
        sum(sa, sb, &sRet);
    }
    else {
        //
        
        for (i = 0; i < get_stack_length(&sa); i++) {
            a = *(pt1+i);
            jw = 0;
            s2 = sRet;
            clear_stack(&sRet);
            for (j = 0; j < get_stack_length(&sb); j++) {
                b = *(pt2+j);

                r = CTI(a) * CTI(b);
                r += jw;

                if (r >= 10) {
                    gw = r % 10;
                    jw = r / 10;
                }
                else {
                    jw = 0;
                    gw = r;
                }

                push(&s1, ITC(r));
            }

            if (jw > 0) {
                push(&s1, ITC(r));
            }

            // 开始移位i
            for (k = i; k > 0; k--) {
                push(&s1, ITC(0));
            }

            sum(s1, s2, &sRet);
        }
    }
}

void print(SElemType s) {
    printf("%d ", s);
}

int main() {

    int len;
    SElemType x;
    char c;
    i = 0;
    j = 0;
    scanf("%s", a);
    
    init_stack(&seqA);
    init_stack(&seqB);

    init_stack(&sRet);
    init_stack(&OP);
    push(&OP, '\n');
    init_stack(&OPNR);

    len = strlen(a);
    while(i < len) {
        c = a[i];
        get_top_elem(&OP, &x);

        if (x != '\n') {
            if (c >= '0' && c <= '9') {
                while(c >= '0' && c <= '9') {
                    push(&seqA, c);
                    i++;
                    c = a[i];
                }
            }
            else {
                push(&OP, c);
            }
        }
        else {
            if (c >= '0' && c <= '9') {
                while( c >= '0' && c <= '9') {
                    push(&seqB, c);
                    i++;
                    c = a[i];
                }
            }
            else {
                if (x == '-' || x == '+') {
                    if (c == '*' || c == '/') {
                        push(&OP, c);
                    }
                    else {
                        pop(&OP, &x);
                        calute(seqA, x, seqB);
                        push(&OP, c);
                    }
                }
                else {
                    pop(&OP, &x);
                    calute(seqA, x, seqB);
                    push(&OP, c);
                }
            }
        }
        i++;
    }

    stack_traverse(sRet, print);
    printf("\n");

    return 0;
}
