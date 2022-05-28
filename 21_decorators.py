'''
--->>> DECORATORS: adds extra features to an already existing function.
'''

# a default or existing function.
def div(a, b):
    print(a/b)

# but we want to make it smarter, by making sure a larger integer always comes 1st when dividing, ie: if div(2,4) is passed, we want
# it to automatically swap larger integer to appear 1st. so, (4,2), now we can use decorators to make this happen.

# 1st create another function, which takes on an argument.
def smart_div(func):
    # create the function/extra feature you want to add to already existing div function.
    def inner_div(a, b):
        if a < b:
            # swap the values.
            a, b = b, a
        # return the result.
        return func(a,b)
    # return/call the inner function just like calling normal function.
    return inner_div

div = smart_div(div)
div(2, 4)





# example 2:
# default function
def multiply(x, y):
    print(x*y)

# decorator
def smart_multiply():
    # inner func
    def inner_multiply(x, y):
        # extra feature
        res = f'{x} raised to power of {y} = {x**y}'
        print(res)
    return inner_multiply

multiply = smart_multiply()
multiply(2, 5)