import random
user_win=0
computer_win=0
option=["stone" , "paper" , "scissor" , "q"]
while True:
  user_input = input("enter stone / paper / scissor or q to quite : ").lower()
  if user_input == "q":  
    break
  if user_input not in option:
    continue
  computer_chose = option[random.randint(0 , 2)]
  print("computer chose" , computer_chose )
  if user_input == computer_chose:
    print("tie")
  elif user_input == "stone" and computer_chose == "scissor":
    print("you win")
    user_win += 1
    continue
  elif user_input == "paper" and computer_chose == "stone":
    print("you win")
    user_win += 1
    continue
  elif user_input == "scissor" and computer_chose == "paper":
    print("you win")
    user_win += 1
    continue
  else:
    print("you lose")
    computer_win += 1
    continue
print("you won" , user_win , "times")
print("computer won" , computer_win , "times")
