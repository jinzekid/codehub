#include "c1.h"
typedef int ElemType;
#include "c1-1.h"
#include "bo1-1.c"

int main(int argc, const char *argv[]) {

    Triplet t;
    ElemType e;
    Status ret;
    
    ElemType e1, e2, e3;
    printf("Please input value:");
    scanf("%d %d %d", &e1,&e2,&e3);
    
    ret = init_triplet(&t, e1, e2, e3);
    printf("%d %d %d\n", t[0], t[1], t[2]);
    
    ret = get(t, 2, &e);
    if (ret == OK) {
        printf(">>:2 value is: %d\n", e);
    }

    ret = put(t, 2, 6);
    if (ret == OK){
        printf(">>:put 6 to 2");
        print_triplet(t);
    }

    ret = is_ascending(t);
    if (ret)
        printf(">>:Triplet is ascending\n");
    else
        printf(">>:Triplet is not ascending\n");

    ret = is_descending(t);
    if (ret)
        printf(">>:Triplet is descending\n");
    else
        printf(">>:Triplet is not descending\n");


    ret = max(t, &e);
    if (ret == OK) {
        printf(">>:max value is %d\n", e);
    }

    ret = min(t, &e);
    if (ret == OK) {
        printf(">>:min value is %d\n", e);
    }

    ret = destroy_triplet(&t);
    if (t == NULL) {
        printf(">>:t is %d\n", t);
    }


    printf(">>:func main exit...\n");
    return 0;
}
