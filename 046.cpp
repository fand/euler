#include <cstdio>
#include <cmath>
#include "reader.hpp"


int main(){

    Reader<long long int> r("prime_9.txt");

    int count = 0;
    
    for (long long int i=2; i < 1000000000; i++) {
        long long int odd = 2 * i - 1;
        bool writable = false;
        for (long long int j=0; j < i; j++) {
            long long int p = r.at(j);
            long long int remain2 = (odd - p) / 2;
            long long int rt = sqrt(remain2);
            if (rt * rt == remain2) {
//                printf("%lld = %lld + 2 * %lld^2\n", odd, p, rt);
                
                writable = true;
                break;
            }
        }
        if (!writable) {
            printf("can't write: %lld\n", odd);
            count++;
            break;
        }
    }

    printf("count: %d\n", count);
    
    return 0;
}
