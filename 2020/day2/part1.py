# For test purposes
import time
start_time = time.time()

# Create an array from our input file
a_InputLines = open('input.txt', 'r').readlines()

# Since we are dealing with a database, let's try using some OOP
class PasswordLine:
    i_LowerBound    = -1
    i_UpperBound    = -1
    s_Letter        = " "
    s_String        = " "
    
    def CheckValidity(self):
        i_LetterOccurances = 0
        for letter in self.s_String:
            if letter == self.s_Letter:
                i_LetterOccurances += 1
        if i_LetterOccurances >= self.i_LowerBound and i_LetterOccurances <= self.i_UpperBound: 
            return 1
        else:
            return 0

    def __str__(self):
        return f"{self.s_Letter} must occur between {self.i_LowerBound} and {self.i_UpperBound} times in the string {self.s_String}"
    


# Create a function that creates an array of objects from the input list
def ParseInput(a_InputArray):
    o_Password = PasswordLine()
    i_ValidPasswords = 0
    for s_Line in a_InputArray:
        # First, split the string at spaces
            a_Line = s_Line.split(" ")
            # Get and store the bounds data
            a_Bounds = a_Line[0].split("-")
            o_Password.i_LowerBound = int(a_Bounds[0])
            o_Password.i_UpperBound = int(a_Bounds[1])   
            # Get and store the letter data
            o_Password.s_Letter     = a_Line[1].replace(":", "")
            # Get and store the string data
            o_Password.s_String     = a_Line[2]
            # Check if the password is valid, and increment our count if it is
            if o_Password.CheckValidity() == 0:
                print(o_Password)
            i_ValidPasswords += o_Password.CheckValidity()
    
    return i_ValidPasswords

print(time.time() - start_time)