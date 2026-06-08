import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while True:
    player = input("\nEnter Rock, Paper, or Scissors (or 'quit' to exit): ").lower()

    if player == "quit":
        print("\nFinal Score:")
        print("You:", player_score)
        print("Computer:", computer_score)
        print("Thanks for playing!")
        break

    if player not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if player == computer:
        print("It's a Tie!")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("You Win!")
        player_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print(f"Score -> You: {player_score} | Computer: {computer_score}")