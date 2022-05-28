import builtins
# print(dir(builtins))
# print(help(builtins.len))

''' java2s.com '''

# *args are basically used for specifying any amount of input parameter inside the function header.
# *kwargs are basically used for specifying any amount of default parameter inside the function header.
def foo(*args, **kwargs):
    print('This is "*args":', *args)
    print('This is "*kwargs":', *kwargs)
# foo()

# example of a function with multiple arguments.. (*args):
def sum(a, *b):
    print('value of a is >>', a)
    print('value of b is >>', b)
    # to sum everything..
    # we 1st assign the value of a to another variable..
    c = a
    # then use for loop to iterate through the value of b which is a tuple.
    for i in b:
        c = c + i
    print('value sum is >>', c)
# sum(1,2,3,4,5,6,7)



# example of a function with multiple k'arguments.. (*kwargs):
# ** represents multiple arguments with the help of keywords, i.e: **kwargs..
def person(name, **data):
    print(name)
    print(data)

# person('name', age=28, city='mumbai', zip=9678695)

'''
Note:  
       *args gives results in TUPLE while 
       **kwargs gives result in DICTIONARY.
'''


# example 3:
def personn(name, **data):
    for i, j in data.items():
        print(i + ':', j)


# personn('Nathan', age=25, city='Abuja', zip=9654895)