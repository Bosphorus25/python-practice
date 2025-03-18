#  Write a Python program to check if a given string is a 
# pangram (contains all letters of the alphabet)
import string
sentence = set("ghijklmnabcdefopqrstudirjvwxyzz")
letters = set(string.ascii_lowercase)
if sentence >= letters:
    print("its pangram")
else:
    print("its not pangram")