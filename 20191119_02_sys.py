import sys

args = sys.argv

print(args, len(args))
try:
    print(args[1])
except Exception:
    print('You have no 2 arguments')
    exit(1)