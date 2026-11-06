import random
attempts=7
def display_rules():
    print("Welcome to Number Guessing Game!\n")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it.\n")
def play (number , attempt=1):
    if attempt>attempts:
            print("\nGame Over!")
            print("The correct number was:", number)
            return
    guess= input(f"attempt{attempt}/7 -enter your guess:")

    try:
         guess=int(guess)
    except ValueError:
           print("Please enter a valid number.\n")
           return play(number, attempt) 
    if guess<1 or guess>100:
              print("Please enter a number between 1 and 100.\n")
              return play(number, attempt)
    check= lambda x,y :"correct" if x == y else (
        "low" if x < y else "high"
    )
    result = check(guess, number)
    if result =="correct":
           print("\nCongratulations! You guessed the correct number!")
           print("You guessed it in", attempt, "attempt(s).")
           return
    if result == "low":
        print("Too Low! Try a higher number.\n")
    else:
        print("Too High! Try a lower number.\n")
    play(number , attempt+1)


display_rules()

random_number = random.randint(1, 100)

play(random_number)
               

