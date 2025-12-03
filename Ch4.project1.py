# How to use { Random } Module
# Gess the PIN number
import random
pin_code = random.randint(1000,9999) #لاختيار رقم عشواىي من اربع خانات
user_input = int(input("Enter a 4-deget PIN code :"))
if len(str(user_input))!=4:
    print("You must enter 4-digit ...")
elif user_input==pin_code:
    print("Success! PIN code matched")
else:
    print("Failure! PIN code NOT matched")
    print(f"The computer enterd {pin_code}")