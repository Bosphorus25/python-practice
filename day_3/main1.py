#  Write a program that checks if a given number is  
#          positive, negative, or zero

number = int(input("enter a number here: "))
if number < 0:
    print("ITS a negative number")
elif number > 0:
    print("its positive")
else:
    print("its zero")