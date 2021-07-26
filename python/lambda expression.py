def times10(x):
    return x * 10

myList = list(range(1, 11))
#print(myList)

#print(list(map(times10, myList)))

l = lambda x : x * 10

print(l(20))

print(map(l, myList))