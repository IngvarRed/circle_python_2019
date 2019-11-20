def get_third(l):
    if len(l)<3:
        raise ValueError('List is too short')
    return l[2]

try:
    print(get_third([1,2,3,4,5]))
    print(get_third([1,2]))
except ValueError as e:
    print('Error ', e)

print('Do something on exit')