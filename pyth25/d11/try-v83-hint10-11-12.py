import random
import art


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    Calculate cards total scores and determine if the cards produce a blackjack of 21
    """
    if sum(cards)==21 and len(cards)==2:
        return 100
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


user_cards=[]
dealer_scope = -1
computer_cards=[]
game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score= calculate_score((user_cards))
dealer_score=calculate_score(computer_cards)


while not game_over:

    print(f"here are just two random cards  {deal_card()}, {deal_card()}")
    print("**********Here are the user's cards:  ",user_cards)
    print(*user_cards, sep=', ')
    print("Total score for the player is: ", calculate_score(user_cards))
    print("**********Here are the dealer's cards:  ", computer_cards)
    print(*computer_cards, sep=', ')
    print("Total score for the dealer is:  ", calculate_score(computer_cards))


    if user_score==100 or dealer_score==100 or user_score > 21:
        print("Game is OVER")
        game_over = True
    else:
        user_hit_more=input("Do you want another card for the player? (y or n) ").lower()
        if user_hit_more == "y":
            user_cards.append(deal_card())
        else:
            print("Game is OVER")
            game_over=True


while dealer_score != 100 and dealer_score > 17:
    computer_cards.append(computer_cards)
    dealer_score=calculate_score(computer_cards)
