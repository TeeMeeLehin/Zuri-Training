#A Game of Rock, Paper, Scissors.

# R is for Rock, P is for Paper, S is for Scissors.
import random

options = ("R", "P", "S")

#Game Starts.

def game(user):
 
 com = random.choice(options)

 if(user != com):
        
    if(user=="R" and com=="P"):
        print("You chose Rock and CPU chose Paper.")
        print("Paper covers Rock. CPU Wins!")

    elif(user=="R" and com=="S"):
        print("You chose Rock and CPU chose Scissors.")
        print("Rock crushes Scissors. You Win!")

    elif(user=="P" and com=="R"):
        print("You chose Paper and CPU chose Rock.")
        print("Paper covers Rock. You Win!")

    elif(user=="P" and com=="S"):
        print("You chose Paper and CPU chose Scissors.")
        print("Scissors cuts Paper. CPU Wins!")

    elif(user=="S" and com=="R"):
        print("You chose Scissors and CPU chose Rock.")
        print("Rock crushes Scissors. CPU Wins!")

    elif(user=="S" and com=="P"):
        print("You chose Scissors and CPU chose Paper.")
        print("Scissors cuts Paper. You Win!")

 else:
     print("You chose " + user + " and CPU chose " + com)
     print("Game is a Tie. Go again. \n")
     user = input("Enter your choice again - R, P or S \n")
     print("Rock! Paper! Scissors!")
     game(user)

user = input("Enter your choice - R, P or S \n")
while user not in options:
 user = input("Invalid Entry. Enter your choice again - R, P or S \n")
else:
 print("Rock! Paper! Scissors!")
 game(user)
    
        
    
