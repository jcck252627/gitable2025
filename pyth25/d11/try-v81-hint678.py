import random
import art


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==11 and len(cards)==2:
        return 100
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


user_cards=[]
computer_cards=[]

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

print(f"here are just two random cards  {deal_card()}, {deal_card()}")
print("***Here are the user's cards:  ",user_cards)
print(*user_cards, sep=', ')
print("Total score for the player is: ", calculate_score(user_cards))
print("***Here are the dealer's cards:  ", computer_cards)
print(*computer_cards, sep=', ')
print("Total score for the dealer is:  ", calculate_score(computer_cards))


