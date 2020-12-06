# For test purposes
import time
start_time = time.time()

a_Tickets   = open('input.txt','r').readlines()
i_NumRows   = 127

class Ticket():
    s_String    = ""
    i_Row       = ""
    def __init__(self, s_String):
        self.s_String    =  s_String
    
    def getRowNumber(self):
        # We have to iterate through the first seven rows
        i_MinRow    = 0
        i_MaxRow    = 127
        for s_Char in self.s_String[:-3]:
            # First, get the middle number between the two:
            i_Median = int((i_MinRow + i_MaxRow) / 2)
            # The upper bound becomes the median if F
            if s_Char == "F":
                i_MinRow = i_MinRow
                i_MaxRow = i_Median
            elif s_Char == "B":
                # The lower bound becomes the median if B
                i_MinRow = i_Median + 1
                i_MaxRow = i_MaxRow
            if i_MaxRow == i_MinRow:
                self.i_Row  =   i_MaxRow
                return self.i_Row
    
    def getSeatNumber(self):
        # We have to iterate through the last 3 entries
        i_MinSeat   = 0
        i_MaxSeat   = 7
        for s_Char in self.s_String[-3:]:
            # First, get the median
            i_Median = int((i_MinSeat+i_MaxSeat)/2)
            if s_Char == "L":
                # If L, upper bound = median
                i_MinSeat   = i_MinSeat
                i_MaxSeat   = i_Median
            elif s_Char == "R":
                # If R, lower bound = median
                i_MinSeat   = i_Median + 1
                i_MaxSeat   = i_MaxSeat
            if i_MinSeat == i_MaxSeat:
                self.i_Seat = i_MinSeat
                return self.i_Seat
                

    def getTicketId(self):
        return self.getRowNumber() * 8 + self.getSeatNumber()

    def getPosition(self):
        return f"Row: {self.getRowNumber()}, Seat: {self.getSeatNumber()}"
    def __str__(self):
        return f"Ticket Label: {self.s_String}"

# make a quicksort algorithm
def Quicksort(a_Unsorted):
    # Define some empty arrays to sort our values
    a_Less    = []
    a_Equal   = []
    a_Greater = []
    # If the length is larger than one, we are not done
    if len(a_Unsorted) > 1:
        # We need to define a number to compare the others to
        i_Pivot = int(a_Unsorted[0])
        # Iterate down the list
        for i_Value in a_Unsorted:
            # Convert the value to an int
            i_Value = int(i_Value)
            # Depending on the value of i_Value compared to i_Pivot, sort it accordingly
            if i_Value < i_Pivot:
                a_Less.append(i_Value)
            if i_Value == i_Pivot:
                a_Equal.append(i_Value)
            if i_Value > i_Pivot:
                a_Greater.append(i_Value)
        # When we are done, sort our new, smaller arrays
        return Quicksort(a_Less) + a_Equal + Quicksort(a_Greater)
    # If the length is 1, we are done and returning a_Unsorted will terminate our recursion
    else:
        return a_Unsorted

a_UnsortedIds = []

for s_Ticket in a_Tickets:
    s_CleanedTicket = s_Ticket.replace("\n", "")
    o_Ticket = Ticket(s_String = s_CleanedTicket)
    a_UnsortedIds.append(o_Ticket.getTicketId())

# Quicksort so that we run through
a_SortedIds = Quicksort(a_UnsortedIds)

# Let's quickly just check what ID doesn't come after an ID one less than itself
for i in range(1, len(a_SortedIds) -1 ):
    if a_SortedIds[i-1] != a_SortedIds[i] - 1:
        print(f"Your seat is {a_SortedIds[i] - 1}")
