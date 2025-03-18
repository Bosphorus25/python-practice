#Write a program to check if a number is prime
num = int(input("entre number here: "))
if num == 1:
    print("its not prime")
else:
    is_prime = True
    for i in range (2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print("its prime")
else:
    print("its not prime")