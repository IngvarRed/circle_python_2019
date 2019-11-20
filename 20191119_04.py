class MyValueError(Exception):
    def __init__(self, message, ll=[]):
        self.mes = message
        self._list = ll

    def __str__(self):
        return self.mes + ' ' + str(self._list)

def get_third(l):
    if len(l)<3:
        raise MyValueError('List is too short')
    return l[2]

try:
    print(get_third([1,2,3,4,5]))
    print(get_third([1,2]))
except MyValueError as e:
    print('Error ', e)

print('Do something on exit')