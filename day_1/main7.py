# Given a list of integers, find the sum of all positive numbers

sample = [3,2,0,-3,-6,-67,-11,-5,9,55]
positive = 0
for i in sample:
    if i > 0:
        positive = positive + i
print(positive)