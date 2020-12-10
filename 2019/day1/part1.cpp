#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

class Module {
    // public is an access specifier
    public:
        int i_Mass;
        int i_Result; 
        // Constructor
        Module(string s_Line) {
            // Get the mass from the input
            i_Mass = stoi(s_Line);
            i_Result = floor(i_Mass/3)-2;
        }
};

int main(){
    // We have to load our input into a file
    ifstream f_Input;
    f_Input.open("input.txt");
    // We need a placeholder string
    string s_Line;

    // Check if we successfully opened
    if (f_Input.is_open())
    // If we are successful, store our current line in line and print
    {
        int i_Sum = 0;
        while ( getline(f_Input, s_Line) )
        {
            // Construct our object
            Module o_Module(s_Line);
            // Add our objects result to our sum
            i_Sum += o_Module.i_Result;
        }
        f_Input.close();
        cout << "Program finished with a result of " << i_Sum << endl;
    }
    // Otherwise say what happened
    else cout << "Unable to open file";
    
    return 0;
}