import numpy as np

def MergeWithErrors(A, p, q, r):
    low = A[p:(q+1)]
    high = A[(q+1):(r+1)]
    print(low)
    print(high)
    i = 0
    j = 0
    k = p
    while(i < q-p+1 and j < r-q):
        if(low[i] <= high[j]):
            A[k] = low[i]
            j += 1
        else:
            A[k] = high[j]
            i += 1
        k += 1
    while(i < q-p+1):
        A[k] = low[i]
        i += 1
        k += 1
    while(j < r-q):
        A[k] = high[j]
        j += 1
        k += 1
    print(A)

b = [0,1,3,5,2,4,6,7]
MergeWithErrors(b, 0, 3, 7)
c = np.random.randint(0, 6, 5)
d = np.random.randint(0, 6, 7)
c = np.sort(c)
d = np.sort(d)
e = []
for i in c:
    e.append(i)
for i in d:
    e.append(i)
MergeWithErrors(e, 0, 4, 11)
i = 0
while i < len(e)-1:
    if e[i] > e[i+1]:
        print('False')
    i += 1