import numpy as np

# i.
def parti(n):
    # creates a list and populates it with values
    # 1 through n and then randomizes it
    data = []
    for i in range(n):
        data.append(i+1)
    np.random.shuffle(data)
    return data

# ii.
def partii(data):
    # counts the number of flips in n^2 time
    flips = 0
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if data[i] > data[j]:
                flips += 1
    return flips

# iii.
def partiii(data):
    # if there is only 1 or less elements then return
    if len(data) > 1:
        # this splits the data into two subarrays
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]

        # add to the number of flips the flips counted
        # by the call on the left subarray and the right subarray
        # and call recursively on the left and right halves of the array
        flips = partiii(left)
        flips += partiii(right)

        # so for everything in the left half,
        # if there is anything greater in the right half
        # then add to the count of flips
        for i in range(len(left)):
            for j in range(len(right)):
                if left[i] > right[j]:
                    flips += 1

        # return the number of flips
        return flips
    # returns 0 if there is 1 or 0 elements since it needs
    # a return and there are 0 flips for a single element
    return 0



# a tester method for easily plugging in
# a size and running all the functions
def tester(n):
    # making the data using part i
    data = parti(n)
    # printed the data to make sure correct
    # amount of flips was being counted
    # but thats a lot for 2^12 so no more
    # print(data)
    print("Number of flips counted by n^2 runtime: ", partii(data))
    print("Number of flips counted by nlogn runtime: ", partiii(data))

# iv.
# this for loop just runs the tester program for
# 2^1 through 2^12
for i in range(1,13):
    size = 2**i
    print("------------------------------------------------------")
    print("For size: ", size)
    tester(size)