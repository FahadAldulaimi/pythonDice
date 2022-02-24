import random
import os
import time

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

diceDict = {

  1:"│       │\n│   ☻   │\n│       │\n",
  2:"│ ☻     │\n│       │\n│     ☻ │\n",
  3:"│ ☻     │\n│   ☻   │\n│     ☻ │\n",
  4:"│ ☻   ☻ │\n│       │\n│ ☻   ☻ │\n",
  5:"│ ☻   ☻ │\n│   ☻   │\n│ ☻   ☻ │\n",
  6:"│ ☻   ☻ │\n│ ☻   ☻ │\n│ ☻   ☻ │\n"

}

while True:
  print("Roll 1 dice, 2 dice, or 0 to exit? ")
  intInput = int(input())
  r1 = random.randint(1, 6)
  r2 = random.randint(1, 6)
  dice1 = "┌───────┐\n" + diceDict[r1] + "└───────┘"
  dice2 = "┌───────┐\n" + diceDict[r2] + "└───────┘"
  clear()

  if intInput == 1:
    for i in range(5):
      print("┌───────┐\n" + diceDict[random.randint(1, 6)] + "└───────┘")
      time.sleep(.300)
      clear()

    print("  _____\n" +" /\n" + "/\n" +dice1)
    print("Value: " + str(r1) + "\n")

  elif intInput == 2:
    li1 = dice1.splitlines()
    li2 = dice2.splitlines()

    for i in range(5):
      print(li1[i] + li2[i])

    print("You rolled a " + str(r1 + r2) + "\n")

  elif intInput == 0:
    break