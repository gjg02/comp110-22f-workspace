"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730392807"


X: str = input("Enter a 5 character word: ")

if len(X) != 5:
    print("Error: Word must contain 5 characters")
    exit()

Y: str = input("Enter a single character: ")

if len(Y) != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + Y + " in " + X)

if Y[0]==X[0]:
    print(Y + " is found in index 0")

if Y[0]==X[1]:
    print(Y + "is found in index 1")  

if Y[0]==X[2]:
    print(Y + " is found in index 2")   

if Y[0]==X[3]:
    print(Y + " is found in index 3")    

if Y[0]==X[4]:
    print(Y + " is found in index 4") 
    

str(Y)
V = str(X)
str=(V)
V = V.count(Y) 

if V == 1:
    print("1 instance of " + Y + " is found in " + X)

if V == 2:
    print("2 instances of " + Y + " is found in " + X)

if V == 3:
    print("3 instances of " + Y + " is found in " + X)

if V == 0:
    print("0 instances of " + Y + "is found in " + X)















 
