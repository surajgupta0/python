import random

def give_cards():
    choices = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(choices)
    
user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(give_cards())
    computer_cards.append(give_cards())

def show_result(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Blackjack for Computer You Loose!"
    elif user_score == 0:
        return "Blackjack! You win!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"
    
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f'Your card is {user_cards}, current score {user_score} ')
    print(f'Computer first number is {computer_cards[0]}')
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        should_continue = input("Type 'y' to get another card, 'n' to pass: ")
        
        if should_continue.lower() == 'y':
            user_cards.append(give_cards())
        else:
            is_game_over = True
        
while computer_score != 0 and computer_score < 17:
    computer_cards.append(give_cards())
    computer_score = calculate_score(computer_cards)
    
result = show_result(user_score, computer_score)
print(f'Your card is {user_cards}, current score {user_score} ')
print(f'Computer card is {computer_cards}, current score {computer_score}')
print (f'{result}')
    