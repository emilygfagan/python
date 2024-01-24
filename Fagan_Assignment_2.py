# Assignment 2: Write a function area_of_circle which returns the area of a circle of radius r.

r_str = input("Enter radius: ")

r = int(r_str)

def area_circle(r):
    pi = 3.14159
    area = pi * r**2
    return area

print(area_circle(r))