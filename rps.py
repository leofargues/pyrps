import random
print("Rock Paper Scissors")
user = input()
robot = (random.randint(1, 3))
if user == "rock" or "Rock":
    user = 1
elif user == "paper" or "Paper":
    user = 2
elif user == "scissors" or "Scissors":
    user = 3
else:
    print("Error")
print("")
print("1 - Rock")
print("2 - Paper")
print("3 - Scissors")
print("")
print("user have choosed", user)
print("robot have choosed", robot)
if robot == user:
    print("Tie")
elif user == 1:
    if robot == 2:
        print("You loose")
    elif robot == 3:
        print("You win")
elif user == 2:
    if robot ==  3:
        print("You lose")
    elif robot == 1:
        print("You win")
elif user == 3  :
    if robot == 1:
        print("You lose")
    elif robot == 2:
        print("You win")
print("e")
