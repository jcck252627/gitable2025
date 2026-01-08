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

def compare (u_score, d_score):

    if u_score ==100 and d_score == 100:
        return "Draw, both you and the dealer have Blackjack !!!! "
    elif d_score == 100:
        return "You lost! the dealer has a Blackjack !!"
    elif u_score == 100:
        return "You won! you have a Blackjack !!!"
    elif u_score > 21:
        return "You lost ! you have busted"
    elif d_score > 21:
        return "You Won ! the dealer have busted"
    elif u_score > d_score:
        return "You Won !!! your final score is higher than the dealer "
    elif u_score == d_score:
        return "Draw !! Score are tied"
    else:
        return "You Lost !"



print(art.logo)

user_cards=[]
dealer_score = -1
computer_cards=[]
game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score= calculate_score((user_cards))
dealer_score=calculate_score(computer_cards)


while not game_over:
    print(f"here are just two random cards  {deal_card()}, {deal_card()}")
    print("**********Here are the user's cards:  ", user_cards)
    print(*user_cards, sep=', ')
    user_score = calculate_score(user_cards)  # <-- Recalculate here!
    print("Total score for the player is: ", user_score)
    print(f"Computer's first card: {computer_cards[0]}")
    print("**********Here are the dealer's first cards:  ", computer_cards[0])
    # print(*computer_cards, sep=', ')
    dealer_score = calculate_score(computer_cards)  # <-- Optional: recalculate if dealer changes
    print("Total score for the dealer is:  ", dealer_score)

    if user_score == 100 or dealer_score == 100 or user_score > 21:
        print("Game is OVER ... Because a Blackjack appeared or player busted")
        game_over = True
    else:
        user_hit_more = input("Do you want another card for the player? (y or n) ").lower()
        if user_hit_more == "y":
            user_cards.append(deal_card())
            if dealer_score < 17:
                computer_cards.append(deal_card())
                dealer_score=calculate_score(computer_cards)
            elif dealer_score > 21:
                print("Dealer busted ... Game OVER !")
        else:
            print("Game is OVER")
            game_over = True

while dealer_score != 100 and dealer_score < 17:
    computer_cards.append(deal_card())
    print("Dealer now has:  ",computer_cards)
    dealer_score=calculate_score(computer_cards)
    print("total dealer score now:  ",dealer_score)


print("______________________________________________________________")
print(compare(user_score, dealer_score))


while input("Do you want play another game of Blackjack ?  (y or n)").lower() == 'y':

