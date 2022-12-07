#include <fstream>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;



int main() {
    ifstream infile("input.txt");
    string line;
    int curr_cal = 0, max_cal = 0;
    while (getline(infile, line)){
        line.erase(remove(line.begin(), line.end(), '\n'),line.end());
        if(line == ""){
            max_cal = max(max_cal, curr_cal);
            curr_cal = 0;
        }
        else{
            curr_cal += stoi(line);
        }
    }
    cout << max_cal << endl;
}
