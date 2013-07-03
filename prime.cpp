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
        printf("Usage: ./prime.exe digit_length\n");        
        return -1;
    }
    
    const int lim_pow = atoi(argv[1]);
    const long long int LIM = pow(10, lim_pow - 1);

//    printf("LIM: %lld\n", LIM);
    
    long long int primes[LIM];
    long long int num_primes = 0;
    

    primes[0] = 2;
    primes[1] = 3;
    num_primes = 2;
    
    for (long long int i=6; i < LIM; i += 6) {
        long long int l = i - 1;
        long long int r = i + 1;        
        bool lp = true;
        bool rp = true;
        
        for (int j=0; j < num_primes; j++) {
            int p =  primes[j];
            if (p * p > r) break;
            if (l % p == 0) lp = false;
            if (r % p == 0) rp = false;
            if ((lp | rp) == false) break;
        }
        
        if (lp) primes[num_primes++] = l;
        if (rp) primes[num_primes++] = r;        
    }

    for (int i=0; i < num_primes; i++) {
        printf("%lld\n", primes[i]);
    }

    return 0;
}
