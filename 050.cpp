#include <cstdio>
#include <cmath>
#include "reader.hpp"


int main(){

    Reader<int> r("prime_9.txt");

    int i_max = 0;
    while (r.at(i_max) < 1000000) { i_max++; }
    int val_max = r.at(i_max);

    
    std::vector<long long int> ans;
    int ans_elements = 0;
    
    printf("len: %d, r.at(i_max): %d\n", i_max, val_max);
    
    for (int i=0; i < i_max; i++) {
        if (i % 1000 == 0) { printf("i: %d\n", i); }
        long long int sum = 0;
        
        for (int j=i; j < i_max - ans_elements; j++) {
            sum += r.at(j);
            
            int ji1 = j - i + 1; 
            if (r.contains(sum) && sum < val_max && ji1 > 1) {
                if (ji1 >= ans_elements) {
                    printf("(%d 個): %lld\n", ji1, sum);
                    ans.push_back(sum);
                    ans_elements = ji1;
                }
            }
        }

    }
    
    return 0;
}
