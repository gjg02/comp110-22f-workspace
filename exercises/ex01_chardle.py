"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730392807"

Word: str = input("Enter a 5 character word: ")

if len(Word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

Letter: str = input("Enter a single character: ")

if len(Letter) != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + Letter + " in " + Word)

if Letter[0] == Word[0]:
    print(Letter + " found at index 0")

if Letter[0] == Word[1]:
    print(Letter + " found at index 1")  

if Letter[0] == Word[2]:
    print(Letter + " found at index 2")   

if Letter[0] == Word[3]:
    print(Letter + " found at index 3")    

if Letter[0] == Word[4]:
    print(Letter + " found at index 4") 
    

count = 0

if Word[0] == Letter:
    count = count + 1

if Word[1] == Letter:
    count = count + 1

if Word[2] == Letter:
    count = count + 1

if Word[3] == Letter:
    count = count + 1

if Word[4] == Letter:
    count = count + 1

if count > 1: 
    print(str(count) + " instances of " + Letter + " found in " + Word)

if count == 1:
    print("1 instance of " + Letter + " found in " + Word)

if count == 0: 
    print("No instances of " + Letter + " found in " + Word)


















 
