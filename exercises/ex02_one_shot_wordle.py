"EX02 - Wordle in 1"
__author__ = 730392807

secret_word = "python"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess = str = input("What is your 6-letter guess? ")

while len(guess) != 6:
    guess = input("That was not 6 letters! Try again: ")
   
check_guess = int(0)
stored_box = ""


while int(check_guess) < int(len(secret_word)):
    if guess[check_guess] == secret_word[check_guess]:
        stored_box = stored_box + GREEN_BOX
        

    else:
        
        index_check= 0
        yellow = False
        while int(index_check) < int(len(secret_word)):
            if guess[check_guess] == secret_word[index_check]:
                yellow = True
            index_check = index_check + 1


        if yellow == True:
            stored_box = stored_box + YELLOW_BOX
        else:
            stored_box = stored_box + WHITE_BOX
                
    check_guess = check_guess + 1
print(stored_box)
        

if guess == secret_word:
    print("Woo! You got it!")

else: print("Not quite. Play again soon!")


