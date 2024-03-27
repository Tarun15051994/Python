'''
Conversions 
kilometer to miles
Conversion factor: 1 kilometer = 0.621371 miles

Celsius to Fahrenheit
Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
'''

kilometers = float(input("Enter Kilometers: "))
miles = kilometers * 0.621371
print(f"{kilometers} kilometer is equal to {miles} miles")

celsius = float(input("Enter Temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} celsius is equal to {fahrenheit} Farhenheit")