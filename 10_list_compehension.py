my_list = ['MixEd', 'caSE', 'eleMentS']
t = []
u = []
for my in my_list:
    t.append(my.lower())
# print(t)
# adding changes to a list using list comprehension.
my_list = [my.upper() for my in my_list]
# print(my_list)

a_list = [1,2,3,4,5,6,7,8,9]
# iterates a fuction over a list ie, in this case i*2
a_list = [i*2 for i in a_list]
# print(a_list)

'''Note'''
# convert a list to str using ' '.join()
# convert a str to list using 'split()'
phrase = 'Lorem ipssum dolar sit amoung consecutors adipicing'.split()
# using list comp to perform mappings. ie with 3 methoda(upper(), lower(), and len())
stuff = [[p.lower(), p.upper(), len(p)] for p in phrase]
# print(stuff)

# list comp with if-conditionals.
M = [x**2 for x in range(10+1) if x % 2 == 0]
# print(M)

# mapping
def mult(val):
    return val ** 2
mapping = range(10+1)
i = map(mult, mapping)
print(list(i))