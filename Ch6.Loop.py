# loop
numbers=[1,2,3,4,5,6,7,8,9,10]
for x in numbers:
    if x%2==0:
        print(x,"\n")
print("Finished the loop successfully")
print("*******************************************")
name="Deema"
for y in name:
    print(y.upper())
print("*******************************************")
colors=["Red","Blue","Green","Black"]
for color in colors:
    print(color)
print("*******************************************")
attendees=["Deema","Zain","Ali"]
for person in attendees:
    print(person)
    response = input ("Is this person attending ? (Yes \ No) :").lower()
    if response=="yes":
        print("Attendance confirmed !")
    else:
        print("Attendance Not confirmed !")
    print("=========================")
print("*******************************************")
gests=input("Enter the names of gests sepsrated by comma :\n").split(",")
for person in gests:
    print("\n",person,"\n")
    response = input ("Is this person attending ? (Yes \ No) :").lower()
    if response=="yes":
        print("Attendance confirmed !")
    else:
        print("Attendance Not confirmed !")
    print("=========================")
print("*******************************************")
items=[]
prices=[]
num_items=int(input("*** Welcom to iShop calculator ***\nHow many items are there in your basket ?"))
if num_items>0:
    print("Lites counting them ....")
    for i in range(0,num_items):
        name =input(f"Please tell me the name of the item number {i+1}")#ضفنا واحد ليبدا العد مثل البشر وليس من الصفر
        items.append(name)
        price =float(input(f"What is the price of {name}"))
        prices.append(price)
    choice=input("Would you like to see your entaire bsket items ? ").lower()
    if choice=="yes":
        print(items)
        see_price=input("Would you like to see how mutch it'll cost ? ").lower()
        if see_price=="yes":
          print("Buying these items will cost :\n",sum(prices))
        else:
          input("Press enter to exit ...")
    else:
        input("Press enter to exit ...")
else:
        input("Seems like you're not in the mood for shopping today ...")
print("*******************************************")
name = "Deema"
name +=" AL-Maqadma "
name *=3
print(name)
print("*******************************************")
