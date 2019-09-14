import random
#                           Rock Paper & Scissors game
# Rules
# -Rock beats Scissors
# -Scissors beats Paper
# -Paper beats Rock

print("\n\t\tRock Paper & Scissors game\n\t\t**** ***** * ******** ****\n")

status = 'y'
player_counter = 0
computer_counter = 0
player_name = input("Enter Your Name : ")
while status == 'y':
    player1 = input(f"\nMake Your Turn {player_name} : ")

    rand_num = random.randint(0,2)

    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "scissors"
    else:
        computer = "paper"
        
    print("Make Your Turn computer : " + computer)

    if player1 == computer:
        print("it's tie buddy good try!")
        print(f"\nScore :\n\t {player_name} : {player_counter} \n\t Computer : {computer_counter}")
        status  = input(f"Do you want to play again {player_name}?(y/n) ")

        if status == 'n':
            if  player_counter == computer_counter:
                print("It's tie buddy...!")
            elif player_counter > computer_counter:
                print("Congratulation you win...!")
            else:
                print("Sorry you loss try next time...!") 
    else:
        if player1 == "rock":
            if computer == "paper":
                print("computer win!")
                computer_counter += 1
            else:
                print(f"{player_name} win!")
                player_counter += 1
        elif player1 == "scissors":
            if computer == "paper":
                print(f"{player_name} win!")
                player_counter += 1
            else:
                print("computer win!")
                computer_counter += 1
        elif player1 == "paper":
            if computer == "scissors":
                print("computer win!")
                computer_counter += 1
            else:
                print(f"{player_name} win!")
                player_counter += 1
        else:
            print("something went wrong!")

        print(f"\nScore :\n\t {player_name} : {player_counter} \n\t Computer : {computer_counter}")
        status  = input(f"\nDo you want to play again {player_name}?(y/n) ")

        if status == 'n':
            if  player_counter == computer_counter:
                print("It's tie buddy...!")
            elif player_counter > computer_counter:
                print("Congratulation you win...!")
            else:
                print("Sorry you loss try next time...!") 
             

    
