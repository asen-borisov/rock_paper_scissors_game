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
print("Welcome to rock paper scissors game\n")
choice = input("What do you choose ? Type: \n0 - Rock\n1 - Paper\n2 - Scissors\n\n Type here: ")

print("\nYour Choice: \n" )

if choice == "0":
    print(rock)
elif choice == '1':
    print(paper)
elif choice == "2":
    print(scissors)


cpu = [rock, paper, scissors]

print("\nComputer:")
comp = random.choice(cpu)
print(comp)

if choice == "0" and comp == scissors:
    print("you win")
elif choice == "0" and comp == paper:
    print("you lose")
elif choice == "0" and comp == rock:
    print("draw")

if choice == "1" and comp == rock:
    print("you win")
elif choice == "1" and comp == scissors:
    print("you lose")
elif choice == "1" and comp == paper:
    print("draw")
  
if choice == "2" and comp == paper:
    print("you win")
elif choice == "2" and comp == rock:
    print("you lose")
elif choice == "2" and comp == scissors:
    print("draw")
