# decorator

def notify_about_calls(func):
    def decorated(*args, **kwargs):
        print("Called ", func.__name__)
        return func(*args, **kwargs)

    return decorated


def f(a, b):
    return a + b


g = f(4, 5)
print(g)
g = notify_about_calls(f)
print(g(1, 2))

# https://habr.com/ru/post/141411/
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@makebold
@makeitalic
def hello():
    return "hello habr"


print(hello())  ## выведет <b><i>hello habr</i></b>