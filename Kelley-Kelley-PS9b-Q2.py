# for easily creating random arrays
import numpy as np

# this is part b of question two, ie the bottom up DP table filling version
# takes in list of assignments, outputs maximum points
def partb(A):
    # this holds the solutions
    solutions = []
    # this is the base case
    solutions.append(A[0])
    # this is another base case since we
    # don't want A[-1] when we reach to A[i-2] when i = 1
    if A[1] > A[0]:
        solutions.append(A[1])
    else:
        solutions.append(A[0])
    # iterate through the rest of the elements for optimal overall solution
    for i in range(2, len(A)):
        # see whether the optimal solution is to include this item or
        # if it is to not include it
        # it does so by looking at the optimal solution for the item before it,
        # and the optimal solution for the item two before it and it
        solutions.append(max(solutions[i-1], solutions[i-2] + A[i]))

    return solutions[len(solutions)-1]

# this is part c which is part b except O(1) space instead
# takes in list of assignments, outputs maximum points
def partc(A):
    # so i1 and i2 are going to be the optimal solution 1 back and 2 back from the current one
    # these are the two base cases
    i2 = A[0]
    i1 = A[1]
    if i2 > i1:
        i1 = i2
    # run the first step of our base cases to see which of the base cases is bigger
    for i in range(2, len(A)):
        # temporarily hold i1
        temp = i1
        # replace i1 with our optimal solution for this step
        i1 = max(i1, i2 + A[i])
        # replace i2 with what i1 was
        i2 = temp
    # i1 will be our optimal solution in the end
    return i1

# this is to test the two functions
def tester(A):
    print("For the array", A, "max points:", partb(A),",", partc(A))

# the array i created as counterexample to greedy strategy being tested
tester([1,1,9,1,1,9])
# the array provided being tested
tester([2,7,9,3,1])
# randomly generating arrays to test
for i in range(0,5):
    tester(np.random.randint(1, 10, 10))