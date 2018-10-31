/*
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
*/

#include <stdio.h>
#include <stdlib.h>

int a[10];

int *twoSum(int *nums, int numsSize, int target) {
    int i, j, num1, num2, tmp1 = 0, tmp2 = 0;
    int *p;
    int *ret;
    int flag = 0;

    ret = (int *)malloc(sizeof(int) * 2);
    if (ret == NULL) return 0;

    p = nums;
    for (i = 0; i < numsSize; i++) {
        num1 = *(p+i);
        tmp1 = i;
        for (j = i + 1; j < numsSize; j++) {
            num2 = *(p+j);
            tmp2 = j;
            if (num1 + num2 == target) {
                flag = 1;
                break;
            }
        }

        if (flag == 1) {
            break;
        }
    }

    if (flag == 1) {
        *ret = tmp1;
        *(ret+1) = tmp2;

        return ret;
    }

    return ret;
}

int main() {

    int *ret; 
    int n, i, t;
    scanf("%d %d", &n, &t);

    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    ret = twoSum(a, n, t);

    printf("[%d, %d]\n", *ret, *(ret+1));

    return 0;
}
