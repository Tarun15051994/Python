'''
Swap two number or multiple numbers
'''

a = float(input("Enter the value of the first variable: "))
b = float(input("Enter the value of the Second variable: "))
#Display original value 
print(f"Original value a = {a}, b = {b}")

#swap the values 
a, b = b, a
#Display swap value 
print(f"Swap value a = {a}, b = {b}")