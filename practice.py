import random
import string

def pass_gen(length=12):
    char = string.ascii_letters + string.digits + string.punctuation + string.printable
    passw = ''.join(random.choice(char) for i in range(length))
    return passw

print(f"your new secure password is {pass_gen(16000)}")

