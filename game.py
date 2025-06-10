import random 


#snake ,water, gun game !

"""
   snake = 1
   water = -1
   gun = 0

"""

computer= random.choice([1,0,-1])
youstr=input ("click to  enter in the game ")

youdict={"s":1 , "w":-1 ,"g":0}
reversedict={1:"snake ", -1:"water", 0:"gun"}
you = youdict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if (computer==you):
    print(" its a draw ")

else:


    if(computer ==-1 and you == 1): 
        print("You win!")

    elif(computer ==-1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer ==1 and you == 0):
        print("You Win!")

    elif(computer ==0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")