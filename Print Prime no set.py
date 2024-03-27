#Prime number from 1 to 10

lower = int(input("Enter start number: "))
upper = int(input("Enter end number: "))

print("Prime number between", lower, "and", upper ,"are: ")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num ):
            if (num % i) == 0:
                break
        else:
            print(num)