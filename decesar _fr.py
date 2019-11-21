'''
open a file to read,
    such as 'story.txt'
read text
pick up punctuation
split by ' '
set the key
    convert word
    find the word in the dictionary 'words.txt'
    change the key rating
the highest rated key is the correct one
decode text
'''

import string
import sys
import operator


def key_to_dict(key):  # create encryption dictionary
    str_arr = string.ascii_lowercase
    str_arr2 = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
    str_arr += string.ascii_uppercase
    str_arr2 += string.ascii_uppercase[key:] + string.ascii_uppercase[:key]

    cliper_dict = {}
    for k, v in zip(str_arr, str_arr2):
        cliper_dict[k] = v
    return cliper_dict


def decript_text(decr_dict, encr_text):  # decrypt text
    decr_text = ''
    for letter in encr_text:
        if letter in decr_dict:
            decr_text += decr_dict[letter]
        else:
            decr_text += letter
    return decr_text


# open a file to read
# argss = sys.argv
args = ['a', 'story.txt']

try:
    file_name = args[1]
    with open(file_name, 'r') as file_text:
        original_text = file_text.read()
except IndexError:
    print("""
Usage: decesar_fr.py file_name
    file_name  -- is a file for read 
    """)
    exit(1)
except IOError as e:
    print("There is no file ")
    exit(2)
except Exception as e:
    print("Error is ", e)
    exit(3)

# pick up 'spaces'
text = original_text.strip()
# pick up punctuation
for symbol in string.punctuation:
    text = text.replace(symbol, "")
# split by ' '
words = text.split()

with open('words.txt', 'r') as wl:
    word_file = wl.read()
# split by ' '
word_list = word_file.split()

# set the key
new_dict = {}
key_rate = {}
for n_key in range(0, 27):
    rate = 0
    new_dict = key_to_dict(n_key)
    # convert word
    for word in words:
        # convert word
        decr_word = decript_text(new_dict, word)
        # find the word in the dictionary 'words.txt'
        if decr_word.lower() in word_list:
            rate += 1
    # change the key rating
    key_rate[rate] = n_key

# the highest rated key is the correct one
optimal = max(key_rate.keys())
# decode text
decode = decript_text(key_to_dict(key_rate[optimal]), original_text)
print(decode)

