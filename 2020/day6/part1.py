# For test purposes
import time
start_time = time.time()

a_QuestionForms   = open('input.txt','r').readlines()

class QuestionForm():
    i_Count             = -1    # This will be the count of questions answered
    s_Input             = -1    # This will be the entire question set
    s_FlattenedInput    = -1    # This will be the question set with duplicates removed
    
    def __init__(self, s_Input):
        self.s_Input = s_Input
        self.s_FlattenedInput   = set(self.s_Input)
        self.i_Count            = len(self.s_FlattenedInput)

    def __str__(self):
        return f"{self.s_Input} -> {self.s_FlattenedInput}, {self.i_Count}"

    

s_Input = ""
i_TotalCount = 0

for s_Line in a_QuestionForms:
    s_ProcessedLine     = s_Line.replace("\n", "")
    # If the line isn't blank, we are dealing within the same group
    if s_ProcessedLine != "":
        s_Input += s_ProcessedLine
    elif s_ProcessedLine == "":
        o_QuestionForm = QuestionForm(s_Input = s_Input)
        print(o_QuestionForm)
        i_TotalCount += o_QuestionForm.i_Count
        s_Input = ""

# We need to individually handle the last entry
o_QuestionForm = QuestionForm(s_Input = s_Input)
i_TotalCount += o_QuestionForm.i_Count

print(i_TotalCount)
s_Input = ""
