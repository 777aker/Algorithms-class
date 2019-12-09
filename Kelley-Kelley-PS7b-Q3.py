# function definition, takes in the citations
def hindex(citations):
    if len(citations) == 1 and not citations[0] == 0:
        return 1
    elif len(citations) == 1:
        return 0
    hindexVal = hindex(citations[:len(citations)-1])
    if citations[len(citations)-1] >= len(citations):
        return len(citations)
    return hindexVal

# test arrays
tester1 = [5, 4, 3, 2, 1]
tester2 = [20, 19, 18]
tester3 = [40]
tester4 = [8, 4, 2]
tester5 = [6, 5, 4]
tester6 = [0]
tester7 = [0, 0, 0]
tester8 = [1, 1, 1]

# printing the results of the tests, all passed yay, even tester4
print(hindex(tester1))
print(hindex(tester2))
print(hindex(tester3))
print(hindex(tester4))
print(hindex(tester5))
print(hindex(tester6))
print(hindex(tester7))
print(hindex(tester8))
