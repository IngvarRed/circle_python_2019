#
import string


# camelCase
# snake_case
def foo_code_cesar(ll, l_key):
    code = ord(ll)
    new_code = ord(ll) + l_key
    if letter in string.ascii_lowercase:
        if new_code > ord("z"):
            new_code = new_code - 26
    elif letter in string.ascii_uppercase:
        if new_code > ord("Z"):
            new_code = new_code - 26
    else:
        new_code = code
    new_ll = chr(new_code)
    return new_ll


letters = input("Text to code > ")
key = int(input("Type secret code > "))  # secret code

for letter in letters:
    new_letter = foo_code_cesar(letter, key)
    print(new_letter, end="", flush=True)
