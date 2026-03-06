import random 
def guess_the_number():
    secret_number = random.randint(1,100)
    attempts = 5

    print("I'm thinking of a number btw 1 and 100.")
    while True:
        guess = int(input("take a guess : "))
        attempts +=1

        if guess <secret_number:
            print("too low")
        elif guess > secret_number:
            print("too high")
        else:
            print(f"correct number {attempts} tries.")
            break
guess_the_number()

#11234567

# EXAM