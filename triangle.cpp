#include <stdio.h>
#include <stdlib.h>

long long int pow(int base, int power){
    long long int ans = 1;
    for (int i=0; i < power; i++) {
        ans *= base;
    }
    return ans;
}


int main(int argc, char **argv){

    if (argc != 2) {
        printf("args error!\n");
        printf("Usage: ./triangle.exe digit_length\n");
        return -1;
    }
    
    const int lim_pow = atoi(argv[1]);
    const long long int LIM = pow(10, lim_pow - 1);

    for (long long int i=1; i < LIM; i++) {
        printf("%lld\n", (i * (i +1) / 2));
    }
    return 0;
}
