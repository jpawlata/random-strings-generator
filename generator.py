from secrets import choice
import string as st

lenght = int(input("Number of characters: "))

def string_generator(lenght):
    chars = st.ascii_letters + st.digits
    string = ''.join(choice(chars) for i in range(lenght))
    return string

string = string_generator(lenght)
print(string)