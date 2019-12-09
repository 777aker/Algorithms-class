import numpy as np

# RUNTIME:
#
def q5(s, t, k):
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

    # this will be the solutions we return

    Output = backtrace(table, s, len(table)-1, len(table[0])-1, 0, k, [])

    return Output

def backtrace(tab, s, i, j, len, k, prev):
    if i <= 0:
        if len == k:
            return prev
        else:
            return
    if tab[i][j] == True:
        if tab[i-1][j] == True:
            possible = backtrace(tab, s, i-1, j, len, k, prev)
            if not possible == None:
                return possible
        if j-s[i-1] >= 0:
            if tab[i-1][j-s[i-1]] == True:
                prev.append(s[i-1])
                len += 1
                return backtrace(tab, s, i-1, j-s[i-1], len, k, prev)
    return False

print(q5([2,1,5,7], 4, 0))
print('------------')
print(q5([2,1,5,7], 6, 2))
print('------------')
print(q5([2,1,5,7],7,2))
print('------------')
print(q5([2,1,5,7], 4, 2))
print('------------')
print(q5([2,1,5,7], 6, 3))
print('------------')
print(q5([1,2,3,4,5], 8, 2))
print('------------')
print(q5([1,2,3,4,5], 8, 3))

