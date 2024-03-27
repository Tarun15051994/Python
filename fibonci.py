"""
Fibonacci Series
0,1,1,2,3,5,8,13,21,34,65,79,144 and so on
"""

nterm = int(input("Enter many terms: "))

num1 = 0
num2 = 1
count = 0

if nterm < 0:
    print(f"Enter only positive number")
elif nterm == 1:
    print(num1)
else:
    print("Print Fibonacci Series:")
    while count < nterm:
        print(num1)
        num = num1 + num2
        num1 = num2
        num2 = num
        count += 1
