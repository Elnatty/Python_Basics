'''
Lambda UseCase..........
1. Scalar values
This is when you want to execute a function on a single value.
(lambda x: x*2)(12) instead of:
def val(x):
    x*2
###Results
24
In the code above, the function was created and then immediately executed.
This is an example of an immediately invoked function expression or IIFE.


'''

# example 1
a = lambda x: x**x
print(a(3))

# example 2
f = lambda a,b: a + a

res = f(5, 6)
print(res)