#include <vector>
#include <string>
#include <memory>
#include <iostream>
#include <fstream>
#include <algorithm>


template<class T>
class Reader
{
public:
    std::vector<T> vec;
    Reader(std::string path){
        try {
            std::ifstream ifs(path);
            std::string s;

            while (ifs >> s) {
                this->vec.push_back(std::stoi(s));
            }
        } catch(std::exception& e) {
            std::cout << "file path error!" << std::endl;
        }
    }
    ~Reader(){}
    
    int size(){ return this->vec.size(); }
    
    T at(int index){ return this->vec[index]; }

    // assume that the vector is always sorted.
    int contains(T value){
        return std::binary_search(this->vec.begin(), this->vec.end(), value);
    }
};

