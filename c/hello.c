#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define DEBUG 1
#ifdef DEBUG
#define OneArgument(a) printf(a) 
#define TwoArguments(a, b) printf(a, b)
#else
#define OneArgument(a) ;
#define TwoArguments(a, b) ;
#endif

 
#define GetMacro(_1, _2, NAME, ...) NAME
#define PRINT(...) GetMacro(__VA_ARGS__, TwoArguments, OneArgument, ...)(__VA_ARGS__)


int main() {
    int array[5] = {1,2,3,4,0};
    int i;
    PRINT("before sort\n");
    for (i = 0; i < 5; i++){
        PRINT("%d\n", array[i]);
    }
    
    return 0;
}
