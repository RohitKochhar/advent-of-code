# For test purposes
import time
start_time = time.time()

# Create an array from our input file
M_Plane = open('input.txt', 'r').readlines()

# We don't need to convert this to a matrix in the form of [ [] , [] , []]
# Since python interprets strings as char arrays, we can keep this in the form of
# [ '', '' , '' ]

# We start at the top left corner, which is a_InputLines[0][0]
# The next position we are going to will be a_InputLines[1][3]
# At iteration i, our position will be a_InputLines[i][3*i], assuming that we start with i=0
# We need to reach the bottom, so we have to iterate down the whole list, so we start our for loop as follows
# Of course, our for loop will quickly try to access indices beyond the length of our string, so we have to account for the repeating forest
# Only the second index, 3*i will yield an error, so we should catch these errors and handle them immediately

i_CurrentXPosition          = 0
i_CurrentYPosition          = 0
i_TreesHit                  = 0

for a_XDimension in M_Plane:
    # Clean up the line from the file
    a_XDimension = a_XDimension.replace("\n","")
    # Check our current square for a tree
    i_TreesHit += (M_Plane[i_CurrentYPosition][i_CurrentXPosition] == "#")
    # Move to the next position
    i_CurrentYPosition += 1
    i_CurrentXPosition += 3
    # Re-populate the forest if needed
    if i_CurrentXPosition >= len(a_XDimension):
        i_CurrentXPosition -= len(a_XDimension)
    
print(time.time() - start_time)