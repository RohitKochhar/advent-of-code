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
        print((self.getRowNumber() * 8) + self.getSeatNumber())
        return self.getRowNumber() * 8 + self.getSeatNumber()

    def getPosition(self):
        print(f"Row: {self.getRowNumber()}, Seat: {self.getSeatNumber()}")
        return f"Row: {self.getRowNumber()}, Seat: {self.getSeatNumber()}"
    def __str__(self):
        return f"Ticket Label: {self.s_String}"

i_MaxId = 0
for s_Ticket in a_Tickets:
    s_CleanedTicket = s_Ticket.replace("\n", "")
    o_Ticket = Ticket(s_String = s_CleanedTicket)
    o_Ticket.getPosition()
    if o_Ticket.getTicketId() > i_MaxId:
        i_MaxId = o_Ticket.getTicketId()
    
print(i_MaxId)