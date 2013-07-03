#include <stdio.h>
#include <string>
using namespace std;



const int divisor[7] = {2,3,5,7,11,13,17};


long long int pow(int base, int power){
    long long int ans = 1;
    for (int i=0; i < power; i++) {
        ans *= base;
    }
    return ans;
}



bool divisible(long long int num){

    long long int tmp;
    for (int i=0; i < 7; i++) {
        tmp = (num % pow(10, 9-i)) / pow(10, 6 - i);
        if (tmp % divisor[i] != 0) {
            return false;
        }
    }
    return true;
}


bool is_pan(long long int num){
    string s = to_string(num);

    int exist[10];
    
    for (int i=0; i < 10; i++) {
        exist[i] = 0;
    }

    long long int l = pow(10, 10);
    long long int r = l / 10;
    for (int i=0; i < 10; i++) {
        exist[((num % l) - (num % r)) / r] += 1;
        l /= 10;
        r /= 10;
    }

//    if (exist[0] != 0) return false;

    for (int i=0; i < 10; i++) {
        if (exist[i] != 1) return false;
    }
    
    return true;
}


int main(){

    long long int sum = 0;

//    for (long long int i=1000000001; i < 1000000001; i++) {        
//    for (long long int i=1406357285; i < 1406357292; i++) {
    for (long long int i=1000000000; i < 10000000000; i++) {
        if (divisible(i) && is_pan(i)) {
            sum += i;
            printf("%lld\n",i);
        }
    }

    printf("\nsum: %lld\n\n", sum);
    return 0;
}
