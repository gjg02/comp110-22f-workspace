"""Wordle- Another One."""
__author__ = "730392807"


# Defining contains_char, which is a function that will see if a specific character is in the secret word
# This infinite loops keeps repeating until all the index's in the secret word have been checked
def contains_char(search_str: str, search_character: str) -> bool:
    """Seeing if a character is in the string."""
    assert len(search_character) == 1

    index: int = 0

    while index < (len(search_str)):
        if search_character == search_str[index]:
            return True
        index += 1

    return False

# Defining emojified, which is a function that see's if the character is in the exact spot as in the secret word- if so then a green box
# If not, then we run the contains_char function to check the other indexes in the word to see if any index in the secret word match the specific character- if so then a yellow box appears
# The default is a white box, meaning there are no instances of that character in the secret word
# Stored box is the variable that keeps track of the different colored boxes, depending on if the character is there or not, and it is returned once the while loop is done
# The infinite loop keeps running until all the indexes have been checked


def emojified(guess_str: str, search_str: str) -> str:
    """Seeing which characters are in the string."""
    assert len(guess_str) == len(search_str)

    i: int = 0 
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    stored_box: str = ""
    
    while i < (len(search_str)):
        if guess_str[i] == search_str[i]:
            stored_box += GREEN_BOX
        elif contains_char(search_str, guess_str[i]):
            stored_box += YELLOW_BOX
        else:
            stored_box += WHITE_BOX
        i += 1           

    return stored_box     

# Defining the function, input_guess is a precautionary measure to make sure that the user doesn't put a longer/shorter string than what it is prompted
# If so, then the user will be asked to make another guess


def input_guess(length: int) -> str:
    """Making sure the user's guess equals the length of the secret word."""
    print_guess = input(f"Enter a {length} character word: ")  
    while length != len(print_guess):
        print_guess = input(f"That wasn't {length} chars! Try again: ")
    return (print_guess)
    

# This main function calls all the other functions and puts the defined functions to use.
# The user is first asked to guess a word of whatever the length is (calling on the input_guess variable)
# If the word is the correct length, then the funciton continues to the boxes variable, which calls on the emojified function to look for the indexes of the guessed word in the indexes of the secret word
# The variable "win" automatically defaults to false, and if the user guesses the secret word, then the variable "win" changes to true and exits the while loop
def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1
    secret = "codes"
    length = len(secret)
    guess = ""
    win: bool = False

    while turn < 7 and win is False:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(length)
        boxes: str = emojified(guess, secret)
        print(boxes)

        if guess == secret:
            win = True
        turn += 1
# If the variable win changes to true, then the user wins the game and is prompted with the winning message
# If the user has used all it's 6 turns, then the user is prompted to try again tomorrow
    if win is True:
        print((f"You won in {turn - 1}/6 turns!"))
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()