
# EXERCEISE - NUMBER GUESSING GAME(with loop)

#---------------soluation------------------
import random

winning_number = random.randint(1,100)
print('You have 10 guess') #telling user that he have 5 guess
guessed_number = int(input('Guess the number between 1 and 100 : '))
guess = 1
left_guess = 10
game_over = False

#infinite loop

while not game_over:   # gameover is not true

    if winning_number == guessed_number:
        print(f'Congrats you guessed the number in {guess} time')
        game_over = True

    else:
        if guess == 10:
            print('Sorry, you can\'t guess the number and you used 10 guesses')
            print(f'The number is {winning_number}')
            game_over = True

        else:
            if guessed_number > winning_number:
                print('"Too high"')

            else:
                print('"Too low"')
            guess +=1
            print(f'{left_guess - (guess-1)} guess left')  # (guess-1) because guess is already 1 
            guessed_number = int(input(' \nGuess again : '))




