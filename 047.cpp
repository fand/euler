#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include "reader.hpp"


std::set<int> factor(int num, Reader<int> &r){
    
    int tmp = num;
    std::set<int> fac;
    int size = r.size();
    int d;

    printf("factor: ");
    for (int i = 0; i < size; i++) {
        d = r.at(i);
        if (tmp % d == 0) {
            printf("%d, ", d);
            fac.insert(d);
            tmp /= d;
            if (tmp == 1) {
                break;
            }
            i--;
            continue;
        }
    }
    printf("\n");
    return fac;
}

template <class T>
bool is_distinct(std::set<T> &v1, std::set<T> &v2){
    // for (int i=0; i < v1.size(); i++) {
    //     if (v2.find(v1[i]) == v2.end()) return false;
    // }
    for (std::set<int>::iterator i = v1.begin(); i != v1.end(); i++) {
        if (v2.find(*i) != v2.end()) return false;
    }
    return true;
}


int main(){

    Reader<int> r("prime_9.txt");

    int n1 = 0;
    int n2 = 0;
    std::set<int> v1, v2;
    v1 = factor(1, r);

    int count = 0;

    for (int i=2; i < 100; i++) {
        printf("i: %d, ", i);
        v2 = factor(i, r);
        if (is_distinct<int>(v2, v2, 2)) {
            count++;
            n2 = i;
        }
        if (count == 1) {
            break;
        }

        n1 = i;
        v1 = v2;
    }


    
    return 0;
}
