def hello():
    print("hello world")

def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks for using this func")
    return mfx

@greet
def hello():
    print("hello world")

def add(a, b):
    print(a+b)


hello()