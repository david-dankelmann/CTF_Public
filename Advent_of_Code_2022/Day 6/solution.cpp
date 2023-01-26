#include <iostream>
#include <fstream>
#include <string>


using namespace std;


int main() {
    std::ifstream infile("input.txt");
    std::string line;

    std::string input;
    getline(infile, input, '\0');
    
    //cout << input << std::endl;
   
    int unique_seq_counter = 0; //Length counter of unique sequence
    int min_seq_length = 4; //target unique sequence length we want to print out

    for (int i = 0; i < input.size(); i++){
        unique_seq_counter++;
        for (int t = 1; t <= min_seq_length-unique_seq_counter; t++){ //Check the next 1...min_seq_length characters for uniqueness -> as unique_seq_counter grows, we can reduce the amount of following characters to check.
            //cout << "Testing: " << input[i] << " and " << input[i+t] << endl; //Debug
            if(input[i] == input[i+t]){ //If there is a recurring character, our unique sequence broke and we have to reset the counter
                //cout << " BREAK " << endl; //Debug
                unique_seq_counter = 0;
                break;
            }
        }
        if(unique_seq_counter == min_seq_length){ //Abort if we found a sequence that suffices the min_seq_length condition
            cout << "Unique sequence detected: " << input.substr(i, min_seq_length) << " at position " << i+1 << endl;
            return 0;
        }


    }
    
}
