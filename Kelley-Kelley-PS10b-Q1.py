# numpy is nice for randoms and I like to import it by default bc its useful
# idk if ill use it but nice to have as an option
import numpy as np

# input is two strings, cost of operations
# uses dynamic programming to return the cost matrix S
# contains optimal solution for all subproblems aligning the two strings
def alignStrings(x, y, cins, cdel, csub):
    # initialize the matrix
    S = [x[:] for x in [[0] * (len(y)+1)] * (len(x)+1)]
    # iterate through entire set
    for i in range(0, len(x)+1):
        for j in range(0, len(y)+1):
            # set the base case to 0
            if ((i == 0) and (j == 0)):
                S[0][0] = 0
            # so if i or j = 0 then we will get an index out of bounds
            # which is fine since these are basically base cases, ie
            # they are just inserting or deleting because that is what
            # the first row and col are
            # so if we are on the first row, just add cost of insert each time
            # since we are trying to match an empty substring to this
            elif i == 0:
                S[0][j] = S[0][j-1] + cins
            # if we are on the first col add the cost of del each time
            # since we are trying to match to an empty substring
            elif j == 0:
                S[i][0] = S[i-1][0] + cdel
            # this means we aren't on a base case so yay
            else:
                # it won't be random here and that's ok because here
                # it is unnoticable since you end up with same table
                # if things are equal
                # the random selection will be in extract alignment
                # set the min to the max it could be
                min = float('inf')
                # this is if a sub is the min cost
                if S[i-1][j-1] + csub < min:
                    min = S[i-1][j-1] + csub
                # this is if a del is the min cost
                if S[i-1][j] + cdel < min:
                    min = S[i-1][j] + cdel
                # this is if an ins is the min cost
                if S[i][j-1] + cins < min:
                    min = S[i][j-1] + cins
                # this is a no op
                if x[i-1] == y[j-1]:
                    min = S[i-1][j-1]
                # and now set the S we are on to the min cost since
                # that is are cost
                S[i][j] = min
    return S

# takes in optimal cost matrix, the strings x and y, cost of operations
# and returns a vector a that represents an optimal sequence of edit
# operations to convert x into y,
def extractAlignment(S, x, y, cins, cdel, csub):
    # this is the solution string returned at the end
    solution = []
    # starting at the end like in class to backtrace to answer
    # and on piazza, tried from S[0][0] but there are so many
    # cases where that doesn't work
    i = len(x)
    j = len(y)
    # until i or j is 0 keep going, we stop here because don't want
    # to go out of bounds, later is addressed if we stop at like i = 0 j = 3
    while i > 0 and j > 0:
        # mins is going to store all the possible ways we could go on the table
        mins = []
        # possible stores solutions that work, we will randomly select from
        # possible later to pick random possible solutions
        possible = []
        # we append every possible path to min
        mins.append(S[i-1][j])
        mins.append(S[i][j-1])
        mins.append(S[i-1][j-1])
        # take the minimum of the possible paths
        minimum = min(mins)
        # if delete works as an optimal path then append it to possible
        if (minimum == S[i-1][j] and S[i][j] == S[i-1][j] + cdel):
            possible.append('delete')
        # if insert works as an optimal path then append it to possible
        if (minimum == S[i][j-1] and S[i][j] == S[i][j-1] + cins):
            possible.append('insert')
        # if substitution works as an optimal path then append it to possible
        if (minimum == S[i-1][j-1] and S[i][j] == S[i-1][j-1] + csub):
            possible.append('substitution')
        # if possible is empty the del, ins, or sub didn't work so it must be
        # a no-op. append no-op to solution, go up one row left one col,
        # and go to next iteration by skipping the rest
        if len(possible) == 0:
            solution.append('no-op')
            i -= 1
            j -= 1
        # if it's not a no-op
        else:
            # pick a possible optimal path at random and append it to solutions
            solution.append(np.random.choice(possible))
            # if the last element in solution is delete ie we just appended delete
            # then go up one row
            if solution[-1] == 'delete':
                i -= 1
            # if the last element in solution is insert ie we just apppended insert
            # then go left one column
            if solution[-1] == 'insert':
                j -= 1
            # if the last element in solution is substitution ie we just appended substitution
            # then go left one col up one row
            if solution[-1] == 'substitution':
                i -= 1
                j -= 1
    # so if we stopped at like i = 0 j = 3, then add inserts until
    # both are 0
    if j != 0:
        while j > 0:
            solution.append('insert')
            j -= 1
    # so if we stopped at like j = 0 i = 3, then add deletes until
    # both are 0
    if i != 0:
        while i > 0:
            solution.append('delete')
            i -= 1
    # reverse solution
    solution = solution[::-1]
    # return the solution
    return solution


# takes input string x, integer 1 <= L <= n, and optimal solution of a edits
# to x, which would make x to y. returns each of the substrings of length at least L
# in x that align exactly, via a run of no-ops to a substring in y
# sum up all the continuous no ops and if they are >= L
# then save them in a list to return
def commonSubstrings(x, L, a):
    # this saves the solution
    solution = []
    # this saves the x position we are since an insert means x will
    # be offset from a by one
    xpos = 0
    # save the a position we are at
    i = 0
    # go through everything in a
    while i < len(a):
        # this is the possible substring that we might append to solution
        # if it ends up being >= L
        possible = []
        # this is the number of no ops we have / length of the common
        # substring
        ops = 0
        # while i is less than the length of a and a[i] is a no-op
        while i < len(a) and a[i] == 'no-op':
            # add to the number of no ops
            ops += 1
            # add the x we are at to possible substring
            possible.append(x[xpos])
            # increment i and xpos
            i += 1
            xpos += 1
        # if the number of ops we did on the substring are >= L then
        # append the substring to the solution
        if ops >= L:
            solution.append(possible)
        # if a is an insert then decrement x pos to counteract the offset
        # an insert creates
        if i < len(a) and a[i] == 'insert':
            xpos -= 1
        # increment i and xpos
        i += 1
        xpos += 1
    # return our solution which is a list of common substrings
    return solution

# a helper function for printing optimal solution tables nicely
def printOpt(x, y, S):
    col = -1
    print('s=', x)
    print('t=', y)
    print('   _ P O L Y N O M I A L')
    for i in S:
        if col == -1:
            print('_', i)
            col += 1
        else:
            print(x[col], i)
            col += 1
# Below are a lot of test cases and some of the actual things we were s
# supposed to check, some test cases from previous homeworks

source = "bear"
target = "bare"
solution = alignStrings(source, target, 1, 1, 1)
printOpt(source, target, solution)
alignment = extractAlignment(solution, source, target, 1, 1, 1)
print(alignment)
print(commonSubstrings(source, 1, alignment))
print('------------------------')

source = 'plain'
target = 'plane'
solution = alignStrings(source, target, 2, 2, 2)
printOpt(source, target, solution)
alignment = extractAlignment(solution, source, target, 2, 2, 2)
print(alignment)
print(commonSubstrings(source, 1, alignment))
print('------------------------')

source = 'EXPONENTIAL'
target = 'POLYNOMIAL'
solution = alignStrings(source, target, 2, 1, 2)
printOpt(source, target, solution)
alignment = extractAlignment(solution, source, target, 2, 1, 2)
print(alignment)
print(commonSubstrings(source, 1, alignment))
print('-------------------------')

# now time for the songs
file = open('Song1_Folsom_Prison.txt', 'r')
file2 = open('Song2_Crescent_City_Blues.txt', 'r')
song1 = file.read()
song2 = file2.read()
file.close()
file2.close()
alignment = alignStrings(song1, song2, 1, 1, 1)
# ok so actually no thats a lot # printOpt(song1, song2, alignment)
operations = extractAlignment(alignment, song1, song2, 1, 1,1)
substrings = commonSubstrings(song1, 10, operations)
# print('Operations: ', operations)
print('Length of song one and song two: ', len(song1), len(song2))
print('Substrings of length 10 or more: ')
lensub = 0
for i in substrings:
    print('Length:', len(i), ', substring:', i)
    lensub += len(i)
print('How much of song2 does not have in common with song1', lensub)
print('Proportion of song2 that is part of song1', lensub/len(song2))
stringVersion = ''
for i in substrings:
    for j in i:
        stringVersion += str(j)
print(stringVersion)