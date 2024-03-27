'''
Armstrong number
'''

num = int(input("Enter a number: "))

#get the length of the string
str_num = str(num)
len_num = len(str_num)

#temp_variables
sum_of_num = 0
temp_num = num

while temp_num > 0:
    digit = temp_num % 10 
    sum_of_num += digit**len_num
    temp_num //= 10

if sum_of_num == num:
    print(f"{num} is Armstrong number")
else:
    print(f"{num} is not Armstrong number")