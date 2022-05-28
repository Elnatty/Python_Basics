'''
How to Make a professional Python script with functions for importing into other python files

"""
module name is the name of the python script.
Module Name: acct_number_generator.py
Author: DKING
Contact: lordnattyguru1916@gmail.com
Desc: The w() function prints 20 empty lines by default.
"""
# then create your function
def wip():
    print('\n' * 20)
'''


# import the name of the python script.
from Dking_Codes.DKing_Mobile_Banking import acct_number_generator

'''the dir() outputs the methods/functions available for the imported script.'''
# print(dir(wiper))

'''help() is used to get full documentation details of script file.'''
# print(help(wiper))

'''.__doc__ is used to get documentation for a particular python script..'''
print(acct_number_generator.__doc__)