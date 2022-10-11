# tup = [12],
# print(tup[0].append(121))
# print(tup)

sq = lambda x:x**2

add = lambda *args:sum(args)

print(sq(12))
print(add(1,2,3,4))


numbers = [12, 43, 56, 21, 89, 40, 81]
newNums = map(lambda x:x*2, numbers)
evNums = filter(lambda x:x%2==0, numbers)
print(list(newNums))
print(list(evNums))

lstCmr = [i for i in numbers if i%2!=0]
print(f'list comprehension: {lstCmr}')
names = ['wreet', 'mridul', 'pritam', 'shishir', 'partho']
cmrNames = [name for name in names if len(name)>6]
print(f'Long names: {cmrNames}')

# iterNums = iter(list(newNums))
# while next(iterNums):
#     print(next(iterNums))
print(type([]))