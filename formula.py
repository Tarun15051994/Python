#Derive area for the triangle and Square.
#formuale 
#Traingle area = 0.5*base*height
#Square area = side * side
'''
Rectangle area = length * breadth 
'''

base = float(input("enter base: "))
height = float(input("enter height: "))
length = float(input("enter length: "))
breadth = float(input("enter breadth: "))

#Area of triangle
tri_area = 0.5 * base * height

#Area of Square
sqr_area = length ** 2

#Area of Rectangle
rect_area = length * breadth

print(tri_area)
print(sqr_area)
print(rect_area)

print(f"Area of Triange for base : {base} and height : {height} is {tri_area}")
print(f"Area of square for length : {length} is {sqr_area}")
print(f"Area of Rectangle for length : {length} and breadth : {breadth} is {rect_area}")