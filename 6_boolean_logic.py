#!usr/bin/python

a = 50
b = 25
c = 'spam'
d = int(input('input a number >>> '))
# (a is d) will output True if the user inputs 50 which is the value of a.
print(f'{a==b}\n'       # outputs False
      f'{b<=a}\n'
      f'{a!=b}\n'
      f'{a is d}')