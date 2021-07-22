'''
Three modes:
- Reading: r
- Writing: w
- Appending: a
'''

vacationPlaces = ["New York", "Los Angeles", "London", "Paris", "Tokyo"]

vacationFile = open('Vacations.txt', 'w')

for city in vacationPlaces:
    vacationFile.write(city + "\n")

vacationFile.close()

vacationFile = open('Vacations.txt', 'a')
vacationFile.write("Canada")
vacationFile.close()

vacationFile = open('Vacations.txt', 'r')
content = vacationFile.read() #Reads the entire file in one go
print(content)

print(vacationFile.readline()) #Reads only one line
print(vacationFile.readline())

#Reads the entire file line by line
for line in vacationFile:
    print(line)

vacationFile.close()