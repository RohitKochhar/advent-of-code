class Interpreter():
    # Constructor
    def __init__(self, a_Data=open("input.txt", "r").readlines()):
        # Initializations
        self.a_Datastream       = []    # Contains all data
        self.i_Cursor           = 0     # Tracks our current line
        self.i_PreambleEndIdx   = 25    # From question

        # Construct variables
        self.ConstructDataArray(a_Data)

        self.b_ContingousListIsFound = False

        # Go through our file and find the bad value
        self.i_BadValue = self.FindBadValue()
        # Part 1 is completed by the result of self.FindBadValue
        print(f"{self.i_BadValue} located at index {self.i_Cursor} breaks the program")

        # Mark the index
        self.i_BadIndex     = self.i_Cursor

        # Find Contigous List
        # Mark the starting and end point of our contigious list
        self.i_ListStartIdx     =   0
        self.i_ListEndIdx       =   0
        
        while self.b_ContingousListIsFound == False:
            self.FindContingousList()
            self.i_ListStartIdx += 1

        self.a_ContigousList = self.a_Datastream[self.i_ListStartIdx-1:self.i_ListEndIdx]

        print(f"Contigious list found {self.a_ContigousList}")

        i_Min = 10000000000000000
        i_Max = 0
        for i in self.a_ContigousList:
            if i < i_Min:
                i_Min = i
            if i > i_Max:
                i_Max = i


        print(f"Question Solution: {i_Min} + {i_Max} = {i_Min + i_Max}")
    

    def ConstructDataArray(self, a_Data):
        for s_Line in a_Data:
            i_Number = int(s_Line.replace("\n", ""))
            self.a_Datastream.append(i_Number)

    def FindBadValue(self):
        for self.i_Cursor in range(self.i_PreambleEndIdx, len(self.a_Datastream)):
            if self.CheckValueIsInSlidingWindow() == False:
                return self.a_Datastream[self.i_Cursor]

    def CheckValueIsInSlidingWindow(self):
        # First, get our value
        i_Value     = self.a_Datastream[self.i_Cursor]
        # then, define our sliding window
        self.a_SlidingWindow     =  self.a_Datastream[self.i_Cursor-self.i_PreambleEndIdx: self.i_Cursor]
        for idx1 in range(0, len(self.a_SlidingWindow)):
            for idx2 in range(0, idx1):
                if self.a_Datastream[self.i_Cursor] == self.a_SlidingWindow[idx1] + self.a_SlidingWindow[idx2]:
                    b_IsInSlidingWindow = True
                    return b_IsInSlidingWindow
                else:
                    b_IsInSlidingWindow = False

        return b_IsInSlidingWindow

    def FindContingousList(self):
        
        self.i_ListEndIdx = self.i_ListStartIdx

        i_Sum = 0
        print(f"{self.i_BadValue}")
        while i_Sum < self.i_BadValue:
            i_Sum += self.a_Datastream[self.i_ListEndIdx]
            self.i_ListEndIdx += 1

        self.b_ContingousListIsFound = i_Sum == self.i_BadValue

        print(f"{self.i_BadValue} {self.b_ContingousListIsFound} ")

        return self.b_ContingousListIsFound

o_Interpreter = Interpreter()
