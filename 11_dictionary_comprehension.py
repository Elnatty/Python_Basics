dict1 = {'ay':1, 'bee':2, 'cee':3}

# the dict comp uses the dict curly braces and the '.items()' method
dic2 = {a:b for a,b in dict1.items()}
# print(dic2)

# list comp with files
lan = list(open('C:/Users/lang.txt'))
print(lan)
new = [i.replace('\n', '') for i in lan]
# or use rstrip() to get rid of the \n
neww = [i.rstrip() for i in lan]
print(neww)