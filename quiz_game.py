print("Welcome to the game")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay, Lets play :)")
score = 0

answer = input("What does CPU Stads for? ") 

if answer.lower() == "central processing unit":
    print("Your answer is Correct!")
    score += 4
else:
     print("Your answer is Not Correct!")


answer = input("What does GPU Stads for? ") 

if answer.lower() == "graphics processing unit":
    print("Your answer is Correct!")
    score += 4
else:
     print("Your answer is Not Correct!")


answer = input("What does RAM Stads for? ") 

if answer.lower() == "random access memory":
    print("Your answer is Correct!")
    score += 4
else:
     print("Your answer is Not Correct!")


answer = input("What does ROM Stads for? ") 

if answer.lower() == "read only memory":
    print("Your answer is Correct!")
    score += 4
else:
     print("Your answer is Not Correct!")

final_percentage = (score/16)*100

print("You got " + str(final_percentage) + "% Out of 100%")