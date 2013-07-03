#include <stdio.h>



int value(int n, int a, int b){
  return n * (a + n) + b;
}

bool is_prime(int n){
  if (n < 2) return false;
  if (n == 2) return true;
  if (n == 3) return true;  

  int count = 0;
  if (n % 2 == 0) count++;
  if (n % 3 == 0) count++;
  int lim = n / 2 + 1;
  for (int i = 6; i < lim; i += 6) {
    if (n % (i-1) == 0) count++;
    if (n % (i+1) == 0) count++;
  }
  if (count == 0) return true;
  return false;
}

void test_prime(){
  printf("2: %d\n", is_prime(2));
  printf("3: %d\n", is_prime(3));
  printf("4: %d\n", is_prime(4));
  printf("5: %d\n", is_prime(5));
  printf("6: %d\n", is_prime(6));
  printf("7: %d\n", is_prime(7));  
  printf("11: %d\n", is_prime(11));
  printf("-1: %d\n", is_prime(-1));
}


int main(){
  test_prime();
  
  int maxa = 0;
  int maxb = 0;
  int maxn = 0;  
  
  for (int a = -1000; a < 1001; a++) {
    for (int b = -1000; b < 1001; b++) {

      int n = 0;
      while (true) {
        if (! is_prime(value(n, a, b))) break;
        n++;
      }
      if (n > maxn) {
        maxa = a;
        maxb = b;
        maxn = n;
        printf("a: %d, b: %d, n: %d\n", a, b, n);
      }
    }
  }

  printf("a: %d, b: %d\n", maxa, maxb);
  printf("product: %d\n", maxa * maxb);  
  return 0;
}
