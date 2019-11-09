# meke and append File

import sys

name_f = input("Please type Name of your file : ")

try:
    file = open(name_f)
except IOError as error_message:
    print(f'make new file {name_f}')
    file_write = open(name_f, 'w')
else:
    with file:
        print(f'open file {name_f}')
        file_write = open(name_f, 'a')

print('enter the text in a row \n press "Enter" twice to finish')
line_app = ' '
while line_app != '':
    line_app = input('>>>')
    file_write.write(line_app + '\n')

file_write.close()
