# advent-of-code
 My files for the advent of code, December 2020

All problem outlines are taken from https://adventofcode.com/2020

## Day 1
### Part 1
#### Problem Outline
the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

`1721, 979, 366, 299, 675, 1456`

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

#### Solutions
##### Solution A
The first solution I found for this problem employs the following steps:

We want to find two values from a list with n elements that equal some number 2020

1. Using a quicksort algorithm with a worst-case complexity of n^2, we sort the data from least to greatest
2. Using an ArrayToHash function with a worst-case complexity of n, we break the big array up into a matrix of 21 rows, with the index of each row representing the hundreds place of the value
3. We then iterate through the first 11 rows of the hash matrix. For each number A in row R, we check the row 21-1-R to see if there is a number B such that A+B=2020. At worst there can be 100 items in each array, so our worst case complexity for this step is (21/2 + 1)*100=1100

This program takes between 0.004 and 0.005 seconds to run with an input size of 200, and has an apparent worst-case complexity of n^2 + n + 1100

The only problem with this solution is the quicksort algorithm, which isn't really needed. 

##### Solution B
The second solution I found is the same as the first, but without a quicksort algorithm

We want to find two values from a list with n elements that equal some number 2020

1. Using an ArrayToHash function with a worst-case complexity of n, we break the big array up into a matrix of 21 rows, with the index of each row representing the hundreds place of the value
2. We then iterate through the first 11 rows of the hash matrix. For each number A in row R, we check the row 21-1-R to see if there is a number B such that A+B=2020. At worst there can be 100 items in each array, so our worst case complexity for this step is (21/2 + 1)*100=1100

This program takes between 0.002 and 0.004 seconds to run with an input size of 200, and has an apparent worst-case complexity of n+1100.

Still, this solution would not work if we wanted any different number than 2020, which although it works, we can still improve that.

##### Solution C
This solution is the same as the second, but now it can adjust to find different values rather than just 2020

We want to find two values from a list with n elements that equal some number N

1. Using an ArrayToHash function with a worst-case complexity of n, we break the big array up into a matrix of (R = N // 100 + 1) rows, with the index of each row representing the hundreds place of the value
2. We then iterate through the first R/2 rows of the hash matrix. For each number A in row r, we check the row R-1-r to see if there is a number B such that A+B=2020. At worst there can be 100 items in each array, so our worst case complexity for this step is (R/2)*100=50R

#### Results
- Solution A has a complexity of n^2 + n + 1100
- Solution B has a complexity of n + 1100
- Solution C has a complexity of n+50(N // 100+1)

When we are searching for 2020, solution B and C are identical, but solution C is the better algorithm as it is the one which is more flexible.

The verbose code with the quicksort algorithm included is in `day1/part1_verbose`, the bare minimum operating code with the best compleixty is in `day1/part1_slim`

### Part 2
#### Problem Outline
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

#### Solutions
##### Solution A
Immediately upon reading this new problem, it seems intuitive to simply adapt our code from part 1 to be recursive, so that for a given number a, we can find two numbers, b and c, using our same hash table which equal 2020-a

We want to find 3 numbers, a,b,c, from a list of n numbers, which add to some larger number N (=2020) 

1. Convert the array into an unordered hash table, this has a complexity of n + N%100.
2. Iterate down the rows of the first half of the hash matrix. For each row that we iterate, go across the row as well and try each value as the base number. There is a worst case complexity of 100 for each row, and we do this ((N+1)%100)/2 times, so the worst case complexity for this step is 50*((N+1)%100).
3. We repeat this step again to find the two numbers which will add to the number from step 2 to add 2020. So this step has a complexity of 50*((N+1)%100), but it happens for each occurance of step 2.

This algorithm has an apparent complexity of n+(N%100)+(50*(N%100))^2

For N = 2020, we get have an affine complexity. This solution takes about 0.003 seconds.
