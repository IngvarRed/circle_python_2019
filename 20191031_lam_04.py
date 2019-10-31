#
l = [['samba', 22], ['banana', 100], ['que', 12]]

l1 = sorted(l)
print(l1)

l2 = sorted(l, key=lambda x: x[1])
print(l2)

l3 = sorted(l, key=lambda x: len(x[0]))
print(l3)

lll = [-2, 4, 10, 25, 0, -7]
print(sorted(lll))
print(sorted(lll, key=lambda x: abs(x)))
