tt = 12, "hello", 32
print(tt)
print(type(tt))
print(id(tt))
var = tt[0]
print(var)
x, y, z, = tt
print(x, y, z)

# tt[0] = 25    # false

for i in tt:
    print(i)