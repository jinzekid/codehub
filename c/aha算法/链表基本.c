#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
    int data;
    struct node* next;
}node;


void insert_node(node** list, node *e) {
   node *tmp = NULL; 
   node *pre = NULL;
   if (list == NULL || e == NULL) {
       return;
   }

   tmp = *list;
   pre = *list;
   printf(">>:first node data:%d\n", tmp->data);

   if (tmp->data > e->data) {
       e->next = pre;
       *list = e;
       return;
   }


   while(tmp && tmp->data < e->data) {
       pre = tmp;
       tmp = tmp->next;
   }
   
   e->next = pre->next;
   pre->next = e;
}

void print_link(node* list) {
    node *p;
    p = list;

    while (p) {
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
}

void create_node(int data, node **new_node) {

    node *p;
    p = (node *)malloc(sizeof(node));
    if (p == NULL) {
        return;
    }
    p->data = data;
    p->next = NULL;

    *new_node = p;
}


int main(){


    node *head, *p, *q, *t;
    int i, n, a;

    scanf("%d", &n);
    head = NULL;

    for(i = 1; i <= n; i++){
        scanf("%d", &a);
        create_node(a, &p);
        if (p == NULL) {
            return -1;
        }

        if (head == NULL) {
            head = p;
        }
        else {
            q->next = p;
        }

        q = p;
    }

    t = head;
    print_link(head);

    printf(">>:Input new node:");
    scanf("%d", &a);
    create_node(a, &p);
    insert_node(&head, p);

    print_link(head);

    return 0;
}
