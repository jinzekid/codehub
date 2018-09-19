// 可以使用归并排序，提升速度
/*
void mergeSort(a[], low, high){
    if (low < high){
        return;
    }
    
    int i = low;
    int j = high;
    int center = (low+high)/2;
    
    mergeSort(a, center, high);
    mergeSort(a, low, center);

    merge(a, i, j); // 归并并且查找逆序对
}

void merge(int a[], int i, int j) {
    
}
*/

/*
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
 
// ================= 代码实现开始 =================
#define MAX_NUM 5000
typedef struct Stu{
    int id;
    int score_algorithm;
    int score_dataStruct;
}Stu, *pStu;
Stu students[MAX_NUM];
int cnt;

void getAnswer(int n, int *pcnt){

    int cnt = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            int score_total_i = students[i].score_algorithm + students[i].score_dataStruct;
            int score_total_j = students[j].score_algorithm + students[j].score_dataStruct;
            if ((score_total_i < score_total_j) ||
                (score_total_j == score_total_i &&
                students[i].score_algorithm < students[j].score_algorithm)) {
                cnt++;

                Stu tmp = students[j];
                students[j] = students[i];
                students[i] = tmp;
            }
        }
    }
    
    *pcnt = cnt;
}


void print_students(int n){
    for (int i = 0; i < n; i++) {
        printf("id=%d, algorithm=%d, dataStruct=%d\n", students[i].id, students[i].score_algorithm, students[i].score_dataStruct);
    }
}

// ================= 代码实现结束 =================


int main(int argc, const char * argv[]) {

    int ret = 0;
    int i, n = 0;
    int total_score = 0;
    scanf("%d", &n); // 输入学生的个数
    
    for (i = 0 ; i < n; i++) {
        students[i].id = i+1;
        scanf("%d%d", &students[i].score_algorithm, &students[i].score_dataStruct);
    }
    
    getAnswer(n, &cnt);
    for (int i = 0; i < n; i++) {
        total_score = students[i].score_algorithm + students[i].score_dataStruct;
        printf("%d %d %d %d\n", students[i].id, total_score , students[i].score_algorithm, students[i].score_dataStruct);
    }
    printf("%d\n", cnt);
    return ret;
}
*/
