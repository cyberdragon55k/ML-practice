import random 
def start_game():
    number_to_guess = random.randint(1,10)
    attempts = 0
    print("I'm thinking of a number between 1 and 10")
    

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("too low ! ")
            elif guess > number_to_guess:
                print("too high ! ")
            else:
                print(f"correct! you got it in {attempts} guesses.")
                break
        except ValueError:
            print("please enter a valid number. ")

if __name__ == "__main__":
    start_game()


    #ooooooo