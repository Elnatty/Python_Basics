#!/usr/bin/python

# exception handling.
try:
    # num = int(input('input a number >>> '))
    n = str(input('what is your name: '))
    # python recognises this conditional only when num is less than 0
    # if num < 0:
    #     print(f'The absolute value of {num} is {-num}')
    if n[0] == 'a':
        print(f'we checked your 1st letter which is {n[0]}')
    # python recognises this conditional when num is greater than 0
    else:
        print(f'your 1st letter is {n[0]}')
        # print(f'The absolute value of {num} is {num}')
except ValueError:
    print(f'Invalid input,  try again...')