myString = "Hello world!"
myString2 = "How are you?"

#String Indexing
print(myString[2])
print(myString[7])
print(myString[-1]) #Negative Indexing

#String slicing
#string[start=0 : stop=len(exclusive) : step=1]
print(myString[2:8])
print(myString[2:8:2])
print(myString[::-1]) #Reverse a string

#Length of a string
print(len(myString)) 

#String concatenation
print(myString + " " + myString2)

#String casing
print(myString.upper())
print(myString.lower())

#String splitting
print(myString.split())
print(myString2.split())

tweet = "Good morning #niceweather #feelinggood #sunny"
print(tweet.split("#"))
print(tweet.split("#", 1))

for x in myString:
    print(x)