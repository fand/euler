#include <stdio.h>

int coins[8] = {1, 2, 5, 10, 20, 50, 100, 200};

int main(){

  int count = 0;

  for (int a=0; a < 2; a++) {
    for (int b=0; b < 3; b++) {
      for (int c=0; c < 5; c++) {
        for (int d=0; d < 11; d++) {
          for (int e=0; e < 21; e++) {
            for (int f=0; f < 41; f++) {
              for (int g=0; g < 101; g++) {
                for (int h=0; h < 201; h++) {
                  if (200*a + 100*b + 50*c + 20*d + 10*e + 5*f + 2*g + h == 200) {
                    count++;
                  }
                }
              }
            }
          }
        }
      }
    }
  }

  printf("combinations: %d\n", count);

  return 0;
}
