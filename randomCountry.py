#simple country guessing game

import random

print("*** Guess the country ***")
print("3 rounds only..")
wordList = ["America", "Canada", "Ireland", "United Kingdom", "China",
            "Malaysia", "Japan", "Cambodia", "Korea", "Romania",
            "Indonesia", "Philiphines", "Russia", "Spain", "Greece"]

random.shuffle(wordList)
count = 0

while(count < 3):
  ran = random.choice(wordList)
  length = len(ran)
  print("Country length is: ", length)
  input1 = input("\nPlease enter a country: ")
  smallRan = ran.lower()
  
  if(input1 == "exit"):
      print("Exiting now...")
      break
  elif(input1 != smallRan):
    print("\nSorry wrong answer")
    print("The answer is: ", ran)
  else:
    print("Congratulation!!")
    break
  count = count + 1
print("\nGoodbye")
