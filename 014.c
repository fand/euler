#include <stdio.h>



int main(){
  int ans = 0;
  int count_ans = 0;
  
  for (int i = 1; i < 1000000; i++) {
    long long int n = (long long int)i;
    int count = 1;
    while (n != 1) {
      if (n % 2 == 0) { n /= 2; }
      else { n = n * 3 + 1; }
      count++;
    }

    if (count > count_ans) {
      ans = i;
      count_ans = count;
    }
    if (i % 10000 == 0) printf("time: %d\n", i);
  }

  printf("%d: %d times loop.\n", ans, count_ans);

  return 0;
}
