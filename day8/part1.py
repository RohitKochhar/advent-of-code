class Interpreter():
    def __init__(self):
        self.i_acc                  = 0
        self.i_CurrentLine          = 0
        self.a_RanInstructions      = []
        self.ReadInstuctionSet()
        self.ExecuteInstruction(self.a_InstructionSet[self.i_CurrentLine])
    
    def ReadInstuctionSet(self, a_Input=open("input.txt", "r").readlines()):
        self.a_InstructionSet   =   []
        for s_Input in a_Input:
            a_Instruction       = s_Input.replace("\n", "").split(" ")
            a_Instruction[1]    = int(a_Instruction[1])
            self.a_InstructionSet.append(a_Instruction)
        return self.a_InstructionSet

    def ExecuteInstruction(self, a_Instruction):
        self.a_RanInstructions.append(self.i_CurrentLine)
        if a_Instruction[0] == "nop":
            self.nop(a_Instruction[1])
        elif a_Instruction[0] == "jmp":
            self.jmp(a_Instruction[1])
        elif a_Instruction[0] == "acc":
            self.acc(a_Instruction[1])
        if self.HasInstructionRan() == False:
            self.ExecuteInstruction(self.a_InstructionSet[self.i_CurrentLine])

    def HasInstructionRan(self):
        for i_RanLine in self.a_RanInstructions:
            if i_RanLine == self.i_CurrentLine:
                return True
        return False

    def nop(self, arg):
        print(f"line: {self.i_CurrentLine}, acc: {self.i_acc} | nop {arg}")
        self.i_CurrentLine += 1

    def jmp(self, arg):
        print(f"line: {self.i_CurrentLine}, acc: {self.i_acc} | jmp {arg}")
        self.i_CurrentLine += arg

    def acc(self, arg):
        print(f"line: {self.i_CurrentLine}, acc: {self.i_acc} | acc {arg}")
        self.i_acc          += arg
        self.i_CurrentLine  += 1

o_Interpreter = Interpreter()