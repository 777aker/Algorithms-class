# import numpy because it has nice random variables and random arrays
import numpy as np

# this is a global variable to determine whether or not to print the array
# and each step of the quickSort for the testing of n = 5, 10, 20
printSorted = False

# so its easiest to just keep comparisons globally
comparisons = 0

# step number
# this is a nice way to identify steps since recursion calls prints get messy
# don't really have a clear order. It gets messy if you don't identify them
# in some way
step = 0

# this is the swap function
# takes in the array, the two values you want to swap
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    # return just because
    return

# this is the quick select alogorithm.
# takes in the array, left most index, right most index, split is the index we want to find
def QuickSelect(A, p, r, split):
    # this is just quickselect from class
    # since split is found elsewhere nothing special needed here
    # this is the base case
    if p == r:
        return r
    else:
        # call partition
        q = Partition(A, p, r)
        # if the index we solved is the value you want then swap
        # it with r and return r, since there are many calls
        # you have to return r in order to make sure r is the last
        # element out of all the calls
        if split == q:
            swap(A, q, r)
            return r
        # if the split is less that q then call Quickselect on left side
        elif split < q:
            pivot = QuickSelect(A, p, q-1, split)
            # swap the pivot gotten from the left side with r so it is in
            # the very last spot
            swap(A, pivot, r)
            # return r since that is the pivot we want and we want the calls
            # that called this to swap too
            return r
        # if none of the above worked means q+1 < split so call right side
        else:
            # basically same logic as above except on right side
            pivot = QuickSelect(A, q+1, r, split)
            swap(A, pivot, r)
            return r
    return

# this is the partition algorithm
# takes in array, left most index, right most index
def Partition(A, p, r):
    # so this prints the arrays and keeps track of the steps
    global step
    step += 1
    global printSorted
    # if we are doing one of the n = 5, 10, 20 steps then print A
    if printSorted:
        print("Beginning of Step", step, ":", A)
    # this is from class, just regular partition after this point
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        # so everytime partition makes a comparison we increment the amount
        # of comaprisons made
        global comparisons
        comparisons += 1
        if A[j] <= pivot:
            i += 1
            swap(A, i, j)
    swap(A, i+1, r)
    # if we are doing one of the n = 5, 10, 20 tests then print A
    if printSorted:
        print("End of step", step, ":", A)
    return i+1

# this is the quicksort alogrithm
# takes in array, left most index, right most index
def QuickSort(A, p, r):
    # this is just the quick sort from class
    # this is the base case for the recursion, whether or not to continue
    if (p < r):
        # this is just calling quickSelect which will put the pivot that gives
        # us a 0.25 0.75 split at A[r], to figure out what will give us a 0.25
        # split we need to use the size of p to r and multiply by 0.25 to get
        # the index of the number that will provide the split
        # ie if we have a length of 8 we want the 2 smallest element to be pivot
        # but if we have less than 4 that no work so
        if r-p >= 4:
            split = (r-p)//4
            QuickSelect(A, p, r, split)
        # this calls partition which returns the pivot index
        q = Partition(A, p, r)
        # recursive calls on quickSort on left side and right side of data
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
    # doesn't need a return yet but makes me feel better
    return

# this is what will test quickSort
# takes in n which is size to test
def tester(n):
    # creates an array with values 0 to n-1
    array = []
    for i in range(n):
        array.append(i)
    # this randomizes the array
    np.random.shuffle(array)
    # reset comparisons for this call
    global comparisons
    comparisons = 0
    global step
    step = 0
    # and hopefully, this will sort it
    QuickSort(array, 0, n-1)
    if not printSorted:
        print("Number of comparisons made by partition with n of ", n, ":", comparisons)
    return

# now lets run some tests
# does tests 2 to 2^10
for i in range(1, 11):
    print("--------------------------------------")
    n = 2**i
    tester(n)

printSorted = True
print("--------------------------------------")
tester(5)
print("--------------------------------------")
tester(10)
print("--------------------------------------")
tester(20)