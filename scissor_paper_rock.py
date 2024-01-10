import random
while True:
    choices = ["rock", "paper", "scissor"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player =input("Enter Scissor, paper, rock: ").lower()
    if player == computer:
        print("computer: ",computer)
        print("player  : ",player)
        print("tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player  : ",player)
            print("you lose! ")
        if computer == "scissor":
            print("computer: ", computer)
            print("player  : ",player)
            print("you win! ")
    elif player == "scissor":
        if computer == "paper":
            print("computer: ", computer)
            print("player  : ",player)
            print("you win! ")
        if computer == "rock":
            print("computer: ", computer)
            print("player  : ",player)
            print("you lose! ")
    elif player == "paper":
        if computer == "scissor":
            print("computer: ", computer)
            print("player  : ",player)
            print("you lose! ")
        if computer == "rock":
            print("computer: ", computer)
            print("player  : ",player)
            print("you win! ")
    play_again = input("play again? (yes/no) ").lower()
    if play_again != "yes":
        break
print("bye!")