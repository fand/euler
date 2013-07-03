#include <stdio.h>

int divisors(long long int num){
  long long int lim = num/2 + 1;
  int count = 0;
  for (long long int i = 1; i < lim; i++) {
    if (num % i == 0) count++;
  }
  return count;
}

int main(){
  long long int t = 0;
  int count = 1;

  int num_div = 0;

  while (1) {
    t += (long long int)count++;
    if (divisors(t) > 500) { break; }
  }

  printf("triangle number: %lld\n", t);
  
  return 0;
}


