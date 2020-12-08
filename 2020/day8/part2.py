import time

class Interpreter():
    def __init__(self):
        # Set the input file
        self.s_InputFile            = "input.txt"
        # Set the current line number to 0
        self.i_CurrentLine          = 0
        # Create a dictionary object with key-pair values of line number and instruction
        self.generateFileDictionary()
        # Set the accumulation variable
        self.i_acc                  = 0
        # Default
        self.b_TerminatedSuccessfully = False

    def generateFileDictionary(self):
        # Create a blank dictionary object
        self.d_File = {}
        # Parse the input and fill this out
        for s_Instruction in open(self.s_InputFile, "r").readlines():
            a_Instruction       = s_Instruction.replace("\n", "").split(" ")
            a_Instruction[1]    = int(a_Instruction[1])
            self.d_File[self.i_CurrentLine]     = a_Instruction
            self.i_CurrentLine  += 1
        # Reset the current line
        self.i_CurrentLine = 0

    def ExecuteInstruction(self):
        if self.i_CurrentLine >= len(self.d_File):
            print("EOF reached, terminating successfully")
            self.b_TerminatedSuccessfully = True
            return
        # Otherwise:
        a_Instruction = self.d_File[self.i_CurrentLine]
        print(f"{self.i_CurrentLine}, acc: {self.i_acc}: {a_Instruction}")
        # Execute the right function for each case
        if a_Instruction[0] == "nop":
            self.nop(a_Instruction[1])
        elif a_Instruction[0] == "jmp":
            self.jmp(a_Instruction[1])
        elif a_Instruction[0] == "acc":
            self.acc(a_Instruction[1])

        # Try to recurse further 
        try:
            self.ExecuteInstruction()
            return
        except RecursionError as re:
            print("EOF never reached, terminating unsuccessfully")
            self.b_TerminatedSuccessfully = False
            return

    def Tweak(self, i_Row):
        # This function swaps jmp and nop
        if self.d_File[i_Row][0] == "nop":
            self.d_File[i_Row][0] = "jmp"
            self.ExecuteInstruction()

        if self.d_File[i_Row][0] == "jmp":
            self.d_File[i_Row][0] = "nop"
            self.ExecuteInstruction()

    def nop(self, arg):
        self.i_CurrentLine += 1

    def jmp(self, arg):
        self.i_CurrentLine += arg

    def acc(self, arg):
        self.i_acc          += arg
        self.i_CurrentLine  += 1

# Try the original instruciton set
o_Interpreter = Interpreter()
o_Interpreter.ExecuteInstruction()

# If it fails, try and automatically debug it
i_Row = 0
while o_Interpreter.b_TerminatedSuccessfully == False:
    # If we are here, we have to start over and try new instructions
    o_Interpreter = Interpreter()

    # The tweak function will replace the variables and run the new function
    o_Interpreter.Tweak(i_Row)

    if o_Interpreter.b_TerminatedSuccessfully == False:
        # If we are here, the tweak did not work, so we untweak
        i_Row += 1
    
    else:
        print("Fixed")
        break



    
    
