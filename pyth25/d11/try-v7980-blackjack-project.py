import random
import art
#card_face =["1","2","3","4","5","6","7,"8","9","10","A","K","Q","J"]
# card_value =[1,2,3,4,5,6,7,8,9,10,11,10,10,10,10]

card_face_value ={
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "A": [1,11],
    "K": 10,
    "Q": 10,
    "J": 10
}

CARD_ART_MAP = {
    "A": art.CARDS[12],
    "2": art.CARDS[11],
    "3": art.CARDS[10],
    "4": art.CARDS[9],
    "5": art.CARDS[8],
    "6": art.CARDS[7],
    "7": art.CARDS[6],
    "8": art.CARDS[5],
    "9": art.CARDS[4],
    "10": art.CARDS[3],
    "J": art.CARDS[2],
    "Q": art.CARDS[1],
    "K": art.CARDS[0],
}


def pick_two_cards_p1():
# Pick two random cards
    cards = random.sample(list(card_face_value.keys()), 2)

    total = 0
    ace_count = 0

    for card in cards:
        if card == "A":
            total += 11  # Assume Ace is 11
            ace_count += 1
        else:
            total += card_face_value[card]

    # Adjust Aces if total > 21
    while total > 21 and ace_count > 0:
        total -= 10  # Convert one Ace from 11 to 1
        ace_count -= 1

    return cards,total

def pick_two_cards_p2():
# Pick two random cards
    cards = random.sample(list(card_face_value.keys()), 2)

    total = 0
    ace_count = 0

    for card in cards:
        if card == "A":
            total += 11  # Assume Ace is 11
            ace_count += 1
        else:
            total += card_face_value[card]

    # Adjust Aces if total > 21
    while total > 21 and ace_count > 0:
        total -= 10  # Convert one Ace from 11 to 1
        ace_count -= 1

    return cards,total


def print_cards(cards):
    for card in cards:
        if card == "A":
            print(art.CARDS[12])
        elif card =="2":
            print(art.CARDS[11])
        elif card =="3":
            print(art.CARDS[10])
        elif card =="4":
            print(art.CARDS[9])
        elif card == "5":
            print(art.CARDS[8])
        elif card == "6":
            print(art.CARDS[7])
        elif card == "7":
            print(art.CARDS[6])
        elif card == "8":
            print(art.CARDS[5])
        elif card == "9":
            print(art.CARDS[4])
        elif card == "10":
            print(art.CARDS[3])
        elif card == "J":
            print(art.CARDS[2])
        elif card == "Q":
            print(art.CARDS[1])

        else:
            print(art.CARDS[0])


#def add_card_to_player():
#def add_card_to_cpu ():



card_face = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "K", "Q", "J"]
card_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [1, 11], 10, 10, 10]

print("Testing access to the diectionary__________________________________________")
card_dict = dict(zip(card_face, card_value))
print(card_dict["A"])  # Output: [1, 11]
print(card_dict["A"][0])
print(card_dict["A"][1])
print(card_dict)
print("___________________________________________________________________________")


print("Welcome to the BlackJack GAME !!!!!")
print(art.logo)
print(art.CARDS[3])


print("Here is CPU's Hand________________________")
cpu_cards, cpu_total = pick_two_cards_p1()
print("CPU's cards:", cpu_cards)
print("Total value:", cpu_total)
print_cards(cpu_cards)

print("Here is Your's Hand_______________________")
player_cards, player_total = pick_two_cards_p2()
print("Player's cards:", player_cards)
print("Total value:", player_total)
print_cards(player_cards)





"""
print(art.BLANKCARD+"  "+art.CARDS[7])
print(art.CARDS[3])
"""



