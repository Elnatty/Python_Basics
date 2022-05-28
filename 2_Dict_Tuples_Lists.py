tup = ('one', 'two', 'two', 'three', 'four', 'five')
# tuples can also be indexed/sliced like strings.
# tuples are immutable. ie can't be expanded like lists.
# tuples methods are very few. ie count and index.
print(tup[1:5])
# the count method shows the number of occurrence of a particular item in the tuple.
# print(tup.count('two'))
# The index method displays the index of the item.
print(tup.index('four'))





"""
>>> LISTS:
lists are mutable, can be indexed/sliced. list has many methods unlike tuples. ie, append, count, extend,\
index, insert(inserts as positional index), pop or remove, sort, reverse."""

lis = ['Moses', 'Favour', 'Bimbo', 'Favour', 'eggs']
lis.append('Daniel')
# print(lis)
# to use the insert method, you pass in two arguments, ie index number and item you want to add/insert.
lis.insert(0, 'Beginning')
# print(lis)
# lis.reverse()
# sorting, using sorted..
sorting = ['Moses', 'Favour', 'Bimbo', 'Favour', 'Eggs']
print(sorted(sorting, reverse=False))
print('\n' * 5)





'''Dictionary.
# slicing is not allowed in dictionary.
# Note List, Strings and Tuples are all 'Sequences' because they consist of an ordered sequence index sequence of
# objects/items. Dictionaries are Mutable but an Unordered set of non-individual items but what are called key:value pairs.'''
dictionary = {'one': 1, 'two': 2, 'three': 3}
# adding to a dictionary by assignment.
dictionary['four'] = 4
print(dictionary)
# grabbing key pairs and converting to list.
key_dictionary = list(dictionary.keys())
print(key_dictionary)
# grabbing value pairs and converting to list.
key_dictionary = list(dictionary.values())
print(key_dictionary)
# you can map a tuple into a dictionary.
tup = ('January', 'February')
dictionary['four'] = tup
# print(dictionary)
# removing items in dictionary.
dictionary.pop('four')
# print(dictionary)