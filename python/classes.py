class Student: #Parent or Base Class

    #Called whenever an object is created to initialise it
    def __init__(self, n, r):
        self.name = n
        self.rollno = r

    #Called whenever we print an object
    def __str__(self):
        return str(self.rollno) + ". " + self.name


class Marks(Student): #Child or derived class
    
    def __init__(self, n, r, s, m):
        Student.__init__(self, n , r)
        self.subject = s
        self.marks = m


s1 = Student("ABC", 10, 50)
s2 = Student("XYZ", 35, 45)
s3 = Student("PQR", 5)

# s1.name = "ABC"
# s1.rollno = 10
# s1.marks = 50

# s2.name = "XYZ"
# s2.rollno = 35
# s2.marks = 45

print(s1)
print(s2)
print(s3)