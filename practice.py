def fo(a,b=2,*args, **kwargs):
    print(a,b)
    for arg in args:
        print(args)
    for key in kwargs:
        print(key,kwargs[key])


fo(1, 2, 3, 4,5,six=6,seven=7)


def add(a,b):
    print(a + b)

add(9,5)
