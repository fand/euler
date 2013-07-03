#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;


bool is_pan(string s){
    int size = s.size();
    int exist[10];
    
    for (int i=0; i < 10; i++) {
        exist[i] = 0;
    }

    for (int i=0; i < size; i++) {
        exist[stoi(s.substr(i,1))] += 1;
    }

    if (exist[0] != 0) return false;

    for (int i=1; i < size+1; i++) {
        if (exist[i] == 0) return false;
    }
    
    return true;
}


int main(){

    ifstream ifs("prime_9.txt");
    string s;

    if (!ifs){
        cout << "file doesn't exist." << endl;
        return -1;
    }

    int max = 0;
    while (ifs >> s) {
        //cout << s << endl;
//        cout << s << ": " << is_pan << ", " << stoi(s, nullptr) <<  endl;
        if (is_pan(s) && stoi(s, nullptr) > max) {
            max = stoi(s, nullptr);

        }
    }

    cout << "max num : " << max << endl;

    return 0;
}
