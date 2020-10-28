from secrets import choice
import string as st


def string_generator():
    # User's input validation
    while True:
        lenght = input("Number of characters: ")
        try:
            lenght = int(lenght)
            break
        except ValueError:
            print("Please enter a number")

    # Generate random string
    chars = st.ascii_letters + st.digits
    string = ''.join(choice(chars) for i in range(lenght))
    return string

string = string_generator()
print(string)