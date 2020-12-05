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

    def ValidateByr(self):
        # First, check if the value even exists
        if self.byr == -1:
            return False
        # Birth year must be four digits, at least 1920 and at most 2002
        elif len(self.byr) != 4:
            # Check 4 digits are there
            return False
        elif int(self.byr) < 1920 or int(self.byr) > 2002:
            # Check the bounds
            return False
        else:
            # Otherwise, we are good!
            return True
    
    def ValidateIyr(self):
        # First, check if the value even exists
        if self.iyr == -1:
            return False
        # Issue year must be four digits, at least 2010 and at most 2020
        elif len(self.iyr) != 4:
            # Check 4 digits are there
            return False
        elif int(self.iyr) < 2010 or int(self.iyr) > 2020:
            # Check the bounds
            return False
        else:
            return True

    def ValidateEyr(self):
        # First, check if the value even exists
        if self.eyr == -1:
            return False
        # Expiry year must be four digits, at least 2020 and at most 2030
        elif len(self.eyr) != 4:
            # Check if there are four digits
            return False
        elif int(self.eyr) < 2020 or int(self.eyr) > 2030:
            # Check the bounds
            return False
        else:
            return True

    def ValidateHgt(self):
        # First, check if the value even exists
        if self.hgt == -1:
            return False
        # Check that the unit is included
        elif self.hgt[-2:] != "cm" and self.hgt[-2:] != "in":
            return False
        elif self.hgt[-2:] == "cm":
            if int(self.hgt[:-2]) < 150 or int(self.hgt[:-2]) > 193:
                return False
            else:
                return True
        elif self.hgt[-2:] == "in":
            if int(self.hgt[:-2]) < 59 or int(self.hgt[:-2]) > 76:
                return False
            else:
                return True
        else:
            return False

    def ValidateHcl(self):
        if self.hcl == -1:
            return False
        elif len(self.hcl) != 7:
            return False
        elif self.hcl[0] != "#":
            return False
        else:
            return True

    def ValidateEcl(self):
        if self.ecl == -1:
            return False
        else:
            return (self.ecl == 'amb') or (self.ecl == 'blu') or (self.ecl == 'brn') or (self.ecl == 'gry') or (self.ecl == 'grn') or (self.ecl == 'hzl') or (self.ecl == 'oth')

    def ValidatePid(self):
        if self.pid == -1:
            return False
        else:
            return (len(self.pid) == 9)

    def CheckValidPassport(self):
        return self.ValidateByr() and self.ValidateIyr() and self.ValidateEyr() and self.ValidateHgt() and self.ValidateHcl() and self.ValidateEcl() and self.ValidatePid()

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

        if o_Passport.CheckValidPassport() == True:
            print(o_Passport)

        s_PassportDetail = ""

s_FlattenedPassport     = s_PassportDetail.replace("\n", " ")
o_Passport              = Passport(s_FlattenedPassport)
i_ValidCount += o_Passport.CheckValidPassport()

print(i_ValidCount)

        

