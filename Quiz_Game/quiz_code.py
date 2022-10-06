print("Welcome to quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! BE ready and Let's play :)")
score = 0

answer = input("What's the national flower of Japan? ")
if answer.lower() == "cherry blossom":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Until 1923, what was the Turkish city of Istanbul called? ")
if answer.lower() == "cyesonstantinople":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the national game of CANADA? ")
if answer.lower() == "ice hockey":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")
if score<= 3:
    print("Better luck next TIME!")
else: 
    print("You rocked it!")