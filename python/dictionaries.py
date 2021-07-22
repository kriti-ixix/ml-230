'''
{ key : value, key1 : value1 }
'''

student = {'name':'ABC', 'roll no': 25, 'gender':'M', 'pass':True}

print(student['name'])
print(student['roll no'])
print(student['pass'])

#Overwriting a value
student['roll no'] = 19
print(student)

#Adding a key to the dictionary
student['subject'] = 'Python'
print(student)

info = ['name', 'roll no', 'pass', 'gender']

newDict = {}

for key in info:
    newDict[key] = input(key + ": ")

print(newDict)

for x in student: #Returns only the keys
    print(x)

print(student.keys())
print(student.values())
print(student.items())

for x in student.items():
    print(x)

#Dictionary unpacking
for (k, v) in student.items():
    print("Key:", k, "Value:", v)