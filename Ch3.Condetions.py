#--->>> checkeing if the number is negative or positive
number = float(input("Enter a number : \n"))
if number>0 :
    print("The number is positive")
elif number<0 :
     print("The number is negative")
else :
     print("The number is zero")
print("**********************************************")
grade = float(input("Enter youe grade : \n"))
if grade>=90 and grade<=100:
     print("A")
elif grade>=75:
     print("B")
elif grade>=50:
     print("C")
else :
     print("F")
print("**********************************************")
#--->>> passworde checker 
passworde = input("Enter your passworde :\n")
if passworde == "abc" :
     print("You are Accept")
else :
     print("Ypur NOT Accept!")
print("**********************************************")
word = input("Enter a word [yes, no , maybe] : \n")  
if word.lower()== "yes":
     print("You chose yes ")
elif word.lower()== "no":
     print("You chose no ")
elif word.lower()== "maybe":
     print("You chose maybe ")
else :
     print("INVALID CHOICE ! ")
print("**********************************************")
#--->>> Gess the number 
num = int(input("Expecte a number : \n"))
correct_num = 5 
if num==correct_num:
     print("Correct *_*")
else :
     print(f"You gessed {num} , but the correct is {correct_num} !!!")
print("**********************************************")
# --->>> Driving license 
age = int(input("Enter your age : \n"))
license = input("Do you have a license ? [yes , no] : \n")
if age>=18 and license.lower()=="yes":
     print("You can Drive ...")
elif age<18 or license.lower()=="no":
     print("Sorry , You can NOT Drive !")
else :
     print(f"Sorry , You entry of [{license}] is not understood !")
print("**********************************************")
# Nested if 
# input checker 
# تنفيذ الكود التالي بناء على تحقق الشرط السابق والا ينتهي البرنامج
# --->>> Validation of having ID
is_palestinian = input("Are you a palestinian ? [yes,no] \n").lower()  #تحويل المدخل لسمول ثم تخزينه داخل المتغير
if is_palestinian=="yes":
     print("Good, that's the first step")
     is_18 = input("Are you a 18 ? [yes,no] \n").lower()
     if is_18=="yes":
          print("You can have an ID ...")
     else :
          print("""Sorry , You have to be 18 or older !
                Please try again when you are 18 ... """)
else:
     print("Sorry , An Palestinian ID is give only to Palestinian ...")
print("**********************************************")
 # Final Project (Treasure Island)
print("""☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️
              💀🪨💀🪨💀🪨💀🪨💀🪨💀🪨💀
                🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️
                      ❌🚫❌
          *+*+*+* 🌴Treasure Island🌴 *+*+*+*
                      ❌🚫❌
                🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️
              💀🪨💀🪨💀🪨💀🪨💀🪨💀🪨💀
         ☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️
      

      Welcome to my island !🏴‍☠️
There are two doors in front of you . 
      a🔴🚪Red door & a 🔵🚪Blue door 
       """)
door = input("which door do you want to open ?").lower()
if door=="blue":
     print("OOP! You chose the crocodile door 🐊🐊🐊🐊\n Game Over!")
elif door=="red":
     print("""Great! now you enterd the room
          you found three boxes 🎁White 🎁Black 🎁Green """)
     box=input("which box do you want to open ?").lower()
     if box=="white":
          print("Oops! you opened a box filled with snakes 🐍🐍🐍🐍")
     elif box=="black":
          print("Oops! you opened a box filled with spiders 🕷🕷🕷🕸")
     elif box=="green":
          print("""🏅 Congratulation 🏅!
                 You found the treasure
                     🎁🎁🎁🎁🎁🎁
                💰💰💰💰💰💰💰💰💰💰💰💰
                👑👑👑👑👑👑👑👑👑👑
                """)
     else:
       print("Invalid Choice !!!")
else:
     print("Invalid Choice !!!")


     