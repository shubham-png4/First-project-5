import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    player = input("Choose (rock/paper/scissors): ").lower()
    
    if player not in choices:
        print("Invalid choice!")
        return
    
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    if player == computer:
        print("🤝 It's a tie!")
    elif (player == "rock" and computer == "scissors") or
         (player == "paper" and computer == "rock") or
         (player == "scissors" and computer == "paper"):
        print("🎉 You win!")
    else:
        print("😞 You lose!")

play_game()