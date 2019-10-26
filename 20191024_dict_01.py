#
dd = {}
print(dd, "==>", type(dd))
dd['ivan'] = "Galyts'ka str. 12"
dd[2] = "Nezaledjnosti str. 1"

print(dd)
for key in dd:
    print(key, "==> ", dd[key])

print('*' * 30)
del dd[2]
print(dd)
dd[1] = ()
print(dd)
print(len(dd))
print(dd.keys())
print(dd.values())