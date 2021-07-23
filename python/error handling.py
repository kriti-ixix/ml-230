
'''
Errors:
    1. compile time error: e.g. 
    2. Logical error: 
    3. Run time error: handle (Exceptions)
    
Error Handling:
    1.Inbuilt:
        
           Types of Errors:
        	• IndexError
        	• ModuleNotFoundError
        	• KeyError
        	• ImportError
        	• StopIteration
        	• TypeError
        	• ValueError
        	• NameError
        	• ZeroDivisionError
        	• KeyboardInterrupt
        	• FloatingPointError
        	• MemoryError
        	• OSError
            
    2. Custom
'''   

        
'''
my_list = [4,5,6,7]
print(my_list[10])    : IndexError


a= 5
b= 's'
print(a+b)            : TypeError

try:
    #code we want to execute
   a= 10
   b = 'v'
   print(a+b)
    

    
except IndexError:
    print('the list index is out of range')
    
except TypeError:
    print("both should be number")
 '''
#Another Exmaple of Inbuilt Errors
try:
    a = int(input("enter number: "))
    b = int(input("enter another number: "))
    print(a/b)
    print(a+b)
    
    
    
except KeyError:
    print('something went wrong')
except ZeroDivisionError:
    print('division with zero means infinite')
    
except Exception:
    print("wrong input")
    
finally:
    print('excecution complete')
    
    
    
    
    
    
    