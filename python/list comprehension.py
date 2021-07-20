myList = list(range(1, 11))
print(myList)

'''
mySquares = []

for i in myList:
    if i%3 == 0:
        mySquares.append(i ** 2)
'''

mySquares = [i ** 2 for i in myList if i%3 == 0]

print(mySquares)