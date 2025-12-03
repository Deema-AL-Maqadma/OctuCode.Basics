# طريقة اختيار قيمة عشوائية من قائمة 
import random
names = input(""" Welcom to whose wallet?
             You will give me a list of names, and I will pick a person to pay 
             If your ready, enter the namrs separated by a comma :\n  """).split(", ")#تقسيم المدخل لعناصر تفصل بينها فاصلة ومسافة وتخزينها داخل القائمة التالية
length=len(names)-1
picked_one=random.randrange(0,length)
print("Please ask ",names[picked_one]," to take his wallet out. Dinner is on him ...")
print("**********************************************")
# اختصار اكبر للكود
names = input(""" Welcom to whose wallet?
             You will give me a list of names, and I will pick a person to pay 
             If your ready, enter the namrs separated by a comma :\n  """).split(", ")#تقسيم المدخل لعناصر تفصل بينها فاصلة ومسافة وتخزينها داخل القائمة التالية
print("Please ask ",random.choice(names)," to take his wallet out. Dinner is on him ...")
print("**********************************************")
# اختصار اكبر للكود
print("Welcom to whose wallet ? \nYou will give me a list of names, and I will pick a person to pay If your ready")
print("Please ask ",random.choice(input("enter the namrs separated by a comma :\n  """).split(", "))," to take his wallet out. Dinner is on him ...")
print("**********************************************")
# Nested list والتعديل عليها
my_list=[['Apples','Bananas'],['Milk','Water']]
print(my_list)
input("Press enter to change the content :")
my_list[0].insert(0,'Oranges')
my_list[0].append('Kiwis')
my_list[1].append('Tea')
my_list.append([1,2,3])
print("Here is the updated List \n",my_list)
# مشروع نقل الارنب للمكان الصحيح 
place=[['🌿','🌿','🌿'],['🌿','🌿','🌿'],['🌿','🌿','🌿']]
print("Welcome to place the rabbit \n",
      place[0],"\n",place[1],"\n",place[2])# لطباعة القائمة كل صف بسطر
go=input("Where should the rabbit go?\nPlease choose a row and a colomn :")
row=int(go[0])#القيمة المدخلة عبارة عن نص بالتالي لازم تخزنهتا كرقم للتعامل معها في الليست 
column=int(go[1])
place[row-1][column-1]='🐇'# نطرح واحد لان الحاسوب يبدا العد من الصفر بالتالي نطرح لتكون القيمة دقيقة
print ("SUCCESS !\n",place[0],"\n",place[1],"\n",place[2])
