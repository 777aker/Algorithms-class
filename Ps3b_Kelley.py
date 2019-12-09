def robot(k, s):
    #it's current position
    current = 0
    #the list of stops
    stops = []
    #the iterator
    i = 0
    while i < len(s)-1:
        if s[i+1] - s[current] > k:
            current = i
            stops.append(s[current])
        i += 1
    print("Required", k, "stops:", stops)

A = [0,20,37,54,70,90]
B = [0,18,21,24,37,56,66]
C = [0,10,15,18]

robot(40, A)
robot(20, B)
robot(20, C)