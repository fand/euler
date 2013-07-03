#include <stdio.h>

class Pan{
private:
    bool *buffer;
    void clear(){
        for (int i=0; i<10; i++) {
            this->buffer[i] = false;
        }
    }
public:
    Pan(){
        this->buffer = new bool[10];
    }
    ~Pan(){
        delete[] this->buffer;
    }

    bool is_pan(int num){
        if (num >= 1000000000 || num < 100000000) return false;
        this->clear();
        int n = num;
        while (n > 0) {
            this->buffer[(n % 10)] = true;
            n /= 10;
        }

        if (this->buffer[0]) return false;
        for (int i=1; i<10; i++) {
            if (this->buffer[i] == false) return false;
        }
        return true;
    }
};


int find_pan(Pan *pan, int num){
    for (int n=2; n < 10; n++) {
        int sum = 0;
        for (int i=1; i <= n; i++) {
            int tmp = num * i;
            int r = 1;
            while (r < tmp) { r *= 10; }
            sum = sum * r + tmp;
        }
        if (pan->is_pan(sum)) {
            return sum;
        }
    }
    return 0;
}



int main(){
    Pan *p = new Pan();

    int max = 0;
    
    for (int num = 0; num < 10000; num++) {
        int tmp = find_pan(p, num);
        if (tmp > max) max = tmp;
    }

    printf("%d\n", max);
    
    delete p;

    return 0;
}


