# * args    =  allow you to pass multiple non key arguments
# ** kwargs =  allow you to pass multiple keywords arguments 


# def print_add(**kwargs):
#     for value in kwargs.values():
#         print(value)


# print_add(street="main road",
#                 city="jbp",
#                 state="mp",
#                 zip="1234")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    for value in kwargs.values():
        print(value, end=" ")

shipping_label("DR ","SPONGEbOB",
               street= "124",
               apt="100",
               state= 'MI')