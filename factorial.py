#Factorial of the number 
#3! = 3 * 2 * 1

num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for the negative number")
elif num == 0:
    print("Factorial for 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print(f'The factorial of num is {factorial}')
