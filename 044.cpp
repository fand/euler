#include <stdio.h>
#include <math.h>

bool is_penta(long long int num){
    long long int rt = sqrt(24 * num + 1);
    if ((rt * rt) != (24 * num + 1)) { return false; }
    long long int tmp = rt + 1;
    if (tmp % 6 == 0 && tmp / 6 > 0) { return true; }
    return false;
}

long long int penta(long long int n){
    return (3*n - 1) * n / 2;
}

long long int min(long long int a, long long int b){
    if (a > b) return b;
    return a;
}


int main(){

    long long int d_min = 100000000;
    long long int l_min = 100000000;
    long long int r_min = 100000000;    
    
    long long int sa;
    long long int wa;    
    
    for (long long int i = 1; i < 10000000000; i++) {
        sa = 3*i + 1;
        wa = (sa + 1) * i + 1;

        if (is_penta(sa) && is_penta(wa)) {
            d_min = min(d_min, sa);
            l_min = penta(i);
            r_min = penta(i+1);
        }
    }
    printf("d_min: %lld\n", d_min);
    printf("l_min: %lld\n", l_min);
    printf("r_min: %lld\n", r_min);    

    
    return 0;
}
