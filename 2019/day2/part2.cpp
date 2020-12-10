#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

// Class Definition -------------------------------------------
class Module {
    // public is an access specifier
    public:
        int i_Mass;
        int i_Fuel;

        // Class methods
        Module(string s_Line);      // Constructor

        int TransferFunction(int i_x);
        int GetFuelNeededForMass(int i_InputMass);

};

Module::Module(string s_Line){
    i_Mass = stoi(s_Line);
    i_Fuel = this->GetFuelNeededForMass(i_Mass);
}

int Module::TransferFunction(int i_x){
    if ( i_x > 6 ){
        return (i_x/3)-2;
    }
    else{
        return 0;
    }
}

int Module::GetFuelNeededForMass(int i_InputMass){
        int i_FuelNeeded = this->TransferFunction(i_InputMass);
    i_InputMass += i_FuelNeeded;
    // If this is true, we don't need to do recurse 
    if (i_FuelNeeded == 0){
        return 0;
    }
    // If it isn't true, we need to find how much fuel we need again
    else {
        i_FuelNeeded += GetFuelNeededForMass(i_FuelNeeded);
    }
    return i_FuelNeeded;
}

// Main function ----------------------------------------------
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
            i_Sum += o_Module.i_Fuel;
        }
        f_Input.close();
        cout << "Program finished with a result of " << i_Sum << endl;
    }
    // Otherwise say what happened
    else cout << "Unable to open file";
    
    return 0;
}