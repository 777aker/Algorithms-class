import random

#input positive integer n
#randomly shuffle array of size n
#counts the total number of flips
#run code on a bunch of n values from [2, 2^12] and present result in a table
#with the value of n in one column and number of flips in the other
#a flip is when a higher number comes before a lower number

def flip(n):
    #fill an array with elements 1 through n
    randArray = []
    i = 1
    while(i <= n):
        randArray.append(i)
        i += 1
    #shuffle the array so the elements are random
    random.shuffle(randArray)
    #prepare for counting flips
    i = 0
    flips = 0
    #goes to the first element and then checks all elements afterward to see if they are greater
    while(i < n):
        f = i+1
        while(f < n):
            if(randArray[i] > randArray[f]):
                #increment flips if one after is greater
                flips += 1
            f += 1
        i += 1
    #return how many flips there were
    return flips

#easy way to test it 12 times
j = 1
while(j < 13):
    #print out answers in nice formmat
    print("2^" + str(j) + " " + str(2**j) + ": " + str(flip(2**j)))
    j += 1