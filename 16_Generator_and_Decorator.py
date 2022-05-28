'''
---->> Generator: is like a resumable function, that instead of running through an iterable
just all at once and returning a single object, we can just actually stop and resume,
ie basically save state in a function execution.

---->> Decorators: are functions you can use to wrap other functions.
Decorators are functions that take another functions as its argument.
'''


'''
# ---->> generator function
def gensq(n):
    for i in range(n):
        yield i ** 2
try:
    a = gensq(4)
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
except StopIteration:
    print('end of result..')
    
    
# ---->> using generators with list comp
# note, we use tuple bracket instead of list square brackets.
ls = (2**n for n in range(10))
print(next(ls))
print(next(ls))
print(next(ls))
print(next(ls))
print(next(ls))    
'''


# ---->> Decorators
