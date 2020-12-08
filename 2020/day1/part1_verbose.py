# For test purposes
import time
start_time = time.time()

i_DesiredValue = 2020

def ArrayToHash(a_Sorted):
    # Find how many 100 intervals we need based on our desired number, and add 1
    i_Intervals = (i_DesiredValue // 100) + 1
    print(i_Intervals)
    a_Matrix = []
    
    # Create a hash table with an index for each possible hundred value
    for i in range(0, i_Intervals):
        a_Matrix.append([])

    # The value will be stored in the array with the index of the numbers hundreds value
    for i_Item in a_Sorted:
        a_Matrix[int(i_Item) // 100].append(int(i_Item))
    # Once it is sorted, return the hashtable
    return a_Matrix

m_Hash = ArrayToHash(open("input.txt", "r").readlines())

for i in range(0, int((len(m_Hash)+1)/2)):
    for j in m_Hash[i]:
        for a in m_Hash[((2020-j) // 100)]:
            if a == 2020-j:
                print(f"{j} and {a} make {j+a}, for a product of {j*a}")

print(time.time() - start_time)

# First, we make a quicksort algorithm
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