def add(*args):
    sm = 0
    print(args)
    for i in args:
        print(i)
        sm += i
    return sm
add(1,2,3,4)
# print(add(1, 2, 3, 4))