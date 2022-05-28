'''
TO convert string to list >>> we use .split().
To convert list to string >>> we use ''.join()
'''

word = 'Money is useless'
# string to list.
v = word.split()
print(v)
# convert list back to string
# we use list comprehension here.
new = [i for i in v]
# use .join() to convert string list back to string.
new_word = ' '.join(new)
print(new_word)