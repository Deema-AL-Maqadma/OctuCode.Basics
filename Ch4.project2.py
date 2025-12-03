# Gess Coin 
import random
print("Welcome to the virtual coin tos game ...")
input("Press enter to start...") # توقف الكود مؤقتا حتى يضغط المستخدم enter
random_number = random.randint(0,1)# اختيار رقم عشوتىي صحيح بين0و1
#لو هستخدم نفس الكود لكن بميثود.random()حتى يكون الحل منصف بغير الشرط >=0.5
if random_number==0:
    print("Heads")
else:
    print("Tails")
print("*****************************************")
# Gess Coin Game ..
print("""Welcome to the coin Guessing Game!
      Choose a method to toss the coin:
      1- Using Random.random()
      2- Using Random.randint()
      """)
choise=int(input("Enter your choise (1 or 2):"))
if choise==1:
    entery=input("Enter your Gess(Head or Tails) :").lower()
    random_number = random.random()
    if random_number>=0.5:
        if entery=="head":
          print("""Congratulation1 you won!
                The computer's coin toss result was: Head""")
        else:
          print("""Sorry, you lost!
                The computer's coin toss result was: Head""")
    else:
        if entery=="tails":
          print("""Congratulation1 you won!
                The computer's coin toss result was: Tails""")
        else:
          print("""Sorry, you lost!
                The computer's coin toss result was: Tails""")
elif choise==2:
    entery=input("Enter your Gess(Head or Tails) :").lower()
    random_number = random.randint(0,1)
    if random_number==0:
        if entery=="head":
          print("""Congratulation1 you won!
                The computer's coin toss result was: Head""")
        else:
          print("""Sorry, you lost!
                The computer's coin toss result was: Head""")
    else:
        if entery=="tails":
          print("""Congratulation1 you won!
                The computer's coin toss result was: Tails""")
        else:
          print("""Sorry, you lost!
                The computer's coin toss result was: Tails""")
else :
    print("Invalid choise ...")