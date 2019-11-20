#
import  collections

counter = collections.Counter('h o m o l t r a h o'.split(' '))
rez = dict(counter.most_common(2))
print(counter.most_common(2))
print(rez)
print(counter)
print('h is ', counter['h'])
var = set(counter)
print(var)
print(len(var))
