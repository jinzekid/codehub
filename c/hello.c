#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Teacher {
    char name[64];
    int age;

}Teacher;

typedef struct Student{
    char name[64];
    int age;
    int id;
}Student;

int main(int argc, char** argv) {


    Student s1;
    Student *ps;
    strcpy(s1.name, "luyang");
    ps = &s1;

    printf("sizeof *ps: %d\n", sizeof(ps));

    printf("address ps: %p\n", ps);
    printf("address s1: %p\n", &s1);
    printf("add &ps: %p\n", &ps);

    printf(">>:student name: %s, address=%p\n", s1.name, &s1.name);
    printf(">>:student->name: %s, address=%p\n", ps->name, &ps->name);

    printf("Hello World!\n");
}


