# For test purposes
import time
start_time = time.time()

# Create a passport class
class Passport():
    byr     = -1
    iyr     = -1
    eyr     = -1
    hgt     = -1
    hcl     = -1
    ecl     = -1
    pid     = -1
    cid     = -1
    def __init__(self, s_PassportString):
        # This function is given a flattened array of string objcts, we need to convert this
        #   to a valid object
        a_PassportProperties = s_PassportString.split(" ")
        for s_Entry in a_PassportProperties:
            a_Property  = s_Entry.split(":")
            if a_Property == "":
                break
            elif a_Property[0] == 'byr':
                self.byr    = a_Property[1]
            elif a_Property[0] == 'iyr':
                self.iyr    = a_Property[1]
            elif a_Property[0] == 'eyr':
                self.eyr    = a_Property[1]
            elif a_Property[0] == 'hgt':
                self.hgt    = a_Property[1]
            elif a_Property[0] == 'hcl':
                self.hcl    = a_Property[1]
            elif a_Property[0] == 'ecl':
                self.ecl    = a_Property[1]
            elif a_Property[0] == 'pid':
                self.pid    = a_Property[1]
            elif a_Property[0] == 'cid':
                self.cid    = a_Property[1]

    def CheckValidPassport(self):
        return not ((self.byr == -1) or (self.iyr == -1) or (self.eyr == -1) or (self.hgt == -1) or (self.hcl == -1) or (self.ecl == -1) or (self.pid == -1))

    def __str__(self):
        return f"byr: {self.byr}, byr: {self.byr}, eyr: {self.eyr}, hgt: {self.hgt}, hcl: {self.hcl}, ecl: {self.ecl}, pid: {self.pid}, cid: {self.cid}"

# Create an array from our input file
a_PassportList  = open('input.txt', 'r').readlines()

a_PassportData      = [] 
s_PassportDetail    = ""
i_ValidCount        = 0

for s_Line in a_PassportList:
    
    if s_Line != "\n":
        s_PassportDetail += s_Line
               
    if s_Line == "\n":
        s_FlattenedPassport     = s_PassportDetail.replace("\n", " ")
        o_Passport              = Passport(s_FlattenedPassport)
        i_ValidCount += o_Passport.CheckValidPassport()
        a_PassportData.append(o_Passport)
        s_PassportDetail = ""

s_FlattenedPassport     = s_PassportDetail.replace("\n", " ")
o_Passport              = Passport(s_FlattenedPassport)
i_ValidCount += o_Passport.CheckValidPassport()

print(i_ValidCount)

        

