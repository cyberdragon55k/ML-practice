# * args    =  allow you to pass multiple non key arguments
# ** kwargs =  allow you to pass multiple keywords arguments 


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("lt.", "Aditya" , "Namdev","1")