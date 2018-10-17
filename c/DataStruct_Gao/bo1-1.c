// 
Status init_triplet(Triplet *T, ElemType v1, ElemType v2, ElemType v3) {

    Triplet t = NULL;
    t = (ElemType *)malloc(3*sizeof(ElemType));
    if (t == NULL)
        exit(OVERFLOW);

    t[0] = v1;
    t[1] = v2;
    t[2] = v3;

    *T = t;
    return OK;
}

Status destroy_triplet(Triplet *T){
   
    Triplet tmp = NULL;
    if (T == NULL) {
        return OK;
    }

    tmp = *T;
    free(tmp);
    *T = NULL;
    return OK;
}

Status get(Triplet T, int i, ElemType *e){
    
    if (i < 1 || i > 3) {
        return ERROR;
    }

    *e = T[i-1];
    return OK;
}

Status put(Triplet T, int i, ElemType e){
    
    if (i < 1 || i > 3) {
        return ERROR;
    }

    T[i-1] = e;
    return OK;
}

Status is_ascending(Triplet T){
    return (T[0] <= T[1] && T[1] <= T[2]);
}

Status is_descending(Triplet T){
    return (T[0] >= T[1] && T[1] >= T[2]);
}

Status max(Triplet T, ElemType *e){

    ElemType max = T[0];
    max = max>T[1]?max:T[1];
    max = max>T[2]?max:T[2];

    *e = max;
    return OK;
}

Status min(Triplet T, ElemType *e){
    
    ElemType min = T[0];
    min = min>T[1]?T[1]:min;
    min = min>T[2]?T[2]:min;

    *e = min;
    return OK;
}

void print_triplet(Triplet T) {
    printf(">>:Triplet values:%d %d %d\n", T[0], T[1], T[2]);
}


