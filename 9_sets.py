# sets
# unordered collection of unique immutable element
# not a sequence (str, list, tuple), not a mapping(dict)
# sets are commonly referred to as valueless dictionary, ie a key only dictionary type.
#  sets isolate uniques.

s1 = set([0, 2, 4, 6])
s2 = ([10, 12, 14, 16])

new_set = s1.union(s2)  # union or update
# new_set.pop()           # pop removes 1st element in the list/set.
# new_set.remove(10)       # remove a discreet element we use the '.remove'
# 6 in new_set            # checking for membership
# new_set.clear()  # clear a set
new_set.add(20)  # adds items to set.

# for new in new_set:     # iterating through a set
#     print(new)

# set comprehension
# uses the curly braces like dictionary
setcomp = {i * 2 for i in s2}
# print(setcomp)]
