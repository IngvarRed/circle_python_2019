#
import string

letters = input("Text to code > ")
key = 10  # secret code

for letter in letters:
    code = ord(letter)
    new_code = ord(letter)+key
    if letter in string.ascii_lowercase:
        if new_code > ord("z"):
            new_code=new_code-26
    elif letter in string.ascii_uppercase:
        if new_code > ord("Z"):
            new_code = new_code-26
    else:
        new_code = code

    new_letter = chr(new_code)
    print(new_letter, end="")
