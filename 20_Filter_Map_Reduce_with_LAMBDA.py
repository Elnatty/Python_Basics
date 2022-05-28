# working with filter, map and reduce with the help of reduce.
'''
--->>> MAP: applies a function to all the items in an input_list. eg: print(list(map(funct_to_apply, list_of_input)))
--->>> FILTER: creates a list of elements for which a function returns true. eg:
                num = range(-5, 5)
                print(list(filter(lambda x: x < 0, num)))
--->>> REDUCE: for performing some operations on list and returning the results. It applies a rolling pair computation to
                sequential pairs of values in a list. for example: instead of doing this...
                p = 1
                lis = [1,2,3,4]
                for l in lis:
                    p = p * l
                print(p)

                we do this instead.
                from functools import reduce
                product = reduce((lambda x, y: x * y), ([1,2,3,4]))
                # outputs 24.
'''



# given a list of random numbers, get the even numbers, using filter function.
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# solution.
# define a function to check for even numbers, or you can use a lambda expression.

# call the function and the object of interest.
even = list(filter(lambda n: n % 2 == 0, nums))
print(even)

# using mapping
doubles = list(map(lambda n: n*2, even))
print(doubles)

# lets sum all values of doubles together or (reduce) using the functools module.
from functools import reduce
sum = reduce(lambda a,b: a+b, doubles)
print(sum)