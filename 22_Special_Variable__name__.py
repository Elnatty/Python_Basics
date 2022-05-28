
def my_func():
    print('Welcome User to MY Code...')

if __name__ == "__main__":
    my_func()

'''
--> The whole idea here is:
    when this script is executed, it runs the my_func.
    but..
    when this script is imported as a module to another script, it wont run unless called. ie, from script_name import my_func. then
    you call it. my_func() --> now it executes the function from another script.
'''