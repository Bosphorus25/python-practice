#  Create a function to count the number of vowels in a 
# given string
sentence = input("enter string hrer: ")
vowels = ("a,e,i,o,u")
total = 0
for i in sentence:
    if i in vowels:
        total = total +1
        print(total)