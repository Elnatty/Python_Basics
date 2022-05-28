# while loops is more like a continual evaluation, ie you open up a while loop with some test that must evaluates to boolean true before it continues.
# be careful because it can result to an infinite loop.

x = 0
y = 13
# while x < y:
#     print(f'x + y = {x}')
#     # incrementing value of x by 1 after every iteration.
#     x += 1
#     # using break and continue with conditionals
#     if x == 2:
#         print(f'current value of x is "{x}"')
#         user_response = input('do you want to continue or not, [y] or [n] >>> ').lower()
#         if user_response == 'y':
#             # if response is 'y', code continues running.
#             continue
#         else:
#             print('good bye..')
#             # break terminates the program.
#             break
#     elif x == 5:
#         print(f'current value of x is "{x}"')
#         user_response = input('do you want to continue or not, [y] or [n] >>> ').lower()
#         if user_response == 'y':
#             # if response is 'y', code continues running.
#             continue
#         else:
#             print('good bye..')
#             # break terminates the program.
#             break



add = 1
guess = 6
while guess > 0:
    guess -= 1
    print('add = %d' % add)
    print(f'{guess} guesses left')
    add += 1
