#importing libraries
from random import randint
import time

#create list
x = ["rock","paper","scissor"]

#computer selection
comp = x[randint(0,2)]

player = False
scoreplayer = 0
scorecomp = 0
#condition
while player == False :
    player = input("which do you choose ? rock,paper or scissor:")
    if player == comp :
        print ('tie!')
    elif player == "rock" :
        if comp == "paper" :
            print ("computer chose",comp)
            time.sleep (2)
            print("you lose", comp ,"covers",player)
            scorecomp += 1
        else :
            print ("computer chose", comp)
            time.sleep(2)
            print ("you win!",player,"smashes",comp)
            scoreplayer += 1
    elif player == "paper":
        if comp == "scissor":
            print("computr choses ",comp)
            time.sleep(2)
            print("you lose ",comp ,"cuts", player)
            scorecomp += 1
        else:
            print("computer chose", comp)
            time.sleep(2)
            print("you win!",player,"covers",comp)
            scoreplayer += 1
    elif player == "scissor":
        if comp == "rock":
            print ("computer chose",comp)
            time.sleep(2)
            print("you lose ", comp ,"smashes",player)
            scorecomp += 1
        else:
            print("computer chose", comp)
            time.sleep(2)
            print ("you win!",player, "cuts",comp)
            scoreplayer += 1
    elif player == "q":
        print("game over")
        print("computer scored",scorecomp,"you scored",scoreplayer)
        if scorecomp == scoreplayer:
            print("it was a tie")
        elif scorecomp > scoreplayer:
            print("Alas! you lost")
        elif scorecomp < scoreplayer:
            print("congratulations! you won")
        break
    else:
        print("that's not a valid input.please try again!")
    player = False
    comp =x[randint(0,2)]
    print("your score is",scoreplayer,"computer's score is ",scorecomp)


