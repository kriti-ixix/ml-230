keys = list(range(1, 11))
print(keys)

'''
{1:1, 2:4, 3:9, 4:16}
'''

# squares = {}

# for k in keys:
#     squares[k] = k ** 2

squares = {k : k ** 2 for k in keys}

print(squares)