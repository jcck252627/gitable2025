import random
import art
#card_face =["1","2","3","4","5","6","7,"8","9","10","A","K","Q","J"]
# card_value =[1,2,3,4,5,6,7,8,9,10,11,10,10,10,10]

card_face_value ={
  "1" : 1,
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

def pick_two_cards():
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

print("i am an Ace (A) for "+str(card_face_value["A"][1])+"  points if i can add it up to less than 21 " )



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


#inital_hand_cpu = random.
#inital_hand_player



cards, total = pick_two_cards()
print("Random cards:", cards)
print("Total value:", total)




"""
print(art.BLANKCARD+"  "+art.CARDS[7])
print(art.CARDS[3])
"""



