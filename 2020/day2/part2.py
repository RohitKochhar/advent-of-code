# For test purposes
import time
start_time = time.time()

# Create an array from our input file
a_InputLines = open('input.txt', 'r').readlines()

# Since we are dealing with a database, let's try using some OOP
class PasswordLine:
    i_Idx1    = -1
    i_Idx2    = -1
    s_Letter  = " "
    s_String  = " "
    
    def CheckValidity(self):
        if (self.s_String[self.i_Idx1] == self.s_Letter) != (self.s_String[self.i_Idx2] == self.s_Letter):
            return 1
        else:
            return 0

    def __str__(self):
        return f"{self.s_Letter} must occur at index {self.i_Idx1} xor {self.i_Idx2} in the string {self.s_String}"
    
# Create a function that creates an array of objects from the input list
def ParseInput(a_InputArray):
    o_Password = PasswordLine()
    i_ValidPasswords = 0
    for s_Line in a_InputArray:
        # First, split the string at spaces
            a_Line = s_Line.split(" ")
            # Get and store the bounds data
            a_Bounds = a_Line[0].split("-")
            # We have to subtract 1 since the elves don't have 0 indexing
            o_Password.i_Idx1 = int(a_Bounds[0]) - 1
            o_Password.i_Idx2 = int(a_Bounds[1]) - 1  
            # Get and store the letter data
            o_Password.s_Letter     = a_Line[1].replace(":", "")
            # Get and store the string data
            o_Password.s_String     = a_Line[2]
            # Check if the password is valid, and increment our count if it is
            i_ValidPasswords += o_Password.CheckValidity()
    
    return i_ValidPasswords

print(ParseInput(a_InputLines))

print(time.time() - start_time)