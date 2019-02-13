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
