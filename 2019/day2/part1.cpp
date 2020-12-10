#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

// Class defintion --------------------------------------------
class Computer {
    public:
        int i_Position;
        string s_InstructionSet;
        Computer(string s_InstructionSet);
};

Computer::Computer(string s_InstructionSet){
    int i_Position      = 0;
    int ai_Instructions[300]; 
    cout << s_InstructionSet.length() << endl;
    for (int i=0; i < s_InstructionSet.length(); i++){
        if (s_InstructionSet[i] != ','){
            ai_Instructions[i] = 
        }
    }
}


int main(){
    // Load input file
    ifstream f_Input("input.txt");
    string s_Line;
    if (f_Input.is_open()){
        while (getline(f_Input, s_Line)){
            Computer o_Computer(s_Line);
        }
        f_Input.close();
        cout << "Program terminated successfully" << endl;
        return 0;
    }
    else cout << "Program terminated unsuccessfully" << endl;
    return 1;
}