#
import sys

args = sys.argv

try:
    file_name = args[1]
    with open(file_name) as f:
        text = f.read()
        # One more example
        # text = ''
        # for line in f:
        #     text += line
except IndexError:
    print('''
Usege: example.py file_name

file_name -- is a file for read
    ''')
    exit(1)
except IOError as e:
    print('There is no file')
    exit(2)

print('*' * 40)
print(text.strip())
print('*' * 40)

print('I CAN DO UT :) ')
print('no errors!!!')
exit(0)
