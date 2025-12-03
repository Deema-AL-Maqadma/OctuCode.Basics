def welcome():
    print("Welcome to our program ^_^")
def end():
    print("Thx ^_^ ... See U !")
welcome()
input("Press enter to exit ...")
end()
print("********************************************")
import random
rand_int=random.randint(1,10)
entry_int=int(input("Gess a number between 1 and 10 : "))
if entry_int>=1 and entry_int<=10: 
 while entry_int!=rand_int:
    if entry_int>rand_int:
        print("Too high! Gess again :")
        entry_int=int(input("Gess a number between 1 and 10 : "))
    elif entry_int<rand_int:
        print("Too law ! Gess again :")
        entry_int=int(input("Gess a number between 1 and 10 : "))
    
 print("Congratulation ! you gessed the number !*_*")
    
else:
   print("Invalid value ! out of the range ...")
print("********************************************")
