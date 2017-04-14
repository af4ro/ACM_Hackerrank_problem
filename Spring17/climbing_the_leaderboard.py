#!/bin/python3

import sys


n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

scores.append(0)
n+=1
result= []
rank = 1
counter1 = 0
counter2 = m-1
previous = float("inf")
while(counter2>=0 and counter1<n):
    if scores[counter1] == previous:
        counter1+=1
        continue
    if alice[counter2]>=scores[counter1]:
        result.append(rank)
        counter2-=1
        continue
    rank+=1
    previous = scores[counter1]
    counter1+=1

for j in reversed(result):
    print(j)