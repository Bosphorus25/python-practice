#  Implement a program that finds the largest number
#          in a list
list1 = [2,4,5,23,57,4,5,764,4,76,235,6,5,7,8,555,3,4,7,76,678,3,45,23,41,76,12,81,19,88]
max_is = list1[0]
test = list1[ ::-1]
for i in test:
    if i > max_is:
        max_is = i 
print(max_is)