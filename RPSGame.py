#                           Rock Paper & Scissors game
# Rules
# -Rock beats Scissors
# -Scissors beats Paper
# -Paper beats Rock

print("\n\t\tRock Paper & Scissors game\n\n")

player1 = input("Make Your Turn player1 : ")
print("no cheating buddy please \n\n" * 20) 
player2 = input("Make Your Turn player2 : ")

if player1 != player2:
    if player1 == "rock":
        if player2 == "paper":
            print("player2 win!")
        elif player2 == "scissors":
            print("player1 win!")
    elif player1 == "scissors":
        if player2 == "paper":
            print("player1 win!")
        elif player2 == "rock":
            print("player2 win!")
    elif player1 == "paper":
        if player2 == "scissors":
            print("player2 win!")
        elif player2 == "rock":
            print("player1 win!")
    else:
        print("something went wrong!")
else:
    print("it's tie buddy!")

    
    
