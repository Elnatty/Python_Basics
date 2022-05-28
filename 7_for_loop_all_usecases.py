# a for loop is a counting loop, which cycles or loops through an iterable.
# a for loops iterates through a finite sequence.
# an iterable could be a string, list, tuple, <dictionary>, also a <range>.

# using string 'python' as our iterable in this case.
for l in 'python':
    # print(f'current letter is: {l}')
    # pass is used to skip.
    pass

# using list as our iterable.
for veg in ['celery', 'orko', 'mushroom']:
    # print(f'current vegetable is: {veg}')
    pass

# using range.
for i in range(5):
    # range(5) loops through from 0-4 but not include 5
    # print(f'{i}')
    pass

# using tuples as iterables.
for a,b in [(1,2), (3,4), (5,6)]:
    # print(a,b)
    pass

# useful for system admins.
import os
# all environment variables that are relevant under the currently logged-in user
for k, v in os.environ.items():
    # print(f'{k} = {v}')
    pass

# using files as iterables.
f = open('Important_Notes.txt')
for line in f:
    # print(line)
    pass

# using dictionaries as iterables.
for k, v in {'key1':'value1', 'key2':'value2', 'key3':'value3'}.items():
    # print(f'{k} = {v}')
    pass



# using embedded elements.
i = ['abc', 123, (5,6), 4.20]
query = [(10,20), 3.14, (5,6)]
for key in query:
    if key in i:
        # print(f'{key}, was found.')
        pass
    else:
        # print(f'{key}, not found.')
        pass


# using range as iterable to create a multiplication table.
for mult in range(1,5+1):
    for i in range(1,12):
        #print(f'{mult} * {i} = {mult * i}')
        pass
    #print('')