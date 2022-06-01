import random
play = True

Player_wins = 0
CPU_wins = 0

while play:
    choices = ["R", "P", "S"]
    CPU = random.choice(choices)
    Player = None

    Player = input("Enter a choice rock(R), paper(P), or scissors(S)?: ").upper()
    if Player not in choices:
        print("error! Please enter a valid choice!")

    if Player == CPU:
         print(f"Both players selected {Player}. It's a tie!")
    
    if Player == "R" and  CPU == "S":
        print(f"Player {Player} : CPU {CPU}")
        print("you win!")
        Player_wins += 1
    
    elif Player == "P" and  CPU == "R":
        print(f"Player {Player} : CPU {CPU}")
        print("you win!")
        Player_wins += 1
    
    elif Player == "S" and  CPU == "P":
        print(f"Player {Player} : CPU {CPU}")
        print("you win!")
        Player_wins += 1
    
    else:
        print(f"Player {Player} : CPU {CPU}")
        print("you lose")
        CPU_wins += 1


    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        play = False
    

print("you won", Player_wins, "times")
print("computer won", CPU_wins, "times")
print("Goodbye,Thank you for playing!")

