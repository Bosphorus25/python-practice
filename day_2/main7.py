#  Implement a program that converts a given number of 
# minutes into hours and minutes
time = int(input("entre minutes here: "))
hour = time // 60 
minutes = time % 60 
print("hours ", hour, "minuts ", minutes)