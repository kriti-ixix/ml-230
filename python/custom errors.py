class Error(Exception):
    pass
    
class ValueTooLargeError(Error):
    pass

class ValueTooSmallError(Error):
    pass



number = 10

while True:
    try: 
        guess = int(input('Enter any guess: '))
        
        if (guess<number):
            raise ValueTooSmallError
            
        elif (guess>number):
            raise ValueTooLargeError
            
        else: 
            print('you guessed correctly')
            break
        
    except ValueTooLargeError:
        print('guess was too high')
        
    except ValueTooSmallError:
        print('guess was too small')
        
    except TypeError:
        print('type number only')
        
    except: 
        print('error')