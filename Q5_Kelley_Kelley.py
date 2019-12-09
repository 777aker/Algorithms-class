import numpy as np

# RUNTIME:
# The runtime is n*t where n is the length of the array
# and t is the target sum we are trying to achieve.
# This is because the algorithm does a bottom up approach to
# filling in a table of size n*t (lines 16 through 32).
# Pulled from Quiz 5.
# There is a helper function called once however,
# that function backwards traces the n*t table,
# but will never traverse the entire table. Some things will be called
# twice however but the combinations of this are minuscule and can't
# create a runtime greater than n*t (lines 47 through 66)
# So the overall runtime is the greater of the two algorithms
# which is n*t
def q5(s, t, k):
    # Parameters:
    # s is the numbers
    # t is the target sum
    # k is the cardinality

    # First, we create the table that says whether or not we
    # can sum up to a value just like in the quiz 5 problem
    # this creates a table len(s)+1 by t, where len(s)+1 is
    # the rows, and t is the columns
    table = [[False] * (t+1) for i in range(len(s)+1)]
    # base case first
    table[0][0] = True
    # bottom up method from quiz 5
    # rewritten a little to work in python
    # First row will be all falses except 0,0 so skip it
    # Makes it easier to deal with out of bounds error
    i = 1
    while i < len(table):
        j = 0
        while j < len(table[i]):
            if j - s[i-1] >= 0:
                table[i][j] = (table[i-1][j] or table[i-1][j - s[i-1]])
            else:
                table[i][j] = table[i-1][j]
            j += 1
        i += 1

    # Output is our solution
    # backtrace will take our table and go backwards along it to find
    # what values were added to get our sum and how many numbers were
    # needed in order to determine if there is a solution to our problem
    # If there are multiple solutions it only returns the first one it finds
    Output = backtrace(table, s, len(table)-1, len(table[0])-1, 0, k, [])
    # If Output = 0 then there was no solution so return False
    if len(Output) == 0:
        return False
    # else return what our solution was
    return Output

def backtrace(tab, s, i, j, len, k, prev):
    # Parameters:
    # tab is the table we are backtracing
    # s is our array of values
    # i is the row in the table we are on (items we are considering)
    # j is the col in the table we are on (target sum we want)
    # len is how many elements we have added so far to get this subproblem (cardinality)
    # k is our target cardinality
    # prev is the elements previously used in order to get to this subproblem

    # prev is actually a pointer and I don't want that
    # so I make a copy so that the recursive calls don't
    # all change the same variable. Not doing this
    # led to some cases where it would fail
    newprev = []
    for element in prev:
        newprev.append(element)
    # if i == 0 then we have achieved our sum
    if i == 0:
        # if the number of elements added together (len) is k
        # then we have achieved our cardinality return this solution
        if len == k:
            return newprev
        # else then the numbers summed to 0 but the cardinality
        # was wrong so just return an empty list as in it failed
        else:
            return []
    # so if the table said we could sum to our target with this subproblem,
    # then we do stuff to find out how. Else we just return an empty
    # list since we couldn't achieve our subproblem ie this path failed
    if tab[i][j] == True:
        # first (since it was easier I did it first) check the path
        # not considering this element
        if tab[i-1][j] == True:
            # call backtrace on the subproblem not considering this element
            possible = backtrace(tab, s, i-1, j, len, k, newprev)
            # if backtrace didn't return an empty string then we found
            # a path so return that path. If backtrace returned an empty string
            # then we didn't find a path so don't return anything because then
            # we need to check to see if including the element in our subproblem
            # will come up valid. ie the next if statement
            if not possible == []:
                return possible
        # if we consider this element in our solution
        if j-s[i-1] >= 0:
            if tab[i-1][j-s[i-1]] == True:
                # then append this element to our list of elements in the solution
                newprev.append(s[i-1])
                # increment the number of elements we have in this solution
                len += 1
                # call backtrace on the subproblem of not considering this element
                # and a sum of minus this element
                return backtrace(tab, s, i-1, j-s[i-1], len, k, newprev)
    # if it reaches here then it failed so just return an empty list
    return []

# A whole lot of test cases
# Some of them were shared and ripped
# from other students to compare and
# see if our solutions lined up
print(q5([2,1,5,7], 4, 0))
print('------------')
print(q5([2,1,5,7], 6, 2))
print('------------')
print(q5([2,1,5,7], 7, 2))
print('------------')
print(q5([2,1,5,7], 4, 2))
print('------------')
print(q5([2,1,5,7], 6, 3))
print('------------')
print(q5([1,2,3,4,5], 8, 2))
print('------------')
print(q5([1,2,3,4,5], 8, 3))
print('------------')
print(q5([5,4,2,1,3], 8, 3))
print('------------')
print(q5([5,4,2,1,3], 8, 2))

