#Variable declaration
num1 = float(input("Enter first number: "))
num2 = float(input("Enter Second number: "))

sum_result = num1 + num2
diff_result = num1 - num2
mul_result = num1 * num2 
div_result = num1 / num2 
mod_result = num1 % num2 
exp_result = num1 ** num2
flr_result = num1 // num2 

print(sum_result)
print(diff_result)
print(mul_result)
print(div_result)
print(mod_result)
print(exp_result)
print(flr_result)

print(f"sum: {num1} + {num2} = {sum_result}")
print(f"Difference: {num1} - {num2} = {diff_result}")
print(f"Multiplication: {num1} * {num2} = {mul_result}")
print(f"Division: {num1} / {num2} = {div_result}")
print(f"Modulus: {num1} % {num2} = {mod_result}")
print(f"Exponential: {num1} ** {num2} = {exp_result}")
print(f"Floor Division: {num1} // {num2} = {flr_result}")