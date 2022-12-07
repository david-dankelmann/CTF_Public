#include <fstream>
#include <string>
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;




int main() {
    vector<char> s1 = {'F', 'C', 'P', 'G', 'Q', 'R'};
    vector<char> s2 = {'W', 'T', 'C', 'P'};
    vector<char> s3 = {'B', 'H', 'P', 'M', 'C'};
    vector<char> s4 = {'L', 'T', 'Q', 'S', 'M', 'P', 'R'};
    vector<char> s5 = {'P', 'H', 'J', 'Z', 'V', 'G', 'N'};
    vector<char> s6 = {'D', 'P', 'J'};
    vector<char> s7 = {'L', 'G', 'P', 'Z', 'F', 'J', 'T', 'R'};
    vector<char> s8 = {'N', 'L', 'H', 'C', 'F', 'P', 'T', 'J'};
    vector<char> s9 = {'G', 'V', 'Z', 'Q', 'H', 'T', 'C', 'W'};

    map<string, vector<char>> stack_map = {{"1", s1}, {"2", s2}, {"3", s3}, {"4", s4}, {"5", s5}, {"6", s6}, {"7", s7}, {"8", s8}, {"9", s9}};


    ifstream infile("input.txt");
    string line;

    int amount_starting_position, amount_ending_position, source_position, target_position, amount;


    while (getline(infile, line)){
        line.erase(remove(line.begin(), line.end(), '\n'),line.end());
        

        //Find positioning of meaningful substrings
        amount_starting_position = line.find("move ") + 5;
        amount_ending_position = line.find(" from "); 
        source_position = amount_ending_position + 6;
        target_position = line.find(" to ") + 4;
        
        //Extract meaningful substrings. amount will be casted to int, source and target will be used to identify the correct stacks that should be manipulated.
        amount = stoi(line.substr(amount_starting_position, amount_ending_position));
        vector<char> &source_stack = stack_map[line.substr(source_position, 1)];
        vector<char> &target_stack = stack_map[line.substr(target_position, 1)]; 

        //Perform movement of items.
        vector<char> temp = vector<char>(source_stack.end()-amount, source_stack.end()); 
        target_stack.insert(target_stack.end(), temp.rbegin(), temp.rend());
        source_stack = vector<char>(source_stack.begin(), source_stack.end()-amount);
    }

    //Obtain result and pretty print stack information
    string res;
    for(auto const& map_entry: stack_map){ //Iterate through our stack map.
        cout << "Stack " << map_entry.first << ": ";
        for(char c: map_entry.second){ //Dump current vector.
            cout << c;
        }
        cout << endl;
        res += map_entry.second.back(); //Add last item of this stack to result
    }
    cout << "Top items: " << res << endl;
    
}
