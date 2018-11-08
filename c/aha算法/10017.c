#include <stdio.h>
#include <stdlib.h>

typedef struct Student {
    char name[64];
    int score_qm;
    int score_bp;
    char is_student_cadres;
    char is_west;
    int num_of_paper;
    int total_price;
}Student;

Student *pstudent[100];

void print_students(int n){

    int i;
    for (i = 0; i < n; i++) {
        Student* ps = pstudent[i];
        printf("%s %d %d %c %c %d %d\n", ps->name, ps->score_qm, ps->score_bp, ps->is_student_cadres, ps->is_west, ps->num_of_paper, ps->total_price);
    }
}

void check_price(int n) {

    int i;
    int max = 0;
    int idx;
    int total = 0;
    for (i = 0; i < n; i++) {
        Student *ps = pstudent[i];

        if (ps->score_qm > 80 && ps->num_of_paper >= 1) {
            ps->total_price += 8000;
        }
        if (ps->score_qm > 85 && ps->score_bp > 80) {
            ps->total_price += 4000;
        }
        if (ps->score_qm > 90) {
            ps->total_price += 2000;
        }
        if (ps->score_qm > 85 && ps->is_west == 'Y') {
            ps->total_price += 1000;
        }
        if (ps->score_bp > 80 && ps->is_student_cadres == 'Y') {
            ps->total_price += 850;
        }
    }

    Student *ps = NULL;

    for (i = 0; i < n; i++) {
        ps = pstudent[i];
        
        if (max < ps->total_price){
            max = ps->total_price;
            idx = i;
        }

        total += ps->total_price;
    }

    printf("%s\n",pstudent[idx]->name);
    printf("%d\n", max);
    printf("%d\n",total);
} 

int main(){

    int n, i;
    int max_price_stu;
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        Student *ps = (Student *)malloc(sizeof(Student));
        scanf("%s %d %d %c %c %d", ps->name, &ps->score_qm, &ps->score_bp, &ps->is_student_cadres, &ps->is_west, &ps->num_of_paper);
        ps->total_price = 0;
        pstudent[i] = ps;
    }


    
    check_price(n);

    //print_students(n);


    getchar();
    return 0;

}
