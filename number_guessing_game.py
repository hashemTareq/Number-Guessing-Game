import random

number_to_guess = random.randint(1, 100)

while True:
  try:
    guess = int(input('Guess the number between 1 and 100: ').strip())
    if guess > number_to_guess:
      print('Too high!')
    elif guess < number_to_guess:
      print('Too low!')
    else:
      print('Gongratulations! You guessed the number.')
      break
  except ValueError:
    print('Please enter a valid number')
