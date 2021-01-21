#!/usr/bin/python3

import random

n = 200
scores = []

# calculate separate means of both items in the score tuple
def mean(scores):
    sumReal = 0
    sumPercieved = 0
    for (real, percieved) in scores:
        sumReal += real
        sumPercieved += percieved
    return (sumReal / len(scores), sumPercieved / len(scores))

# sort by first item, the real score
def sortByReal(scores):
    scores.sort(key = lambda x: x[0])
    return scores

# generate samples
for i in range(n):
    scores.append((random.randint(0, 100), random.randint(0, 100)))

# sort samples and bucket by quartile
scores = sortByReal(scores)
firstQ = scores[:int(n/4)]
secondQ = scores[int(n/4):int(n/2)]
thirdQ = scores[int(n/2):int(n*3/4)]
fourthQ = scores[int(n*3/4):]

# print means of real and percieved scores, bucketed by real score quartiles
print(mean(firstQ))
print(mean(secondQ))
print(mean(thirdQ))
print(mean(fourthQ))
