result = -1

# First, we make a quicksort algorithm
def Quicksort(a_Unsorted):
    a_Less    = []
    a_Equal   = []
    a_Greater = []

    if len(a_Unsorted) > 1:
        i_Pivot = int(a_Unsorted[0])
        for i_Value in a_Unsorted:
            i_Value = int(i_Value)
            if i_Value < i_Pivot:
                a_Less.append(i_Value)
            if i_Value == i_Pivot:
                a_Equal.append(i_Value)
            if i_Value > i_Pivot:
                a_Greater.append(i_Value)

        return Quicksort(a_Less) + a_Equal + Quicksort(a_Greater)

    else:
        return a_Unsorted

a_Sorted = Quicksort(open("input.txt", "r").readlines())

def ArrayToHash(a_Unsorted):
    # Values are between 0 and 2020, so we should organize values in terms of their hundreds value
    # So we should start by defining a matrix with 21 rows
    a_Matrix = [    [], [], [], [], [], [], [],
                    [], [], [], [], [], [], [],
                    [], [], [], [], [], [], [], 
    ]

    for i_Item in a_Unsorted:
        a_Matrix[i_Item // 100].append(i_Item)

    return a_Matrix


m_Hash = ArrayToHash(a_Sorted)

for i in range(0, int((len(m_Hash)+1)/2)):
    for j in m_Hash[i]:
        for a in m_Hash[((2020-j) // 100)]:
            if a == 2020-j:
                print(f"{j} and {a} make {j+a}, for a product of {j*a}")
