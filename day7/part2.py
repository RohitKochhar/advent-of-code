# For test purposes
import time
start_time = time.time()

a_ContainingColors  = []

class Bag():
    # Constructor
    def __init__(self, s_BagRule):
        self.a_Rule     =   s_BagRule.split(" ")
        self.s_Color    =   f"{self.a_Rule[0]} {self.a_Rule[1]}"
        self.a_Children =   self.getChildren()

    def getChildren(self):
        a_Children  =   []
        for i in range(4, len(self.a_Rule), 4):
            if self.a_Rule[4] == "no":
                return []
            else:
                s_ChildColor    =   f"{self.a_Rule[i+1]} {self.a_Rule[i+2]}"
                a_Children.append([s_ChildColor, self.a_Rule[i]])
                   
        return a_Children
    
    def __str__(self):
        #return f"{self.s_Color} is a child of {self.a_AllChildren}"
        return f"{self.s_Color} is parent to {self.a_Children}"

    def findAllChildren(self, d_BagRules):
        print(f"{self.s_Color} is parent to:")
        self.a_AllChildren  =   []
        for a_Child in self.getChildren():
            
            o_Child = d_BagRules[a_Child[0]]
            a_Entry = [o_Child, a_Child[1]]
            
            print(f"\t-> {a_Entry[1]} x {a_Entry[0].s_Color}")

            self.a_AllChildren.append(a_Entry)
            for o_Grandchild in o_Child.findAllChildren(d_BagRules):
                self.a_AllChildren.append(o_Grandchild)
        
        return self.a_AllChildren

    def ExpandChildren(self, d_BagRules):
        # Returns an array of objects
        a_Expanded = []
        for a_Child in self.a_Children:
            for i in range(0, int(a_Child[1])):
                o_Child = d_BagRules[a_Child[0]]
                a_Expanded.append(o_Child)
                for o_GrandChild in o_Child.ExpandChildren(d_BagRules):
                    a_Expanded.append(o_GrandChild) 
        self.i_NumExpandedChildren = len(a_Expanded)
        return a_Expanded



    def findNumChildren(self, i_Sum=0):
        #print(f"{self.s_Color} is parent to:")
        for a_Child in self.a_AllChildren:
            #print(f"\t-> {a_Child[1]} x {a_Child[0].s_Color}")
            i_Sum += int(a_Child[1])
            i_Sum += int(a_Child[1])*a_Child[0].findNumChildren()
        return(i_Sum)


d_BagRules = {}


a_Input = open('input.txt', 'r').readlines()

s_BagOfInterestColor    = 

for s_BagRule in a_Input:
    o_Bag   =   Bag(s_BagRule)
    if o_Bag.s_Color == "shiny gold":
        o_RootBag   =   o_Bag
    d_BagRules[o_Bag.s_Color] = o_Bag

#o_RootBag.findAllChildren(d_BagRules)

for o_Child in o_RootBag.ExpandChildren(d_BagRules):
    print(o_Child)

print(o_RootBag.i_NumExpandedChildren)