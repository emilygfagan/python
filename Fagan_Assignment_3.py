# Assignment 3: Write a function which is given the day number, and it returns the day name (a string).

user_str = input("Enter a number from 0-7: ")

user_int = int(user_str)

def day_of_week(user_int):
    if user_int == 0:
        print("Sunday")
    elif user_int == 1:
        print("Monday")
    elif user_int == 2:
        print("Tuesday")
    elif user_int == 3:
        print("Wednesday")
    elif user_int == 4:
        print("Thursday")
    elif user_int == 5:
        print("Friday")
    elif user_int == 6:
        print("Saturday")
    else:
        print("Number not in range, try again.")

day_of_week(user_int)