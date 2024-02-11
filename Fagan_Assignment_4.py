# Write a function which is given an exam mark, and it returns a string according to the grade scheme.
""" 
Grade Scheme: 
    First --> m >= 75
    Upper Second --> [70-75)
    Second --> [60-70)
    Third --> [50-60)
    F1 Supp --> [45-50)
    F2 --> [40-45)
    F3 --> m < 40
"""

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for m in xs:
    if m >= 75:
        print(f"Mark: {m}, Grade: First")
    elif 70 <= m < 75:
        print(f"Mark: {m}, Grade: Upper Second")
    elif 60 <= m < 70:
        print(f"Mark: {m}, Grade: Second")
    elif 50 <= m < 60:
        print(f"Mark: {m}, Grade: Third")
    elif 45 <= m < 50:
        print(f"Mark: {m}, Grade: F1 Supp")
    elif 40 <= m < 45:
        print(f"Mark: {m}, Grade: F2")
    elif m < 40:
        print(f"Mark: {m}, Grade: F3")
