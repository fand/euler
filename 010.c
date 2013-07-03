#include <stdio.h>


int main(){

  int primes[1000000];
  primes[0] = 2;
  primes[1] = 3;
  int num_primes = 2;
 
  int i = 6;

  while (i <= 2000000) {
    int l = i-1;
    int r = i+1;
    bool lp = true;    
    bool rp = true;

    for (int j = 0; j < num_primes; j++) {
      if (l % primes[j] == 0) { lp = false; }
      if (r % primes[j] == 0) { rp = false; }
    }
    
    if (lp) {
      primes[num_primes++] = l;
    }
    if (rp) {
      primes[num_primes++] = r;
    }

    i += 6;
  }

  long long int sum = 0;
  for (int j = 0; j < num_primes; j++) {
    sum += (long long int)primes[j];
  }


  printf("sum in %lld.\n", sum);

  return 0;
}
