//
//  main.c
//  c_basic
//
//  Created by 陆杨 on 2018/8/21.
//  Copyright © 2018 陆杨. All rights reserved.
//

#include <stdio.h>

struct student {
    char name[64];
    int age;
    int id;
};
typedef struct student stu;

void print_student_info(stu student) {
    printf("----学生信息---\n");
    printf("姓名: %s\n", student.name);
    printf("年龄: %d\n", student.age);
    printf("学号: %d\n", student.id);
}

void func(int n){
    
    stu s1 = {"yang", 30, 1};
    print_student_info(s1);
    
    
    return;
}


int main2222(int argc, const char * argv[]) {
    // insert code here...
    printf("Hello, World!\n");
    
    func(10);
    return 0;
}
