from random import randrange
play_again = "yes"
choices = ["Rock","Paper","Scissors"]


while play_again=='yes':
    player_choice = input("Choose: Rock, Paper, or Scissors: ").capitalize()
    computer_choice = choices[randrange(3)]

    print("The computer chose: " + computer_choice)
    print("You chose: " + player_choice)

    if computer_choice == player_choice:
      print("It's a tie!")
    elif computer_choice == "Rock":
      if player_choice == "Paper":
        print("You win!")
      else:
        print("You lose!")
    elif computer_choice == "Paper":
      if player_choice == "Rock":
        print ("You lose!")
      else:
        print ("You win!")
    elif computer_choice == "Scissors":
      if player_choice == "Rock":
        print("You win!")
      else:
        print("You lose!")

    print("\n\n---------------------------\n")
    play_again = input("Do you want to play again?: ").lower()

print("Thank you for Playing!")
import unittest
from main import rock_paper_scissors

class TestRockPaperScissors(unittest.TestCase):

    def test_win(self):
        """Test case where the player wins"""
        self.assertEqual(rock_paper_scissors("rock", "scissors"), "You win!")
        self.assertEqual(rock_paper_scissors("scissors", "paper"), "You win!")
        self.assertEqual(rock_paper_scissors("paper", "rock"), "You win!")

    def test_lose(self):
        """Test case where the player loses"""
        self.assertEqual(rock_paper_scissors("rock", "paper"), "You lose!")
        self.assertEqual(rock_paper_scissors("scissors", "rock"), "You lose!")
        self.assertEqual(rock_paper_scissors("paper", "scissors"), "You lose!")

    def test_tie(self):
        """Test case where it's a tie"""
        self.assertEqual(rock_paper_scissors("rock", "rock"), "It's a tie!")
        self.assertEqual(rock_paper_scissors("paper", "paper"), "It's a tie!")
        self.assertEqual(rock_paper_scissors("scissors", "scissors"), "It's a tie!")

if __name__ == "__main__":
    unittest.main()
