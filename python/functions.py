def addNumbers():
    x = 5
    y = 10
    print("Sum is", x+y)

def subNumbers(x, y):
    print("Difference is:", x-y)

def multiplyNumbers(x, y, z):
    product = x * y * z
    return product

'''
Types of functions:
Paramters:
- Default
- Paramterised

Return: 
- No return type
- Return type
'''

addNumbers()
subNumbers(10, 5)
p1 = multiplyNumbers(10, 20, 30)
p2 = multiplyNumbers(100, 200, 300)

print("The products are:", p1, 'and', p2)