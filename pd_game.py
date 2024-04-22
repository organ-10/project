import random

WINNING_SCORE = 100

def roll_die():
  """Simulates rolling a single die."""
  return random.randint(1, 6)

def hold(score):
  """Adds the current turn score to the total score."""
  return score

def player_turn(player_name, player_score):
  """Implements a single player's turn."""
  turn_score = 0
  roll = 0

  while True:
    print(f"{player_name}'s turn.")
    choice = input("Roll (r) or Hold (h)? ")

    if choice.lower() == 'r':
      roll = roll_die()
      print(f"You rolled: {roll}")

      if roll == 1:
        print("Oops! You rolled a 1. Turn over.")
        turn_score = 0  # Reset turn score
        break  # End the turn
      else:
        turn_score += roll
    elif choice.lower() == 'h':
      player_score += turn_score
      print(f"You held. Your score is now {player_score}")
      break
    else:
      print("Invalid input. Please enter 'r' or 'h'.")

  return player_score

def main():
  """Main game loop."""
  player_score = 0
  computer_score = 0

  while player_score < WINNING_SCORE and computer_score < WINNING_SCORE:
    player_score = player_turn("Player", player_score)

    if player_score >= WINNING_SCORE:
      break  # Player reached winning score

    # Simple computer strategy: Roll until score is at least 20
    computer_turn_score = 0
    while computer_turn_score < 20:
      roll = roll_die()
      print(f"Computer rolled: {roll}")

      if roll == 1:
        print("Computer rolled a 1. Turn over.")
        computer_turn_score = 0
        break
      else:
        computer_turn_score += roll

    computer_score += computer_turn_score
    print(f"Computer held. Computer score: {computer_score}")

  # Determine the winner
  if player_score >= WINNING_SCORE:
    print("Congratulations! You win!")
  else:
    print("Computer wins!")

if __name__ == "__main__":
  main()

