import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choice = int(input("press 0 for Rock, 1 for paper or 2 for scissors"))

if(choice >= 3 or choice < 0):
  print("invalid number")
else:
  choice_arr = [rock, paper, scissors]

  player_chose = choice_arr[choice]

  print(player_chose)


  computer_choice = int(random.randint(0, 2))

  computer_chose = choice_arr[computer_choice]
  
  print("computer chose:")
  print(computer_chose)

  if(player_chose == rock and computer_chose == scissors):
    print("you win")
  elif(player_chose == scissors and computer_chose == paper):
    print("you win")
  elif(player_chose == paper and computer_chose == rock):
    print("you win")
  elif(player_chose == computer_chose):
    print("draw")
  else:
    print("you lose")

