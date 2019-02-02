#guessing game with exit function

import random

print("*** Guessing number game ***")
print("5 rounds only")
print("Type exit to exit the game")
count = 0

while(count < 4):
    input1 = input("Please enter range 1 - 20: ")
    x = random.randint(1,20)
    y = str(x) #changing random int to str

    if(input1 == "exit"):
        print("Exiting now...")
        break
    elif(input1 != y):
        print(x)
    elif(input1 == y):
        print("Congratulation...")
    else:
        print("Invalid response")
    count = count + 1
print("\nGoodbye..")
