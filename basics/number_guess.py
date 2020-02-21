import random


def start_game():
    while True:
        correct_answer = random.randint(1, 10)

        guess_number = int(input("Guess a number between 1 to 20: "))

        if correct_answer == guess_number:
            print(f'You win! 👏🎉')
            break
        else:
            print(f"Nope! It was {correct_answer}")
            play_again = input('Try again. 1/0: ')
            if int(play_again) == 0:
                break


start_game()
