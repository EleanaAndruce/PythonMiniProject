#simple magic 8 ball game

import random

print("*** Magic 8 Ball ***")
print("3 rounds only..")
wordList = ['It is kind of hazy... Try again',
		'Definitely',
		'Absolutely',
		'You may rely on it',
		'Outlook good',
		'It is certain',
		'Follow your heart',
		'Go for it',
		'Better not tell you now',
		'Sign point to yes',
		'Cannot predict now',
		'Ask again later',
		'Concentrate and ask again',
		'Do not count on it',
		'My reply is no',
		'My sources say no',
		'Outlook not so good',
		'Very doubtful']

random.shuffle(wordList)
count = 0

while(count < 3):
  ran = random.choice(wordList)
  input1 = input("\nPlease type you question: ")
  smallRan = ran.lower()
  
  if(input1 == "exit"):
      print("Exiting now...")
      break
  else:
    print(ran)
  count = count + 1
print("***********")
print("\nGoodbye")
print("Disclaimer: Please do not take this seriously")
