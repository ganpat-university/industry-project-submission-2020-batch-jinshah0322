import random

print("Rock, Paper, Scissors Game!")
print("Player 1, enter your choice (rock/paper/scissors): ")
player1_choice = input().lower()

print("Player 2, enter your choice (rock/paper/scissors): ")
player2_choice = input().lower()

if player1_choice == player2_choice:
    print("It's a tie!")
elif (
    (player1_choice == "rock" and player2_choice == "scissors") or
    (player1_choice == "paper" and player2_choice == "rock") or
    (player1_choice == "scissors" and player2_choice == "paper")
):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")