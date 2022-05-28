# multi-exception handler
'''
while True:
    try:
        a = float(input('First number: '))
        b = float(input('Second number: '))
        print('result is ', a/b)
    except ZeroDivisionError:
        print('zero division wont work..')
    except ValueError:
        print('Error: incorrect data type..')
    else:
        break
'''

''''
# another scenerio.
except (ZeroDivisionError, IOError, ValueError) as e:
    print('Error', e)
'''

'''
The finally block runs irrespective of try and except blocks runs or not. 
'''

class CustomError(Exception):
    pass
raise CustomError('something went wrong..')