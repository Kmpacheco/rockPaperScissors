'''
Created on Feb 1, 2020

@author: ITAUser
'''
import random 

keepPlaying = True 

while (keepPlaying == True):
    print ("Welcome, you ready to lose")
    print ("First to 2 wins. Press q to quit. Type in lower case letters")
    
    scoreComp = 0 
    scorePlayer = 0
    
    while(scorePlayer < 2) and (scoreComp < 2):
        choiceComp = random.randint (1,3)
        choicePlayer = input("pick either rock, paper, or scissors!")
        
        if (choiceComp == "q"):
            keepPlaying = False
            break 
        elif((choicePlayer == "rock") and (choiceComp == 1)) or ((choicePlayer == "paper") and (choiceComp == 2 )) or ((choicePlayer == "scissors") and (choiceComp == 3)):
            print("Draw")
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
            
            
        elif((choicePlayer == "rock") and (choiceComp == 2)) or ((choicePlayer == "paper") and (choiceComp == 3)) or ((choicePlayer == "scissors") and (choiceComp == 1)):
            print("You Lose")
            scoreComp = scoreComp + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        elif((choicePlayer == "rock") and (choiceComp == 3)) or ((choicePlayer == "paper") and (choiceComp == 1)) or ((choicePlayer == "scissors") and (choiceComp == 2)):
            print("You won")
            scorePlayer = scorePlayer + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        elif:
            print("Rock, Paper or Scissors!")
        
        
        if(scorePlayer == 2):
            print("You Win!!")
            
        if (scoreComp == 2):
            print("You will never win")
            
        print("Computer's Score: ", + scoreComp , "Your Score: ", + scorePlayer)
        
            