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

#### Solution
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