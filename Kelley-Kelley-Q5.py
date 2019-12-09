import numpy as np

def partition(bottles, lids, p, r):
    # this takes the last element in bottles and sets it as the pivot
    pivotb = bottles[r]
    # this initializes i which lids[:i] will be less than pivotb
    i = p-1
    # this initializes the bottle pivot to be -1 since not found yet
    pivotl = -1
    # for all the stuff in lids including the last element
    for j in range(p, r+1):
        # if it is less than the bottle pivot then put it in lids[:i]
        if lids[j] < pivotb:
            i += 1
            # this swaps the elements
            temp = lids[j]
            lids[j] = lids[i]
            lids[i] = temp
            # if we are swapping the pivot then we need to keep track
            # of where we moved it to so we can put it in the correct
            # spot later
            if i == pivotl:
                pivotl = j
        # if the value equals the bottle pivot then save it because thats
        # what we will use to sort the bottles
        elif lids[j] == pivotb:
            pivotl = j
    # this swaps the pivot so that it is after the end of lids[:i]
    temp = lids[pivotl]
    lids[pivotl] = lids[i+1]
    lids[i+1] = temp
    # set the lids pivot to actually be the value instead of the index
    pivotl = temp
    # now we will do the same we did for lids except for bottles
    # this initializes i which bottles[:i] will be less than pivotb
    i = p - 1
    # for all the stuff in bottles except last since we know thats the pivot
    for j in range(p, r):
        # if it is less than the lid pivot then put it in bottles[:i]
        if bottles[j] < pivotl:
            i += 1
            # this swaps the elements
            temp = bottles[j]
            bottles[j] = bottles[i]
            bottles[i] = temp
    # since the bottles pivot was the last thing put it in after i so its after bottles[:i]
    # which only contains elements smaller than it
    temp = bottles[r]
    bottles[r] = bottles[i+1]
    bottles[i+1] = temp
    return i + 1

# it will basically sort the data using quicksort
# except the pivot will be the thing in the other array
def bottleQuickSort(bottles, lids, p, r):
    if p < r:
        q = partition(bottles, lids, p, r)
        bottleQuickSort(bottles, lids, p, q-1)
        bottleQuickSort(bottles, lids, q+1, r)

# now we test for correctness
bottles = []
lids = []
# make bottles and lids
for i in range(1, 10):
    bottles.append(i)
    lids.append(i)
# shuffle them around
np.random.shuffle(bottles)
np.random.shuffle(lids)
# print out what they are to start
print("Before sorting")
print("bottles: ", bottles)
print("lids: ", lids)
# sort them
bottleQuickSort(bottles, lids, 0, 8)
# print the results
print("After sorting")
print("bottles: ", bottles)
print("lids: ", lids)

# but just to be sure because I'm extra, lets try 100 times with
# a size of 50 for bottles and lids (technically like 49 or something)
# so if it fails a single time this will be true
failed = False
# do the test 100 (really I think like 98 or something) times
for i in range(1, 100):
    bottles = []
    lids = []
    # an array size of 48??
    for i in range(1, 50):
        bottles.append(i)
        lids.append(i)
    # shuffle the arrays
    np.random.shuffle(bottles)
    np.random.shuffle(lids)
    # sort them
    bottleQuickSort(bottles, lids, 0, 48)
    # if a single element does not equal the corresponding element
    # in the other array the set failed to true
    for i in range(len(bottles)):
        if not bottles[i] == lids[i]:
            failed = True
# print whether it failed or not
if failed:
    print("Dang it failed, that really sucks")
    print("Never failed for me and I tried several times")
else:
    print("OMG I actually did it. It passed like 100 tries with size 50 arrays :)")
