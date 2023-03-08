import random 
Cnumber=random.randrange(1,101)
userInput=int(input("Enter a number :- "))

if Cnumber>userInput:
    print("Computer guess Number :", Cnumber)
    print("Your guess Number", userInput, "is smaller than Computer guess Number.")
elif userInput>Cnumber:
    print("Computer guess Number :", Cnumber)
    print("Your guess Number", userInput, "is higher than Computer guess Number.")
else:
    print("Computer guess Number :", Cnumber)
    print("Your guess Number", userInput, "is equl to Computer guess number")
