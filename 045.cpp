#include <stdio.h>

int tri(int n){
    return n*(n+1)/2;
}

int penta(int n){
    return n*(3*n - 1)/2;
}
    
int hexa(int n){
    return n*(2*n - 1);
}


int main(){
    
    int t = 285;
    int p = 165;
    int h = 143;

    t++;

    int tt = tri(t);
    int pp = penta(p);
    int hh = hexa(h);

    
    while (1) {
        if (tt == pp && tt == hh) {
            break;
        }
        
        while (tt < pp && tt < hh) {
            t++;
            tt = tri(t);
        }
        while (pp < tt && pp < hh) {
            p++;
            pp = penta(p);
        }
        while (hh < tt && hh < pp) {
            h++;
            hh = hexa(h);
        }
    }
    
    printf("tt: %d\n", tt);
    
    return 0;
}
