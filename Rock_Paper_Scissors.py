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

#Write your code below this line 
user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissor: "))
computer_choice = random.randint(0, 2)

if user_choice==0 and computer_choice==2: 
  print("You chose rock: ")
  print(rock)
  print("Computer chose Scissor: ")
  print(scissors)
  print("You Won!!🥳")

elif user_choice==0 and computer_choice==1:
  print("You chose rock: ")
  print(rock)
  print("Computer chose Paper: ")
  print(scissors)
  print("You Lose!!🤕")

elif user_choice==0 and computer_choice==0:
  print("You chose rock: ")
  print(rock)
  print("Computer chose rock: ")
  print(rock)
  print("It's a Tie!!🤝")

# Paper Condition
elif user_choice==1 and computer_choice==0:
  print("You chose paper: ")
  print(paper)
  print("Computer chose rock: ")
  print(rock)
  print("You Won!!🥳")

elif user_choice==1 and computer_choice==2:
  print("You chose paper: ")
  print(paper)
  print("Computer chose scissors: ")
  print(scissors)
  print("You Lose!!🤕")

elif user_choice==1 and computer_choice==1:
  print("You chose paper: ")
  print(paper)
  print("Computer chose paper: ")
  print(paper)
  print("It's a Tie!!🤝")  

# Scissor Condition

elif user_choice==2 and computer_choice==1:
  print("You chose scissors: ")
  print(scissors)
  print("Computer chose paper: ")
  print(paper)
  print("You Won!!🥳")

elif user_choice==2 and computer_choice==0:
  print("You chose scissors: ")
  print(scissors)
  print("Computer chose rock: ")
  print(rock)
  print("You Lose!!🤕")

elif user_choice==2 and computer_choice==2:
  print("You chose scissors: ")
  print(scissors)
  print("Computer chose scissors: ")
  print(scissors)
  print("It's a Tie!!🤝")

else:
  print("Invalid Choice! ☠️")