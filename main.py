import random

def game():
  computer_number = random.randint(0,100)
  guesses_taken = 0
  while True:
    answer = int(input("Guess the number between 1 and 100: "))
    if computer_number == answer:
      guesses_taken+=1
      print("Correct! You won in", guesses_taken, "guess(es)")
      control = input("Would you like to play again? (Type yes or no) ")
      if control == "yes":
        game()
      elif control == "no":
        print("Goodbye")
      else:
        while control != "yes" or "no":
          print("\nInvalid response.\n")
          control = input("Would you like to play again? (Type yes or no) ")
          if control == "yes":
              game()
          elif control == "no":
              print("Goodbye")
              break
          
      break
    elif computer_number > answer:
      guesses_taken+=1
      print("Too low! Try again! You have taken", guesses_taken, "guess(es).")
    else:
      guesses_taken+=1
      print("Too high! Try again! You have taken", guesses_taken, "guess(es)")
game()
