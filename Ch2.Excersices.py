#حساب طول ونوع الرقم السري المدخل من قبل المستخم
pin = input("Enter your PIN number  :\n") #ترجع بقيمة نصية string
print("The length = ",len(pin))  
print('The Typet = ' ,type(pin))
print("The Type after converting = ",type(int(pin)))
print("******************************************")
print(type("Deema"))
print(type(25))
print(type(True))
print(type(2.15))
print("******************************************")
print(5+4)
print(5-4)
print(5*4)
print(5/4) # القسمة يكون الناتج عشري
print(5%4) 
print(5//4) # floor devision الجزء الصحيح وتحذف الجزء العشري 
print(5**4) # الاس
print("******************************************")
# Q/Compute the area & price //
length = float(input("Enter the length of the room : \n"))
width  = float(input("Enter the width of the room : \n"))
price  = float(input("Enter the price of one meter : \n"))
area = length*width
total_price = area*price
print("-> The Area Of the room = ", area)
print("-> The Total Price Of the room = ", total_price)
print("******************************************")
# برنامج يدخل المستخدم عدد الثواني واحسب عدد الساعات والدقاىق والثواني
second = int(input("Enter the second : \n"))
minute = second//60
hour = minute// 60
remaining_second = second%60
print("-> The Hours = ",hour ,"\n-> The Minutes = ",minute ,"\n-> The Second = ",remaining_second)
print("******************************************")
# برنامج لاحضار سنة الميلاد 
age = int(input("How old are you : \n"))
print(f"you were born in the {2025-age} year")