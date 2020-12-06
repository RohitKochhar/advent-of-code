# For test purposes
import time
start_time = time.time()

a_QuestionForms   = open('input.txt','r').readlines()

class QuestionForm():
    i_Count             = -1    # This will be the count of questions answered
    a_Input             = []    # This will be the entire question set

    # We now need to know how many group members we have:
    i_NumMembers        = -1
    
    def __init__(self, a_Input, i_NumMembers):
        self.a_Input            = a_Input
        self.i_NumMembers       = i_NumMembers
        self.i_FinalAnswers     = self.RemoveUniqueAnswers()
        self.i_Count            = len(self.i_FinalAnswers)

    def RemoveUniqueAnswers(self):
        # The first intersection will be the entire first element
        s_Intersection = set(a_Input[0])
        # Then, we need to go through the rest of the list and get the following intersections
        for i_Member in range(1, self.i_NumMembers):
            s_Intersection = set(a_Input[i_Member]) & s_Intersection
        return s_Intersection

    def __str__(self):
        return f"{self.a_Input} -> {self.i_FinalAnswers} {self.i_Count} - {self.i_NumMembers}"

    

a_Input = []
i_MemberCount   = 0
i_TotalCount    = 0

for s_Line in a_QuestionForms:
    s_ProcessedLine     = s_Line.replace("\n", "")
    # If the line isn't blank, we are dealing within the same group
    if s_ProcessedLine != "":
        i_MemberCount += 1
        a_Input.append(s_ProcessedLine)
    elif s_ProcessedLine == "":
        o_QuestionForm = QuestionForm(a_Input = a_Input, i_NumMembers = i_MemberCount)
        print(o_QuestionForm)
        i_TotalCount += o_QuestionForm.i_Count
        a_Input = []
        i_MemberCount = 0

# We need to individually handle the last entry
o_QuestionForm = QuestionForm(a_Input = a_Input, i_NumMembers = i_MemberCount)
i_TotalCount += o_QuestionForm.i_Count

print(i_TotalCount)
