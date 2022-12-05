#include <fstream>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

bool is_contained(string p1, string p2){
    
    int p1_start = stoi(p1.substr(0, p1.find("-")));
    int p1_end = stoi(p1.substr(p1.find("-")+1, p1.size()));
    int p2_start = stoi(p2.substr(0, p2.find("-")));
    int p2_end = stoi(p2.substr(p2.find("-")+1, p2.size()));

    if(p2_start >= p1_start && p2_end <= p1_end){
        return true;
    }
    else if(p1_start >= p2_start && p1_end <= p2_end){
        return true;
    }
    else{
        return false;
    }
}

int main() {
    ifstream infile("input.txt");
    string line;
    int res = 0;
    while (getline(infile, line)){
        line.erase(remove(line.begin(), line.end(), '\n'),line.end());
        int split_position = line.find(",");
        string p1 = line.substr(0, split_position);
        string p2 = line.substr(split_position+1, line.size());
        if(is_contained(p1, p2)){
            res += 1;
        }
    }
    cout << res << endl;
}
