def multy(*args):
    print(args)


def kwfunc(**kwargs):
    for e, r in kwargs.items():
        print(e, r)


kwfunc(apple='яблоко', plum='слива')

a = [1, 2, 3]
multy(1)
