#include <stdio.h>


void divisor(int num, int *buf, int &buf_size){
  buf_size = 0;
  int lim = num / 2 + 1;
  
  for (int i = 1; i < lim; i++) {
    if (num % i == 0) {
      buf[buf_size++] = i;
    }
  }
}

bool contain(int num, int *buf, int buf_size){
  bool ans = false;
  for (int i = 0; i < buf_size; i++) {
    if (buf[i] == num) { ans = true; }
  }
  return ans;
}
  
bool isAbundant(int num, int *buf, int buf_size){
  int sum = 0;
  for (int i = 0; i < buf_size; i++) {
    sum += buf[i];
  }
  return (sum > num) ? true : false;
}



int main(){
  
  int div[1024 * 1024];
  int a[1024 * 1024];
  int can[1024 * 1024];
  int div_size = 0;
  int a_size = 0;
  int can_size = 0;
  
  for (int i = 1; i < 28124; i++) {
    divisor(i, div, div_size);
    if (isAbundant(i), div, div_size) {
      a[a_size++] = i;
    }
    
    for (int j = 0; j < a_size; j++) {
      if (contain(i - a[j], a, a_size)) {
        can[can_size++] = i;
      }
    }
  }
  
  int sum = 0;
  for (int i = 1; i < 28124; i++) {
    if (!contain(i, can, can_size)) {
      sum += i;
    }
  }

  printf("sum = %d\n", sum);

  return 0;
}


    
