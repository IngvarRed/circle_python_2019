#
import sys
from pprint import pprint

args = sys.argv

print(args)

if len(args) == 3:
    dict_file_name = args[1]
    text_file_name = args[2]
else:
    print('i need more arguments')
    exit(1)

print(dict_file_name)
print(text_file_name)

print(sys.getwindowsversion())
print(sys.path)
for i in sys.path:
    print(i)

pprint(sys.path)

dd = {12: sys.path, 1234: 'asda', 'sdfsfd': 13}

pprint(dd)

print(sys.float_info)
