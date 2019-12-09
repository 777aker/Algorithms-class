import numpy as np

def epic(cards, i, j, memoize):
    # takes in our set of cards
    # i is the left end, j is the right end
    # memoize is the table of stored solutions

    # this is our memoization, if we have an answer then return
    # memoization allows us to meet the required runtime
    if not memoize[i][j] == 0:
        return memoize[i][j]

    # so if j-i = 1, then we are at a base case of there
    # only being two cards to choose from
    # here we can act greedily
    if j-i == 1:
        # if the left is less then the right then take the left
        if cards[i] < cards[j]:
            # store and return results
            memoize[i][j] = cards[i], cards[j]
            return cards[i], cards[j]
        # if both are equal if value
        elif cards[i] == cards[j]:
            # pick one at random
            if np.random.randint(0, 1):
                # store and return the results
                memoize[i][j] = cards[i], cards[j]
                return cards[i], cards[j]
            else:
                # store and return the results
                memoize[i][j] = cards[j], cards[i]
                return cards[j], cards[i]
        # this means the right was bigger than the left so take it
        else:
            # store and return the results
            memoize[i][j] = cards[j], cards[i]
            return cards[j], cards[i]

    # now for our real algorithm
    # lets first take the card on the left
    # assuming we took the one on the left, figure out
    # what the greedy person did
    # if they took the one on the left
    if cards[i+1] < cards[j]:
        # then call epic without the two cards on the left
        left, p2l = epic(cards, i+2, j, memoize)
        # add to p2l what they took
        p2l += cards[i+1]
    # if both sides had the same value, then lets assume the
    # greedy player chose randomly
    # depending on what they chose call epic without the card
    # p1 and p2 chose
    elif cards[i+1] == cards[j]:
        if np.random.randint(0, 1):
            left, p2l = epic(cards, i+2, j, memoize)
            p2l += cards[i+1]
        else:
            left, p2l = epic(cards, i+1, j-1, memoize)
            p2l += cards[j]
    # the right card was bigger so call epic with them taking
    # the right card
    else:
        left, p2l = epic(cards, i+1, j-1, memoize)
        p2l += cards[j]
    # we took the left card so add it to the results of taking
    # the left card
    left += cards[i]

    # this is if we take the card on the right
    # its the exact same thing as taking on the left
    if cards[i] < cards[j-1]:
        right, p2r = epic(cards, i+1, j-1, memoize)
        p2r += cards[i]
    elif cards[i] == cards[j-1]:
        if np.random.randint(0, 1) == 0:
            right, p2r = epic(cards, i+1, j-1, memoize)
            p2r += cards[i]
        else:
            right, p2r = epic(cards, i, j-2, memoize)
            p2r += cards[j-2]
    else:
        right, p2r = epic(cards, i, j-2, memoize)
        p2r += cards[j-2]
    right += cards[j]

    # so if the left gave a better solution use that
    if left < right:
        # store and return our solution
        memoize[i][j] = left, p2l
        return left, p2l
    # if left and right have the same results, then pick one randomly
    elif left == right:
        if np.random.randint(0, 1) == 0:
            memoize[i][j] = left, p2l
            return left, p2l
        else:
            memoize[i][j] = right, p2r
            return right, p2r
    # if the right was better then use the right as our solution
    else:
        memoize[i][j] = right, p2r
        return right, p2r


# test cases from the homework and piazza
# passed :)
cards = [4, 2, 6, 5]
table = [[0]*len(cards) for i in range(len(cards))]
print(cards)
print(epic(cards, 0, len(cards)-1, table))
print('----------------')
# passed :)
cards = [9, 8, 10, 9]
table = [[0]*len(cards) for i in range(len(cards))]
print(cards)
print(epic(cards, 0, len(cards)-1, table))
print('----------------')
# passed :)
cards = [35, 83, 47, 37, 90, 10, 13, 2, 96, 50, 93, 36, 64, 95]
table = [[0]*len(cards) for i in range(len(cards))]
print(cards)
print(epic(cards, 0, len(cards)-1, table))
print('----------------')
# passed :)
cards = [2, 2, 2, 2]
table = [[0]*len(cards) for i in range(len(cards))]
print(cards)
print(epic(cards, 0, len(cards)-1, table))
print('----------------')

# now just random test cases of size 100 ranging from 1 to 100
print("Simulation of 100 cards with values 1 to 100")
cards = np.random.randint(1, 100, 100)
table = [[0]*len(cards) for i in range(len(cards))]
print(cards)
print(epic(cards, 0, len(cards)-1, table))
print('----------------')