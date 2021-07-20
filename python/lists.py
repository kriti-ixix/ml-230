myList = [1, 2, 3, 4.5, 10.256, "Hi", "How are you", True, False]

#List Indexing
print(myList[5])
print(myList[-1])

#Overwriting an element
myList[6] = "Good morning"
print(myList)

#List Slicing
print(myList[2:7])
print(myList[2:7:3])

#Nested Lists
myNestedList = [1, 2, 3, [4, 5, 6, "Hi"], True, "Hello"]
print(myNestedList[3][2])

#Appending to a list
newList = []

for i in range(5):
    newList.append(input("Enter an element: "))

print(newList)

#Inserting element in a list
newList.insert(1, 100)
print(newList)

#Remove element from a list
l1 = ['a', 120, 'b', 5, 10, True]
remove1 = l1.pop()
print(l1)
remove2 = l1.pop(0)
print(l1)
print("Removed values:", remove1, remove2)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'b', 'b']
alphabets.remove('b')
print(alphabets)
print(len(alphabets))

#Sorting the list
myList = [10, 40, 50, 100, 35, 17]
myList.sort()
print("Sorted List:", sorted(myList))
print("Original List:", myList)
sortedList = sorted(myList, reverse=True)
print("Reverse Sorted List:", sortedList)

for element in myList:
    print(element)