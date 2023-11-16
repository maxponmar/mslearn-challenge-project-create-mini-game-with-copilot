import random

choices = ['rock', 'paper', 'scissors']
score = 0

def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    global score
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        score += 1
        return 'You win!'
    else:
        return 'Computer wins!'

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f'You chose {user_choice}, computer chose {computer_choice}.')
    print(determine_winner(user_choice, computer_choice))
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print(f'Your score: {score}')