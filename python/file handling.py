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