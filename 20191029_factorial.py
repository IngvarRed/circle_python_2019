# 4! = 4*3*2*1
# f(n) = n* f(n-1) > 4! = 4*3! ...  1! = 1

def f(n):
    if n == 1:
        return 1
    return n * f(n-1)

print(f(4))