# List  of things
colors =[]
colors.append(input("Add the first color you like : "))
choice=input("Do you want to add more colors ? (Yes,No) : ").lower()
if choice=="yes":
    colors.append(input("Add another color to the list : "))
    print("The colors you like are :\n",colors)
else:
    print("The colors you like are :\n",colors)
print("*****************************************")
# لجمع محتوى قائمتينتن باستخدام قائمة جديدة
class_a=["Ahmed","Ali"]
class_b=["Deema","Yara"]
all_students=class_a+class_b
print(all_students)
all_students=[]
all_students.extend(class_a)
all_students.extend(class_b)
print(all_students)
all_students.remove("Ali")
print(all_students)
all_students.append("Sami")
print(all_students)
print("*****************************************")
# Validation if the user enter a word
name=input("Enter your name :")
if name:
    print("Hello ,",name)
else:
    print("You forgot to enter ypur name !")
print("*****************************************")
# Validation if a spacific element in the list
fruit_basket=["Appels","Oranges","Bananas"]
gess=input("Gess the name of fruits in the basket :")
if gess in fruit_basket:
    print("Good gess ...")
else:
    print("Sorry, better luck next time !")
print("*****************************************")
