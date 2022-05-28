# # convert string to list using >>> split(',') outputs ['Cbt Nuggets']
sentence = 'Cbt Nuggets'
print(sentence.split(','))
# # convert string to list using >>> split(' ') outputs ['Cbt', 'Nuggets']
print(sentence.split(' '))


# String slicing...
# all prints out same results...
a = 'Giant'
# 2 represents the index, then 5 is "count to but not including 5" ie 'ant'
print(a[2:5])
print(a[-3:5])
print(a[-3:])