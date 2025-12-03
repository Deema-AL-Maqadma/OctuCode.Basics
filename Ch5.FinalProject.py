# Rock, Paper, Scissor Game
import random
rock_ascii='👊'
paper_ascii='✋'
seissor_ascii='✌️'
print("Welcome to the -->> Rock, Paper, Scissor Game <<--")
confirm=input("Press Enter to continue or type (Help) for the rules .").lower()
if confirm=="help":
    print("""
           ********* RULES *********
          1) you choose and the computer chooses
          2) rock smashes scissor -> Rock wins
          3) scissor cut paper -> Scissor win
          4) paper covers rock ->Paper wins

         """)
user_select=input("Enter your choic (Rock, Paper, Scissor) :").lower()
if user_select not in ["rock", "paper", "scissors"]:
    print("Invalid choice! please run the program again and choose (Rock, Paper, Scissor)... ")
else :
    # Display user choice in ascii
    if user_select=="rock":
        print("you choose \n",rock_ascii)
    elif user_select=="paper":
        print("you choose \n",paper_ascii)
    else:
        print("you choose \n",seissor_ascii)
# computer choice
computer_choice=random.choice(["rock", "paper", "scissors"])
if computer_choice=="rock":
     print("computer choose \n",rock_ascii)
elif computer_choice=="paper":
    print("computer choose \n",paper_ascii)
else:
    print("computer choose \n",seissor_ascii)
# Determine the winner
if user_select==computer_choice: # في حالة التعادل
    print("It's a tie !")
elif(
   ( user_select=="rock" and computer_choice=="scissors")
   or ( user_select=="paper" and computer_choice=="rock")
   or ( user_select=="scissors" and computer_choice=="paper")
):
    print("you win ! ",user_select," beats ",computer_choice)
else:
        print("you lose ! ",computer_choice," beats ",user_select)

