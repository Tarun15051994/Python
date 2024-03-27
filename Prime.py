"""
Check whether the given number is prime
"""
#number which is divided by 1 and itself is prime number

num = int(input("Enter a number: "))

flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag or num == 1:
    print(f"{num} is not a prime")
else:
    print(f"{num} is a prime")



