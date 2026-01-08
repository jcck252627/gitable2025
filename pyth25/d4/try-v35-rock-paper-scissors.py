import random

rock_i = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_i = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_i = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock_i, paper_i, scissors_i]
rps_plays = ["rock", "paper", "scissors"]

you_choice=input("Which one do you choose ? Type 'rock', 'paper', or 'scissors' ...  ").lower()
while you_choice not in rps_plays:
    print("You have entered an invalidate play .... Try AGAIN !")
    you_choice = input("Which one do you choose ? Type 'rock', 'paper', or 'scissors' ...  ").lower()

print("--------------")
print("Your play:   "+you_choice)
if you_choice =='rock':
    print(game_images[0])  # rock
elif you_choice =='paper':
    print(game_images[1])  # paper
else:
    print(game_images[2])  # scissors


computer_choice= random.choice(rps_plays)
print("Computer play:  "+computer_choice)
if computer_choice =='rock':
    print(game_images[0])  # rock
elif computer_choice =='paper':
    print(game_images[1])  # paper
else:
    print(game_images[2])  # scissors


if you_choice == computer_choice:
    print("It's a draw! You both chose", you_choice)

elif you_choice == "rock" and computer_choice == "scissors":
    print("Rock smashes scissors ..... YOU WIN!")
elif you_choice == "rock" and computer_choice == "paper":
    print("Paper covers rock ..... YOU LOSE!")

elif you_choice == "paper" and computer_choice == "rock":
    print("Paper covers rock ..... YOU WIN!")
elif you_choice == "paper" and computer_choice == "scissors":
    print("Paper got cut by scissors ..... YOU LOSE!")

elif you_choice == "scissors" and computer_choice == "paper":
    print("Scissors cuts paper ..... YOU WIN!")
elif you_choice == "scissors" and computer_choice == "rock":
    print("Rock smashes scissors ..... YOU LOSE!")


"""""""""""""""
print("__________________________________")
print("__________________________________")
print("__________________________________")
print("____________________________-______")
print(game_images[0]) # rock
print(game_images[1]) # paper
print(game_images[2]) # scissors

"""""""""""""""



