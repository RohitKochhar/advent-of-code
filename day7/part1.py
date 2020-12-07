# For test purposes
import time
start_time = time.time()

a_ContainingColors  = []

class Bag():
    s_Color         =   ""
    # Define an array with all the colors this bag can contain
    a_Children      =   []
    # Define an array of all the colors that can contain this bag
    a_Parents   =   []

    # Constructor
    def __init__(self, s_BagRule):
        self.a_Rule     =   s_BagRule.split(" ")
        self.s_Color    =   f"{self.a_Rule[0]} {self.a_Rule[1]}"
        self.a_Children =   self.getChildren()

    def getChildren(self):
        a_Children  =   []
        for i in range(4, len(self.a_Rule), 4):
            s_ChildColor    =   f"{self.a_Rule[i+1]} {self.a_Rule[i+2]}"
            a_Children.append([s_ChildColor, self.a_Rule[i]])
        
        return a_Children
    
    def __str__(self):
        return f"{self.s_Color} is parent to {self.a_Children}"

    def isParentOf(self, s_ChildColor):
        b_IsParentOf    =   False
        for a_Child in self.a_Children:
            if a_Child[0] == s_ChildColor:
                b_IsParentOf    =   True
                break
        return b_IsParentOf

    def findAllParents(self, a_Bags):
        # This function will go through all our rules to find bags which are parent to self
        self.a_Parents = []
        for o_Bag in a_Bags:
            if o_Bag.isParentOf(self.s_Color):
                self.a_Parents.append(o_Bag)
                if o_Bag.findAllParents(a_Bags) != []:
                    for o_Parent in o_Bag.findAllParents(a_Bags):
                        self.a_Parents.append(o_Parent)
        self.a_Parents = set(self.a_Parents)
        return self.a_Parents


a_Input = open('input.txt', 'r').readlines()
a_Bags  = []
s_BagOfInterestColor    = "shiny gold"

for s_BagRule in a_Input:
    o_Bag   =   Bag(s_BagRule)
    if o_Bag.s_Color == s_BagOfInterestColor:
        o_RootBag   =   o_Bag
    else:
        a_Bags.append(o_Bag)

a_Parents = o_RootBag.findAllParents(a_Bags)

for o_Parent in a_Parents:
    print(o_Parent.s_Color)

print(len(a_Parents))