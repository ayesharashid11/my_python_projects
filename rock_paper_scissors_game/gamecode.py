

import random

# Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None
# Check for all possibilities when computer chose scissors
    elif comp=='r':
        if you=='p':
         return True
        elif you=='s':
            return False
# Check for all possibilities when computer chose paper
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
# Check for all possibilities when computer chose scissors

    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False
    
# by using random module computer selects random number from given options 
# so player don't cheat the computer's selected option
print("Comp Turn: Select Rock(r) , Paper(p), Scissors(s)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'r'
elif randNo == 3:
    comp = 'p'

you = input("Your Turn: Select from Rock(r) , Paper(p), Scissors(s)?")
a = gameWin(comp, you)
#printing the selected option of YOU and computer
print(f"Computer choose {comp}")
print(f"You choose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
