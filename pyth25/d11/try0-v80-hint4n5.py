import random
import art

def deal_card():
    """
    Return a random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_picked = random.choice(cards)
    return cards

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 100
    if 11 in cards and sum(cards)> 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

player_cards =[]
dealer_cards =[]
is_game_over = False

for _ in range(2):
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())

player_score=calculate_score(player_cards)
dealer_score=calculate_score(dealer_cards)

print(f"Player's cards: {player_cards}. current score: {player_score}")
print(f"Dealer's 1st card: {dealer_cards[0]}, current score: {dealer_score}")



if player_score ==100 or dealer_score==100 or player_score > 21:
    is_game_over = True

