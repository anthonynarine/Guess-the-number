import random
import sys

def user_guess(x):
    random_number = random.randint(1, x)
    guess = 0 #we set guess to 0 because our random # will be between 1 and x never. so we never accidently gueess accidently guess the randomly created number
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, your guess is too low.")
        elif guess > random_number:
            print ("Sorry your guess is too high")

    print (f"You did it you guessed the computer's number {random_number}")

def computer_guess(x):
    low = 1 #lower bound for the computer to guees
    high = x #the higher bound the computer can guess
    feedback = "" #we need to tell the comp if it's guess is too hight or too low.  
    while feedback != "c":   #we now loop over the feedback expression. we use C to indicate the correct guess
        if low != high:
            guess = random.randint(low, high) #we pass in low and hight so we can stop condidering numbers passed in too low or too high. this was we guess a number between the bound that is correct
        else:
            guess = low #could also be hight b/c low = high
        feedback = input(f"Is {guess} too high (H), too (L), correct (C) or (E) to Quit: ").lower()
        if feedback == "h":
            high = guess -1 # our upper bound is now what was just guessed -1. ex if we guess was 9  then we know the # is between 1-8
        elif feedback == "l":
            low = guess + 1
        elif feedback == "e":
            sys.exit()
    print(f"Yes! The computer guesed your number, {guess}, correctly!")

computer_guess(392)





# https://www.youtube.com/watch?v=8ext9G7xspg&t=333s start @ 10 mins. 
#review this code demo Anthony!