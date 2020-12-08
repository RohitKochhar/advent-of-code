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

# Define the hash matrix from our input file
m_Hash = ArrayToHash(open("input.txt", "r").readlines())

# Iterate through row in the first half of the hash matrix
for i in range(0, int((len(m_Hash)+1)/2)):
    # Go across each row
    for i_A in m_Hash[i]:
        # i_A is our base number, we need to find two numbers when added to A that will make 2020
        i_Needed = i_DesiredValue-i_A
        # Now, we have to iterate through the hash table again to find two values which add to i_Needed
        for j in range(0, int((len(m_Hash)+1)/2)):
            # Go across each row again
            for i_B in m_Hash[j]:
                # Find the value of what C must be
                i_NeededC = i_Needed - i_B
                for i_C in m_Hash[i_NeededC // 100]:
                    if i_C == i_NeededC:
                        print(f"{i_A}, {i_B}, and {i_C} make {i_A+i_B+i_C} for a product of {i_A*i_B*i_C}")

print(time.time() - start_time)