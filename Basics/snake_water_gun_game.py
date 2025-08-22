import random

computer = random.choice([1,-1,0])
youStr = input("Enter your number: ")
yourDict = {"s":1, "w":-1, "g": 0}
repeatedDict = {1: "snake", -1: "water", 0: "gun"}

you = yourDict[youStr]

print(f"you choose {repeatedDict[you]} \ncomputer choose {repeatedDict[computer]}")

if(computer == you):
    print("It's draw")
    
else:
    if(computer == -1 and you == 1):
        print("you win")
    elif(computer == -1 and you == 0):
        print("you win")
    elif(computer == 1 and you == -1):
        print("you loose")
    elif(computer == 1 and you == 0):
        print("you win")
    elif(computer == 0 and you == 1):
        print("you loose")
    elif(computer == 0 and you == -1):
        print("you win")
    else:
        print("something went wrong")    
        
    