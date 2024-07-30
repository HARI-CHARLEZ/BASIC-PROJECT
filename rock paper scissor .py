# game logic
def main(): 

    import random

    # user choice 
    user_selection=input(str("Enter your hand signs:"))

    # computer choice
    hand_signs=['rock','paper','scissor']
    computer_choice=random.choice(hand_signs)
    print("computer choice:",computer_choice)

    #sign-1
    if user_selection == "rock" and computer_choice == "paper":
        print('computer wins')
    elif user_selection == "rock" and computer_choice == "scissor":
        print('congragualtion you wins')

    #sign-2
    elif user_selection == "paper" and computer_choice == "rock":
        print('congragualtion you wins')
    elif user_selection == "paper" and computer_choice == "scissor":
        print('computer wins')

    #sign-3
    elif user_selection == "scissor" and computer_choice == "rock":
        print('computer wins')
    elif user_selection == "scissor" and computer_choice == "paper":
        print('congragualtion you wins')

    #sign same
    if user_selection == "rock" and computer_choice == "rock":
        print(' ☺ play again')
    elif user_selection == "paper" and computer_choice == "paper":
        print(' ☺ play again')
    elif user_selection == "scissor" and computer_choice == "scissor":
        print(' ☺ play again')
    

main()
while True:
  ques1=input("you try again (yes/no):")
  if(ques1=="yes"):
    main()
  else:
    exit()

