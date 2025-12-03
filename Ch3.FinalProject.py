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


     