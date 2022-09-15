"""EX02 - Wordle in 1."""
__author__ = "730392807"

# Here I am defining the variables of the boxes, and the secret word
secret_word = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Asking the user for their guess of the secret word
guess = str = input("What is your 6-letter guess? ")

# If the user's guess is not the length of the secret word, they are asked to try again
while len(guess) != len(secret_word):
    guess = input("That was not 6 letters! Try again: ")
   
# An infinite loop was created to check each index of the user's guess to see if it matches the same index of the secret word
# A green box will appear if they are the same
check_guess = int(0)
stored_box = ""
while int(check_guess) < int(len(secret_word)):
    if guess[check_guess] == secret_word[check_guess]:
        stored_box = stored_box + GREEN_BOX

# An infinite loop was created to check each index of the user's guess to if it matches any index of the secret word
# A separate variable was created to do this so as to not be confused with the first variable
# If it does match than the index will appear in a yellow box  
# If the index of the user's guess does not match any of the index's of the secret word, then a white box will appear  
    else:
        index_check = 0
        yellow = False
        while int(index_check) < int(len(secret_word)):
            if guess[check_guess] == secret_word[index_check]:
                yellow = True
            index_check = index_check + 1

# This section adds all the "boxes" together to show the user which letters of the guessed word are in the secret word
        if yellow is True:
            stored_box = stored_box + YELLOW_BOX
        else:
            stored_box = stored_box + WHITE_BOX
# This while loop variable ensures that the variable check guess changes so we do not have an infinite loop              
    check_guess = check_guess + 1
print(stored_box) 

if guess == secret_word:
    print("Woo! You got it!")

else: 
    print("Not quite. Play again soon!")