# decorators = a function that extends the behavior of another function w/o modify 
# the base funtion pass the base function as an argument to the decoratot
# 
#   @add_sprinkes
#   get_ice_cream(" vanilla")

def add_sprinkles(func):
    def wrapper():
        print("you add sprinkles")
        func()
    return wrapper


def add_fud(func):
    def wrapper():
        print("you add fudge")
        func()
    return wrapper

@add_sprinkles
@add_fud
def get_ice_cream():
    print("here is you ice cream")

get_ice_cream()

get_ice_cream()