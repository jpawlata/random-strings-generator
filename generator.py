from secrets import choice
from tabulate import tabulate
import string as st

def length_input():
    # User's input validation
    while True:
        lenght = input("Number of characters: ")
        try:
            lenght = int(lenght)
            break
        except ValueError:
            print("Please enter a number")
    return lenght   

def number_input():
    # User's input validation
    while True:
        number = input("Number of strings: ")
        try:
            number = int(number)
            break
        except ValueError:
            print("Please enter a number")
    return number   

def string_generator(lenght, number):
    # Generate random strings
    chars = st.ascii_letters + st.digits
    strings = [["".join(choice(chars) for i in range(lenght))] for num in range(number)]
    return strings


strings = string_generator(length_input(), number_input())
headers = ["Index", "Strings"]
print(tabulate(strings, headers = headers, tablefmt = "orgtbl", showindex = "always"))